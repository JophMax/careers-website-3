from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "Data Scientist",
  'location': "Candyland",
  "salary": "120,000"
}, {
  'id': 2,
  'title': "Data Analyst",
  'location': "Canada",
  "salary": "12,000"
}, {
  'id': 3,
  'title': "Backend Engineer",
  'location': "Evansfield",
  "salary": "120,000,00"
}]


@app.route("/")
def hello_world():
  return render_template("index.html", jobs=JOBS)

@app.route("/jobs")
def jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
