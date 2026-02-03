from fastapi import FastAPI, HTTPException, Body, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi import Request
from pydantic import BaseModel, Field
from typing import Optional
from preprocessing import decode_audio, extract_features
from model import VoiceClassifier
import uvicorn
import sys
import json
import base64
import asyncio

# Initialize FastAPI app
app = FastAPI(
    title="AI Voice Detection API",
    description="API to detect AI-generated voices in multiple languages.",
    version="1.0.0"
)

# Initialize the classifier (in a real app, you'd load the model path here)
classifier = VoiceClassifier()

class AudioRequest(BaseModel):
    audio_base64: str = Field(..., description="Base64 encoded MP3 audio string")
    language: str = Field(..., description="Language of the audio (Tamil, English, Hindi, Malayalam, Telugu, Kannada)")

class AudioResponse(BaseModel):
    classification: str
    confidence_score: float
    explanation: str
    metadata: Optional[dict] = None

@app.get("/", response_class=HTMLResponse)
async def root(request: Request, format: str | None = None):
    accept = request.headers.get("accept", "")
    if format == "json" or "application/json" in accept:
        return JSONResponse({
            "status": "active",
            "message": "AI Voice Detection System is running",
            "endpoints": {
                "detect": "/detect",
                "docs": "/docs",
                "app": "/app",
                "health": "/health"
            }
        })
    return """
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
<<<<<<< HEAD
      <title>AI Voice Detection - Advanced Audio Analysis</title>
      <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
          font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          min-height: 100vh;
          padding: 2rem 1rem;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .container {
          max-width: 900px;
          width: 100%;
          animation: fadeIn 0.5s ease-in;
        }
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .card { 
          background: rgba(255, 255, 255, 0.95);
          backdrop-filter: blur(10px);
          border-radius: 20px;
          padding: 2.5rem;
          box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
          transition: transform 0.3s ease;
        }
        .card:hover { transform: translateY(-5px); }
        .header {
          text-align: center;
          margin-bottom: 2rem;
        }
        h1 { 
          font-size: 2.2rem;
          font-weight: 700;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
          margin-bottom: 0.5rem;
        }
        .subtitle {
          font-size: 1rem;
          color: #64748b;
          margin-bottom: 1.5rem;
        }
        .links { 
          display: flex;
          gap: 1rem;
          justify-content: center;
          flex-wrap: wrap;
          margin-bottom: 2rem;
        }
        .links a { 
          color: #667eea;
          text-decoration: none;
          padding: 0.5rem 1rem;
          border-radius: 8px;
          background: rgba(102, 126, 234, 0.1);
          transition: all 0.3s ease;
          font-size: 0.9rem;
        }
        .links a:hover { 
          background: rgba(102, 126, 234, 0.2);
          transform: translateY(-2px);
        }
        .form-section {
          background: #f8fafc;
          border-radius: 12px;
          padding: 1.5rem;
          margin-bottom: 1.5rem;
        }
        label { 
          display: block;
          margin-bottom: 0.5rem;
          font-weight: 600;
          color: #334155;
          font-size: 0.95rem;
        }
        .input-group {
          display: grid;
          grid-template-columns: 1fr;
          gap: 1.5rem;
          margin-bottom: 1.5rem;
        }
        @media (min-width: 640px) { 
          .input-group { grid-template-columns: 1fr 1fr; }
        }
        input[type=file] {
          width: 100%;
          padding: 0.75rem;
          border: 2px dashed #cbd5e1;
          border-radius: 10px;
          background: white;
          cursor: pointer;
          transition: all 0.3s ease;
          font-size: 0.9rem;
        }
        input[type=file]:hover {
          border-color: #667eea;
          background: #f1f5fe;
        }
        select, textarea { 
          width: 100%;
          padding: 0.75rem;
          border: 2px solid #e2e8f0;
          border-radius: 10px;
          background: white;
          font-size: 0.95rem;
          transition: all 0.3s ease;
          font-family: inherit;
        }
        select:focus, textarea:focus, input[type=file]:focus { 
          outline: none;
          border-color: #667eea;
          box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        button { 
          width: 100%;
          padding: 1rem;
          border: none;
          border-radius: 12px;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          color: white;
          font-size: 1.1rem;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.3s ease;
          box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        }
        button:hover:not(:disabled) { 
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
        }
        button:active:not(:disabled) { 
          transform: translateY(0);
        }
        button:disabled { 
          background: linear-gradient(135deg, #94a3b8 0%, #cbd5e1 100%);
          cursor: not-allowed;
          box-shadow: none;
        }
        .spinner {
          display: none;
          width: 20px;
          height: 20px;
          border: 3px solid rgba(255,255,255,0.3);
          border-top-color: white;
          border-radius: 50%;
          animation: spin 0.8s linear infinite;
          margin: 0 auto;
        }
        @keyframes spin {
          to { transform: rotate(360deg); }
        }
        button:disabled .spinner {
          display: inline-block;
        }
        button:disabled .btn-text {
          display: none;
        }
        .result-container {
          margin-top: 1.5rem;
          animation: slideIn 0.3s ease-out;
        }
        @keyframes slideIn {
          from { opacity: 0; transform: translateY(10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        pre { 
          background: #0f172a;
          color: #e2e8f0;
          padding: 1.5rem;
          border-radius: 12px;
          overflow: auto;
          font-size: 0.9rem;
          line-height: 1.6;
          box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
        }
        .result-ai {
          border-left: 4px solid #ef4444;
          background: #fef2f2;
          color: #991b1b;
        }
        .result-human {
          border-left: 4px solid #10b981;
          background: #f0fdf4;
          color: #065f46;
        }
        textarea {
          resize: vertical;
          min-height: 80px;
        }
        .divider {
          height: 1px;
          background: linear-gradient(to right, transparent, #e2e8f0, transparent);
          margin: 1.5rem 0;
        }
        .badge {
          display: inline-block;
          padding: 0.25rem 0.75rem;
          border-radius: 20px;
          font-size: 0.85rem;
          font-weight: 600;
        }
        .badge-ai {
          background: #fee2e2;
          color: #dc2626;
        }
        .badge-human {
          background: #dcfce7;
          color: #16a34a;
        }
        .tabs {
          display: flex;
          gap: 0.5rem;
          margin-bottom: 1.5rem;
          border-bottom: 2px solid #e2e8f0;
        }
        .tab {
          padding: 0.75rem 1.5rem;
          background: none;
          border: none;
          border-bottom: 3px solid transparent;
          cursor: pointer;
          font-weight: 600;
          color: #64748b;
          transition: all 0.3s ease;
          font-size: 0.95rem;
        }
        .tab:hover {
          color: #667eea;
        }
        .tab.active {
          color: #667eea;
          border-bottom-color: #667eea;
        }
        .tab-content {
          display: none;
        }
        .tab-content.active {
          display: block;
        }
        .live-monitor-section {
          background: #f8fafc;
          border-radius: 12px;
          padding: 1.5rem;
          margin-bottom: 1.5rem;
        }
        .monitor-controls {
          display: flex;
          gap: 1rem;
          margin-bottom: 1.5rem;
          align-items: center;
          flex-wrap: wrap;
        }
        .monitor-btn {
          padding: 0.75rem 1.5rem;
          border: none;
          border-radius: 10px;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.3s ease;
          font-size: 0.95rem;
        }
        .monitor-btn.start {
          background: linear-gradient(135deg, #10b981 0%, #059669 100%);
          color: white;
          box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
        }
        .monitor-btn.start:hover {
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
        }
        .monitor-btn.stop {
          background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
          color: white;
          box-shadow: 0 4px 15px rgba(239, 68, 68, 0.4);
        }
        .monitor-btn.stop:hover {
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(239, 68, 68, 0.5);
        }
        .monitor-btn:disabled {
          background: #cbd5e1;
          cursor: not-allowed;
          box-shadow: none;
          transform: none;
        }
        .status-indicator {
          display: flex;
          align-items: center;
          gap: 0.5rem;
          padding: 0.5rem 1rem;
          border-radius: 8px;
          font-weight: 600;
          font-size: 0.9rem;
        }
        .status-indicator.idle {
          background: #f1f5f9;
          color: #64748b;
        }
        .status-indicator.listening {
          background: #dbeafe;
          color: #1e40af;
        }
        .status-pulse {
          width: 10px;
          height: 10px;
          border-radius: 50%;
          background: currentColor;
          animation: pulse 1.5s ease-in-out infinite;
        }
        @keyframes pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.5; }
        }
        .alert-banner {
          display: none;
          padding: 1rem;
          border-radius: 10px;
          margin-bottom: 1rem;
          font-weight: 600;
          animation: slideDown 0.3s ease-out;
        }
        @keyframes slideDown {
          from { opacity: 0; transform: translateY(-10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .alert-banner.show {
          display: flex;
          align-items: center;
          gap: 0.75rem;
        }
        .alert-banner.ai-detected {
          background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
          color: #991b1b;
          border-left: 4px solid #dc2626;
        }
        .alert-icon {
          font-size: 1.5rem;
          animation: shake 0.5s ease-in-out;
        }
        @keyframes shake {
          0%, 100% { transform: translateX(0); }
          25% { transform: translateX(-5px); }
          75% { transform: translateX(5px); }
        }
        .detection-history {
          max-height: 200px;
          overflow-y: auto;
          background: white;
          border-radius: 8px;
          padding: 0.75rem;
          margin-top: 1rem;
        }
        .detection-item {
          padding: 0.5rem;
          border-bottom: 1px solid #f1f5f9;
          font-size: 0.85rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        .detection-item:last-child {
          border-bottom: none;
        }
        .audio-visualizer {
          height: 60px;
          background: #0f172a;
          border-radius: 8px;
          margin-top: 1rem;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 2px;
          padding: 0.5rem;
        }
        .viz-bar {
          width: 4px;
          background: linear-gradient(to top, #667eea, #764ba2);
          border-radius: 2px;
          transition: height 0.1s ease;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <div class="card">
          <div class="header">
            <h1>🎙️ AI Voice Detection</h1>
            <p class="subtitle">Advanced AI-powered audio analysis for detecting synthetic voices</p>
            <div class="links">
              <a href="/docs">📚 API Docs</a>
              <a href="/health" target="_blank">💚 Health Check</a>
              <a href="/?format=json" target="_blank">🔗 API Info</a>
            </div>
          </div>
          
          <!-- Tabs -->
          <div class="tabs">
            <button class="tab active" data-tab="file-upload">📁 File Upload</button>
            <button class="tab" data-tab="live-monitor">🔴 Live Monitor</button>
          </div>
          
          <!-- File Upload Tab -->
          <div class="tab-content active" id="file-upload">
            <div class="form-section">
              <div class="input-group">
                <div>
                  <label for="file">🎵 Audio File (WAV/MP3)</label>
                  <input id="file" type="file" accept=".wav,.mp3,audio/*">
                </div>
                <div>
                  <label for="lang">🌍 Language</label>
                  <select id="lang">
                    <option>English</option>
                    <option>Tamil</option>
                    <option>Hindi</option>
                    <option>Malayalam</option>
                    <option>Telugu</option>
                    <option>Kannada</option>
                  </select>
                </div>
              </div>
              
              <button id="send">
                <span class="btn-text">🔍 Analyze Audio</span>
                <div class="spinner"></div>
              </button>
            </div>
            
            <div class="divider"></div>
            
            <div>
              <label for="base64">🔐 Or Paste Base64 Audio (Optional)</label>
              <textarea id="base64" placeholder="Paste your Base64 encoded audio string here..."></textarea>
            </div>
            
            <div id="out" class="result-container">
              <label>📊 Analysis Result</label>
              <pre id="result">{ "status": "Ready to analyze audio" }</pre>
            </div>
          </div>
          
          <!-- Live Monitor Tab -->
          <div class="tab-content" id="live-monitor">
            <div id="ai-alert" class="alert-banner ai-detected">
              <span class="alert-icon">🚨</span>
              <div>
                <strong>AI-Generated Voice Detected!</strong>
                <div style="font-size: 0.85rem; margin-top: 0.25rem;">Confidence: <span id="alert-confidence">0</span>%</div>
              </div>
            </div>
            
            <div class="live-monitor-section">
              <div class="monitor-controls">
                <button id="start-monitor" class="monitor-btn start">
                  🎙️ Start Live Monitoring
                </button>
                <button id="stop-monitor" class="monitor-btn stop" disabled>
                  ⏹️ Stop Monitoring
                </button>
                <div id="monitor-status" class="status-indicator idle">
                  <span class="status-pulse"></span>
                  <span>Idle</span>
                </div>
                <select id="live-lang" style="padding: 0.5rem; border-radius: 8px; border: 2px solid #e2e8f0;">
                  <option>English</option>
                  <option>Tamil</option>
                  <option>Hindi</option>
                  <option>Malayalam</option>
                  <option>Telugu</option>
                  <option>Kannada</option>
                </select>
              </div>
              
              <div class="audio-visualizer" id="visualizer">
                <div class="viz-bar" style="height: 10px;"></div>
                <div class="viz-bar" style="height: 15px;"></div>
                <div class="viz-bar" style="height: 20px;"></div>
                <div class="viz-bar" style="height: 25px;"></div>
                <div class="viz-bar" style="height: 20px;"></div>
                <div class="viz-bar" style="height: 15px;"></div>
                <div class="viz-bar" style="height: 10px;"></div>
                <div class="viz-bar" style="height: 15px;"></div>
                <div class="viz-bar" style="height: 20px;"></div>
                <div class="viz-bar" style="height: 25px;"></div>
                <div class="viz-bar" style="height: 30px;"></div>
                <div class="viz-bar" style="height: 25px;"></div>
                <div class="viz-bar" style="height: 20px;"></div>
                <div class="viz-bar" style="height: 15px;"></div>
                <div class="viz-bar" style="height: 10px;"></div>
              </div>
              
              <div>
                <label style="margin-top: 1rem; display: block;">📜 Detection History</label>
                <div class="detection-history" id="detection-history">
                  <div style="text-align: center; color: #94a3b8; padding: 1rem;">
                    Start monitoring to see detections
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <script>
        // Tab switching
        document.querySelectorAll('.tab').forEach(tab => {
          tab.addEventListener('click', () => {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            tab.classList.add('active');
            document.getElementById(tab.dataset.tab).classList.add('active');
          });
        });
        
        // File upload functionality
=======
      <title>AI Voice Detection</title>
      <style>
        body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 2rem; }
        .card { max-width: 800px; margin: 0 auto; border: 1px solid #eee; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
        h1 { font-size: 1.6rem; margin-bottom: 1rem; }
        label { display: block; margin: .5rem 0 .25rem; font-weight: 600; }
        input[type=file], select, textarea { width: 100%; padding: .5rem; border: 1px solid #ccc; border-radius: 6px; }
        button { margin-top: 1rem; padding: .6rem 1rem; border: none; border-radius: 6px; background: #2563eb; color: #fff; cursor: pointer; }
        button:disabled { background: #9aa7c7; cursor: not-allowed; }
        pre { background: #0f172a; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; }
        .row { display: grid; grid-template-columns: 1fr; gap: 1rem; }
        @media (min-width: 640px) { .row { grid-template-columns: 1fr 1fr; } }
        .small { font-size: .85rem; color: #555; }
        .links a { margin-right: .75rem; }
      </style>
    </head>
    <body>
      <div class="card">
        <h1>AI-Generated Voice Detection</h1>
        <div class="links">
          <a href="/docs">API Docs</a>
          <a href="/health" target="_blank">Health JSON</a>
          <a href="/?format=json" target="_blank">Root JSON</a>
        </div>
        <p class="small">Upload audio and select language. The API returns classification, confidence, and explanation.</p>
        <div class="row">
          <div>
            <label for="file">Audio file (WAV/MP3)</label>
            <input id="file" type="file" accept=".wav,.mp3,audio/*">
          </div>
          <div>
            <label for="lang">Language</label>
            <select id="lang">
              <option>English</option>
              <option>Tamil</option>
              <option>Hindi</option>
              <option>Malayalam</option>
              <option>Telugu</option>
              <option>Kannada</option>
            </select>
          </div>
        </div>
        <button id="send">Detect</button>
        <div id="out" style="margin-top:1rem;">
          <pre id="result">{ "status": "waiting for input" }</pre>
        </div>
        <p class="small">Or paste Base64 audio below (optional):</p>
        <textarea id="base64" rows="4" placeholder="Base64 audio string"></textarea>
      </div>
      <script>
>>>>>>> 72eee4ab216b8d7567659bc8a18fe88544647020
        async function toBase64(file) {
          return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result.split(',')[1]);
            reader.onerror = reject;
            reader.readAsDataURL(file);
          });
        }
<<<<<<< HEAD
        
        async function detect() {
          const btn = document.getElementById('send');
          const resultPre = document.getElementById('result');
          btn.disabled = true;
          resultPre.textContent = '⏳ Analyzing audio... Please wait.';
          resultPre.className = '';
          
          const fileInput = document.getElementById('file');
          const lang = document.getElementById('lang').value;
          let audioB64 = document.getElementById('base64').value.trim();
          
          try {
            if (!audioB64) {
              const f = fileInput.files[0];
              if (!f) throw new Error('Please select an audio file or paste Base64 audio');
              audioB64 = await toBase64(f);
            }
            
=======
        async function detect() {
          const btn = document.getElementById('send');
          btn.disabled = true;
          const fileInput = document.getElementById('file');
          const lang = document.getElementById('lang').value;
          let audioB64 = document.getElementById('base64').value.trim();
          try {
            if (!audioB64) {
              const f = fileInput.files[0];
              if (!f) throw new Error('Select a file or paste Base64 audio');
              audioB64 = await toBase64(f);
            }
>>>>>>> 72eee4ab216b8d7567659bc8a18fe88544647020
            const res = await fetch('/detect', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ audio_base64: audioB64, language: lang })
            });
<<<<<<< HEAD
            
            const data = await res.json();
            const formatted = JSON.stringify(data, null, 2);
            resultPre.textContent = formatted;
            
            // Add styling based on classification
            if (data.classification && data.classification.toLowerCase().includes('ai')) {
              resultPre.className = 'result-ai';
            } else if (data.classification && data.classification.toLowerCase().includes('human')) {
              resultPre.className = 'result-human';
            }
          } catch (err) {
            resultPre.textContent = JSON.stringify({ 
              error: String(err.message || err),
              timestamp: new Date().toISOString()
            }, null, 2);
            resultPre.className = '';
=======
            const txt = await res.text();
            document.getElementById('result').textContent = txt;
          } catch (err) {
            document.getElementById('result').textContent = JSON.stringify({ error: String(err) }, null, 2);
>>>>>>> 72eee4ab216b8d7567659bc8a18fe88544647020
          } finally {
            btn.disabled = false;
          }
        }
<<<<<<< HEAD
        
        document.getElementById('send').addEventListener('click', detect);
        document.getElementById('file').addEventListener('change', (e) => {
          if (e.target.files[0]) {
            document.getElementById('base64').value = '';
          }
        });
        
        // Live monitoring functionality
        let ws = null;
        let mediaRecorder = null;
        let audioContext = null;
        let analyser = null;
        let animationId = null;
        let recordingInterval = null;
        
        async function startLiveMonitoring() {
          try {
            // Request microphone access
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            
            // Setup WebSocket connection
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            ws = new WebSocket(`${protocol}//${window.location.host}/ws/live-monitor`);
            
            ws.onopen = () => {
              console.log('WebSocket connected');
              updateMonitorStatus('listening', 'Listening...');
            };
            
            ws.onmessage = (event) => {
              const data = JSON.parse(event.data);
              if (data.type === 'detection_result') {
                handleDetectionResult(data);
              }
            };
            
            ws.onerror = (error) => {
              console.error('WebSocket error:', error);
              stopLiveMonitoring();
            };
            
            ws.onclose = () => {
              console.log('WebSocket disconnected');
            };
            
            // Setup audio visualization
            audioContext = new (window.AudioContext || window.webkitAudioContext)();
            analyser = audioContext.createAnalyser();
            const source = audioContext.createMediaStreamSource(stream);
            source.connect(analyser);
            analyser.fftSize = 32;
            startVisualization();
            
            // Setup MediaRecorder to capture audio chunks
            const options = { mimeType: 'audio/webm' };
            mediaRecorder = new MediaRecorder(stream, options);
            const audioChunks = [];
            
            mediaRecorder.ondataavailable = async (event) => {
              if (event.data.size > 0 && ws && ws.readyState === WebSocket.OPEN) {
                // Convert audio chunk to base64
                const reader = new FileReader();
                reader.onloadend = () => {
                  const base64 = reader.result.split(',')[1];
                  const language = document.getElementById('live-lang').value;
                  ws.send(JSON.stringify({
                    type: 'audio_chunk',
                    audio: base64,
                    language: language
                  }));
                };
                reader.readAsDataURL(event.data);
              }
            };
            
            mediaRecorder.start();
            // Capture audio every 2 seconds
            recordingInterval = setInterval(() => {
              if (mediaRecorder && mediaRecorder.state === 'recording') {
                mediaRecorder.stop();
                mediaRecorder.start();
              }
            }, 2000);
            
            // Update UI
            document.getElementById('start-monitor').disabled = true;
            document.getElementById('stop-monitor').disabled = false;
            
          } catch (error) {
            alert('Error accessing microphone: ' + error.message);
            console.error('Error:', error);
          }
        }
        
        function stopLiveMonitoring() {
          if (mediaRecorder && mediaRecorder.state !== 'inactive') {
            mediaRecorder.stop();
          }
          if (recordingInterval) {
            clearInterval(recordingInterval);
          }
          if (ws) {
            ws.close();
          }
          if (audioContext) {
            audioContext.close();
          }
          if (animationId) {
            cancelAnimationFrame(animationId);
          }
          
          // Reset visualizer bars
          document.querySelectorAll('.viz-bar').forEach(bar => {
            bar.style.height = '10px';
          });
          
          updateMonitorStatus('idle', 'Idle');
          document.getElementById('start-monitor').disabled = false;
          document.getElementById('stop-monitor').disabled = true;
          document.getElementById('ai-alert').classList.remove('show');
        }
        
        function startVisualization() {
          const bars = document.querySelectorAll('.viz-bar');
          const bufferLength = analyser.frequencyBinCount;
          const dataArray = new Uint8Array(bufferLength);
          
          function draw() {
            animationId = requestAnimationFrame(draw);
            analyser.getByteFrequencyData(dataArray);
            
            bars.forEach((bar, i) => {
              const value = dataArray[i] || 0;
              const height = (value / 255) * 50 + 5;
              bar.style.height = height + 'px';
            });
          }
          draw();
        }
        
        function updateMonitorStatus(state, text) {
          const statusEl = document.getElementById('monitor-status');
          statusEl.className = `status-indicator ${state}`;
          statusEl.querySelector('span:last-child').textContent = text;
        }
        
        function handleDetectionResult(data) {
          const isAI = data.classification.toLowerCase().includes('ai');
          const confidence = Math.round(data.confidence_score * 100);
          
          // Show alert if AI detected with high confidence
          if (isAI && confidence > 70) {
            const alertEl = document.getElementById('ai-alert');
            alertEl.classList.add('show');
            document.getElementById('alert-confidence').textContent = confidence;
            
            // Play alert sound (optional)
            try {
              const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
              const oscillator = audioCtx.createOscillator();
              const gainNode = audioCtx.createGain();
              oscillator.connect(gainNode);
              gainNode.connect(audioCtx.destination);
              oscillator.frequency.value = 800;
              oscillator.type = 'sine';
              gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
              gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.5);
              oscillator.start(audioCtx.currentTime);
              oscillator.stop(audioCtx.currentTime + 0.5);
            } catch (e) {
              console.error('Audio alert error:', e);
            }
            
            // Hide alert after 5 seconds
            setTimeout(() => {
              alertEl.classList.remove('show');
            }, 5000);
          }
          
          // Add to history
          addDetectionToHistory(data);
        }
        
        function addDetectionToHistory(data) {
          const historyEl = document.getElementById('detection-history');
          const time = new Date().toLocaleTimeString();
          const isAI = data.classification.toLowerCase().includes('ai');
          const confidence = Math.round(data.confidence_score * 100);
          
          const item = document.createElement('div');
          item.className = 'detection-item';
          item.innerHTML = `
            <span>${time}</span>
            <span class="badge ${isAI ? 'badge-ai' : 'badge-human'}">
              ${data.classification} (${confidence}%)
            </span>
          `;
          
          // Clear placeholder text
          if (historyEl.querySelector('div[style*="text-align"]')) {
            historyEl.innerHTML = '';
          }
          
          historyEl.insertBefore(item, historyEl.firstChild);
          
          // Keep only last 10 items
          while (historyEl.children.length > 10) {
            historyEl.removeChild(historyEl.lastChild);
          }
        }
        
        document.getElementById('start-monitor').addEventListener('click', startLiveMonitoring);
        document.getElementById('stop-monitor').addEventListener('click', stopLiveMonitoring);
=======
        document.getElementById('send').addEventListener('click', detect);
>>>>>>> 72eee4ab216b8d7567659bc8a18fe88544647020
      </script>
    </body>
    </html>
    """

