from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

HTML_HOME = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>API Quishpe 1.0.5</title>
    <style>
        body {
            background: #f0f4f8;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 70px;
        }
        h1 {
            color: #333;
        }
        .card {
            background: white;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            width: 400px;
        }
        button {
            background: #007bff;
            border: none;
            padding: 10px 20px;
            color: white;
            font-size: 15px;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 15px;
        }
        button:hover {
            background: #0056cc;
        }
    </style>
</head>
<body>

<div class="card">
    <h1>API Flask - Quishpe</h1>
    <p>Versión <strong>1.0.5</strong></p>
    <p>Bienvenido a la API desplegada en CI/CD 🚀</p>

    <button onclick="window.location.href='/predict?text=hola'">
        Ir a /predict
    </button>
</div>

</body>
</html>
"""

@app.get("/")
def home():
    return render_template_string(HTML_HOME)

@app.get("/predict")
def predict_get():
    """
    Permite probar desde navegador:
    /predict?text=hola
    """
    text = request.args.get("text", "")
    return jsonify({
        "input": text,
        "score": len(text),
        "version": "1.0.5"
    })

@app.post("/predict")
def predict_post():
    """
    Para pruebas automáticas.
    """
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    return jsonify({
        "input": text,
        "score": len(text),
        "version": "1.0.5"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
