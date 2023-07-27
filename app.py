from flask import Flask, render_template, jsonify
from database import jobs_loaded_import

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = jobs_loaded_import()
  return render_template("index.html", jobs=jobs)


@app.route("/jobs")
def jobs():
  jobs = jobs_loaded_import()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
