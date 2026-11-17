
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Kubernetes Project</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Welcome to My CI/CD Project!</h1>
            <h2>Docker + Jenkins + Kubernetes</h2>
            <p>Application deployed successfully!</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "CI/CD Kubernetes Project"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
