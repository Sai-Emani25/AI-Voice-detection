import os
import google.generativeai as genai
import json

class VoiceClassifier:
    def __init__(self, api_key: str = None):
        """
        Initialize the classifier with Gemini API.
        
        Args:
            api_key: Google Gemini API key. If not provided, will look for GEMINI_API_KEY env variable.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "Gemini API key is required. Set GEMINI_API_KEY environment variable or pass api_key parameter."
            )
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        # Using gemini-1.5-flash for cost-effective text generation
        # If this model is not available, try: gemini-1.5-pro, gemini-pro, or check available models
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.is_loaded = True
        print("Gemini API initialized successfully.")

    def predict(self, features: dict):
        """
        Predicts whether the voice is AI-generated or Human using Gemini AI.
        
        Args:
            features (dict): extracted features from preprocessing.
            
        Returns:
            dict: {
                "classification": "AI-Generated" | "Human",
                "confidence_score": float (0.0 to 1.0),
                "explanation": str
            }
        """
        try:
            # Prepare prompt with audio features for Gemini
            prompt = f"""
You are an expert audio forensics AI specializing in detecting AI-generated voices.

Analyze the following audio features and determine if this voice is AI-Generated or Human:

Audio Features:
- Duration: {features.get('duration', 0):.2f} seconds
- Spectral Centroid (mean): {features.get('spectral_centroid_mean', 0):.2f} Hz
- Spectral Rolloff (mean): {features.get('spectral_rolloff_mean', 0):.2f} Hz
- Zero Crossing Rate (mean): {features.get('zero_crossing_rate_mean', 0):.6f}
- RMS Energy (mean): {features.get('rms_mean', 0):.6f}
- MFCC Features: Available

Based on these audio characteristics, provide your analysis in the following JSON format:
{{
  "classification": "AI-Generated" or "Human",
  "confidence_score": a number between 0.0 and 1.0,
  "explanation": "Detailed explanation of your analysis"
}}

Key indicators to look for:
- AI-generated voices often have unnatural spectral consistency
- Unusual patterns in zero-crossing rates
- Artificial smoothness in energy levels
- Anomalies in formant transitions

Respond ONLY with valid JSON, no additional text.
"""

            # Call Gemini API
            response = self.model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Clean response to extract JSON
            # Sometimes the model might wrap it in markdown code blocks
            if response_text.startswith("```"):
                # Remove code block markers
                response_text = response_text.replace("```json", "").replace("```", "").strip()
            
            # Parse JSON response
            result = json.loads(response_text)
            
            # Validate and normalize the response
            classification = result.get("classification", "Unknown")
            if classification not in ["AI-Generated", "Human"]:
                # Try to normalize common variations
                classification_lower = classification.lower()
                if "ai" in classification_lower or "generated" in classification_lower:
                    classification = "AI-Generated"
                elif "human" in classification_lower:
                    classification = "Human"
                else:
                    classification = "Unknown"
            
            confidence_score = float(result.get("confidence_score", 0.5))
            confidence_score = max(0.0, min(1.0, confidence_score))  # Clamp between 0 and 1
            
            explanation = result.get("explanation", "Analysis completed using Gemini AI.")
            
            return {
                "classification": classification,
                "confidence_score": round(confidence_score, 4),
                "explanation": explanation
            }
            
        except json.JSONDecodeError as e:
            print(f"Failed to parse Gemini response: {response_text}")
            # Fallback: Try to extract information from text
            response_lower = response_text.lower()
            if "ai-generated" in response_lower or "ai generated" in response_lower:
                classification = "AI-Generated"
            elif "human" in response_lower:
                classification = "Human"
            else:
                classification = "Unknown"
            
            return {
                "classification": classification,
                "confidence_score": 0.5,
                "explanation": f"Analysis completed but response format was unexpected. Raw response: {response_text[:200]}"
            }
            
        except Exception as e:
            print(f"Error during Gemini prediction: {e}")
            return {
                "classification": "Unknown",
                "confidence_score": 0.0,
                "explanation": f"Error during analysis: {str(e)}"
            }
