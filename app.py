
from flask import Flask, render_template,jsonify

app = Flask(__name__)


JOBS= [
{
     "id": 1,
     "title": "Data Analyst",
     "location": "Dar-es-Salaam, Tanzania",
     "salary": "Tshs. 2,000,000"
},

{
     "id":2,
     "title": "Cybersecurity",
     "location": "Dodoma, Tanzania",
     "salary": "Tshs. 4,000,000"
},

{
     "id":3,
     "title": "Frontend Engineer",
     "location": "Zanzibar, Tanzania",
     "salary": "Tshs. 1,500,000"
},

{
     "id":4,
     "title":"Backend Engineer",
     "location":"Mwanza, Tanzania",
     "salary": "Tshs. 6,000,000"
},
]


@app.route("/")
def home():
    #return "Hello, Flask!"
    return render_template("app_02.html",
                            jobs=JOBS,
                            company_name="Baraka")

@app.route("/api/jobs")
def list_jobs():
     return jsonify(JOBS)


if __name__ == "__main__":
#   app.run(debug=True)
     app.run(host="0.0.0.0", debug=True)

     
