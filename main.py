# flask aap

from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Eat Sleep Code Repeat</title>
  <style>
    body{display:flex;align-items:center;justify-content:center;height:100vh;margin:0;background:#0f172a;color:#e6f1ff;font-family:Inter,system-ui,sans-serif}
    .card{padding:2rem 3rem;border-radius:12px;box-shadow:0 8px 24px rgba(2,6,23,0.6);text-align:center}
    h1{font-size:2.25rem;margin:0 0 .5rem}
    p{margin:0;font-weight:600;opacity:.85}
  </style>
</head>
<body>
  <div class="card">
    <h1>Eat · Sleep · Code · Repeat</h1>
    <p>Built with Flask — lightweight and fast.</p>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
