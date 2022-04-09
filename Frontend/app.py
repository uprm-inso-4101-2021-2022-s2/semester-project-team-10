from flask import Flask, render_template, url_for

app = Flask(__name__)

tasks = [
    {
        'name': 'Rigoberto Idalgo',
        'job_title': 'Cashier',
        'assigned_task':'Store Openning',
        'date':'March 25, 2022',
        'time':'7:00am - 1:00pm'
    },
    {
        'name': 'Bob Ross',
        'job_title': 'Manager',
        'assigned_task':'Management',
        'date':'March 24, 2022',
        'time':'9:00am - 5:00pm'
    }

]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)