@app.get("/health")
def health_check():
    return {"status": "active", "message": "AI Voice Detection System is running"}

@app.get("/app", response_class=HTMLResponse)
def app_page():
    return """
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="apple-mobile-web-app-capable" content="yes">
      <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
      <title>AI Voice Detection</title>
      <link rel="manifest" href="/manifest.json">
      <style>
        body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 2rem; }
        .card { max-width: 720px; margin: 0 auto; border: 1px solid #eee; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
        h1 { font-size: 1.4rem; margin-bottom: 1rem; }
        label { display: block; margin: .5rem 0 .25rem; font-weight: 600; }
        input[type=file], select, textarea { width: 100%; padding: .5rem; border: 1px solid #ccc; border-radius: 6px; }
        button { margin-top: 1rem; padding: .6rem 1rem; border: none; border-radius: 6px; background: #2563eb; color: #fff; cursor: pointer; }
        button:disabled { background: #9aa7c7; cursor: not-allowed; }
        pre { background: #0f172a; color: #e2e8f0; padding: 1rem; border-radius: 8px; overflow: auto; }
        .row { display: grid; grid-template-columns: 1fr; gap: 1rem; }
        @media (min-width: 640px) { .row { grid-template-columns: 1fr 1fr; } }
        .small { font-size: .85rem; color: #555; }
      </style>
      <script>
        if ('serviceWorker' in navigator) {
          window.addEventListener('load', () => {
            navigator.serviceWorker.register('/sw.js').catch(() => {});
          });
        }
      </script>
    </head>
    <body>
      <div class="card">
        <h1>AI-Generated Voice Detection</h1>
        <p class="small">Upload audio and select language. The API returns classification, confidence, and explanation.</p>
        <div class="row">
          <div>
            <label for="file">Audio file (WAV/MP3)</label>
            <input id="file" type="file" accept=".wav,.mp3,audio/*">
          </div>
          <div>
            <label for="lang">Language</label>
            <select id="lang">
              <option>English</option>
              <option>Tamil</option>
              <option>Hindi</option>
              <option>Malayalam</option>
              <option>Telugu</option>
              <option>Kannada</option>
            </select>
          </div>
        </div>
        <button id="send">Detect</button>
        <div id="out" style="margin-top:1rem;">
          <pre id="result">{ "status": "waiting for input" }</pre>
        </div>
        <p class="small">Or paste Base64 audio below (optional):</p>
        <textarea id="base64" rows="4" placeholder="Base64 audio string"></textarea>
      </div>
      <script>
        async function toBase64(file) {
          return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result.split(',')[1]);
            reader.onerror = reject;
            reader.readAsDataURL(file);
          });
        }
        async function detect() {
          const btn = document.getElementById('send');
          btn.disabled = true;
          const fileInput = document.getElementById('file');
          const lang = document.getElementById('lang').value;
          let audioB64 = document.getElementById('base64').value.trim();
          try {
            if (!audioB64) {
              const f = fileInput.files[0];
              if (!f) throw new Error('Select a file or paste Base64 audio');
              audioB64 = await toBase64(f);
            }
            const res = await fetch('/detect', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ audio_base64: audioB64, language: lang })
            });
            const txt = await res.text();
            document.getElementById('result').textContent = txt;
          } catch (err) {
            document.getElementById('result').textContent = JSON.stringify({ error: String(err) }, null, 2);
          } finally {
            btn.disabled = false;
          }
        }
        document.getElementById('send').addEventListener('click', detect);
      </script>
    </body>
    </html>
    """

