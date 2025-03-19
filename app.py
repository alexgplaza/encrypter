from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Ejecutar el binario y capturar la salida
        result = subprocess.run(
            ['./bin/nom-proxy-encrypt'],
            input=text.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result.returncode != 0:
            return jsonify({"error": "Encryption failed", "details": result.stderr.decode()}), 500

        encrypted_text = result.stdout.decode().strip()
        return jsonify({"encrypted_text": encrypted_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
