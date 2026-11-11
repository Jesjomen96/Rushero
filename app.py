import os
from flask import Flask, request, jsonify, render_template_string
from google import genai

app = Flask(__name__)

# Inicializar el cliente de Gemini con tu clave de API privada
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Interfaz visual de Rushero
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rushero AI</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background: #0b0f19; color: #e2e8f0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; flex-direction: column; height: 100vh; }
        header { background: #111827; padding: 15px; text-align: center; font-size: 1.2rem; font-weight: bold; border-bottom: 1px solid #1f2937; color: #38bdf8; }
        #chat { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 12px; }
        .msg { padding: 12px 16px; border-radius: 12px; max-width: 85%; word-wrap: break-word; line-height: 1.4; }
        .user { background: #0284c7; color: white; align-self: flex-end; border-bottom-right-radius: 2px; }
        .bot { background: #1e293b; color: #f1f5f9; align-self: flex-start; border-bottom-left-radius: 2px; border: 1px solid #334155; }
        #input-area { display: flex; padding: 15px; background: #111827; border-top: 1px solid #1f2937; gap: 10px; }
        input { flex: 1; padding: 14px; border: 1px solid #374151; border-radius: 8px; background: #1f2937; color: white; font-size: 1rem; outline: none; }
        input:focus { border-color: #38bdf8; }
        button { padding: 14px 24px; background: #0284c7; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 1rem; }
        button:hover { background: #0369a1; }
    </style>
</head>
<body>
    <header>⚡ RUSHERO AI</header>
    <div id="chat">
        <div class="msg bot">Hola, soy Rushero. Tu asistente de inteligencia artificial personal. ¿En qué te ayudo hoy?</div>
    </div>
    <div id="input-area">
        <input type="text" id="prompt" placeholder="Escribe un mensaje a Rushero..." onkeypress="handleKey(event)" />
        <button onclick="send()">Enviar</button>
    </div>
    <script>
        function handleKey(e) { if(e.key === 'Enter') send(); }
        async function send() {
            let input = document.getElementById('prompt');
            let text = input
            
