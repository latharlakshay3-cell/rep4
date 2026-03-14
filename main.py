from flask import Flask, request, render_template_string
import subprocess
import os

app = Flask(__name__)

HTML = """
<h2>Network Test Panel</h2>
<form method="post">
IP: <input name="ip"><br><br>
Port: <input name="port"><br><br>
Time: <input name="time"><br><br>
Packet Size: <input name="size"><br><br>
Threads: <input name="threads"><br><br>
<button type="submit">Run</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ip = request.form["ip"]
        port = request.form["port"]
        duration = request.form["time"]
        size = request.form["size"]
        threads = request.form["threads"]

        if os.path.exists("mrx"):
            os.chmod("mrx", 0o755)

        subprocess.Popen(["./mrx", ip, port, duration, size, threads])

        return "Process started"

    return render_template_string(HTML)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