@app.get("/manifest.json", response_class=JSONResponse)
def manifest():
    return {
        "name": "AI Voice Detection",
        "short_name": "VoiceDetect",
        "start_url": "/app",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#2563eb",
        "icons": []
    }

@app.get("/sw.js", response_class=PlainTextResponse)
def service_worker():
    return """
    self.addEventListener('install', (event) => {
      self.skipWaiting();
    });
    self.addEventListener('activate', (event) => {
      event.waitUntil(clients.claim());
    });
    self.addEventListener('fetch', (event) => {
      event.respondWith(fetch(event.request));
    });
    """
<<<<<<< HEAD

=======
>>>>>>> 72eee4ab216b8d7567659bc8a18fe88544647020
@app.post("/detect", response_model=AudioResponse)
async def detect_voice(request: AudioRequest):
    """
    Analyzes the uploaded audio and returns whether it is AI-generated or Human.
    """
    # Validate language
    supported_languages = ["tamil", "english", "hindi", "malayalam", "telugu", "kannada"]
    if request.language.lower() not in supported_languages:
        # We can just warn or proceed, but let's strictly validate for now or just allow it.
        # The prompt says "Voice samples will be provided in five languages", implying these are the expected ones.
        pass 

    try:
        # 1. Decode Audio
        y, sr = decode_audio(request.audio_base64)
        
        # 2. Extract Features
        features = extract_features(y, sr)
        
        # 3. Predict
        result = classifier.predict(features)
        
        # 4. Construct Response
        return AudioResponse(
            classification=result["classification"],
            confidence_score=result["confidence_score"],
            explanation=result["explanation"],
            metadata={
                "duration_seconds": features["duration"],
                "detected_language": request.language,
                "features_summary": {k: v for k, v in features.items() if k != "duration" and k != "mfcc_mean"}
            }
        )
        
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        print(f"Internal Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error processing audio")

@app.websocket("/ws/live-monitor")
async def websocket_live_monitor(websocket: WebSocket):
    """
    WebSocket endpoint for real-time audio monitoring.
    Receives audio chunks and returns classification results.
    """
    await websocket.accept()
    try:
        while True:
            # Receive audio data from client
            data = await websocket.receive_text()
            message = json.loads(data)
            
            if message.get("type") == "audio_chunk":
                audio_base64 = message.get("audio")
                language = message.get("language", "English")
                
                try:
                    # Decode and analyze audio
                    y, sr = decode_audio(audio_base64)
                    features = extract_features(y, sr)
                    result = classifier.predict(features)
                    
                    # Send result back
                    await websocket.send_json({
                        "type": "detection_result",
                        "classification": result["classification"],
                        "confidence_score": result["confidence_score"],
                        "explanation": result["explanation"],
                        "timestamp": asyncio.get_event_loop().time()
                    })
                except Exception as e:
                    await websocket.send_json({
                        "type": "error",
                        "message": str(e)
                    })
            elif message.get("type") == "ping":
                await websocket.send_json({"type": "pong"})
                
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"WebSocket error: {e}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
