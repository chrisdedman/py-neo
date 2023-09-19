"""Start the Flask app and get Near Earth Object Data."""
from flask import Flask, request, render_template
from datetime import datetime, timedelta
from api import get_api_data, get_neo_info
from config import BASE_URL, API_KEY, port

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def neo_data():
    """Get Near Earth Object Data."""
    if request.method == "POST":
        start_date = request.form.get("start_date")
        end_date   = request.form.get("end_date")
    else:
        end_date   = (datetime.today()).strftime("%Y-%m-%d")
        timelapse  = request.args.get("timelapse", default=0, type=int)
        start_date = (datetime.today() - timedelta(days=timelapse)).strftime("%Y-%m-%d")

    data = get_api_data(BASE_URL, API_KEY, start_date, end_date)

    if data:
        num_of_object     = data["element_count"]
        near_earth_object = data["near_earth_objects"]
        dates             = []

        for i in range(int(start_date[-2:]), int(end_date[-2:]) + 1):
            dates.append(start_date[:-2] + "%02d" % int(str(i)))

        neo_info = get_neo_info(near_earth_object, dates)

        return render_template("neo_data.html", neo_info=neo_info, num_of_object=num_of_object, start_date=start_date, end_date=end_date)

    else:
        return "NEO Data Not Found!"

if __name__ == "__main__":
    app.config.from_pyfile('settings.py')
    app.run(host="0.0.0.0", port=port, debug=True)
