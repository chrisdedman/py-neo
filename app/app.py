from flask import Flask, request, render_template
from datetime import datetime, timedelta, date
from app.api import get_api_data, get_neo_info
from app.config import BASE_URL, API_KEY, port

app = Flask(__name__)

def fetch_data(start_date, end_date, context):
    """Fetch data from NASA API based on a given dates."""
    data = get_api_data(BASE_URL, API_KEY, start_date, end_date)

    if data:
        num_of_object     = data["element_count"]
        near_earth_object = data["near_earth_objects"]
        dates             = []

        for i in range(int(start_date[-2:]), int(end_date[-2:]) + 1):
            dates.append(start_date[:-2] + "%02d" % int(str(i)))

        neo_info = get_neo_info(near_earth_object, dates)

        return render_template(context, neo_info=neo_info, num_of_object=num_of_object, start_date=start_date, end_date=end_date)
    else:
        return "NEO Data Not Found!"

@app.route("/", methods=["GET", "POST"])
def index():
    """Get Near Earth Object Data."""
    start_date = date.today().strftime("%Y-%m-%d")
    end_date   = date.today().strftime("%Y-%m-%d")

    return fetch_data(start_date, end_date, "index.html")

@app.route("/neo-data", methods=["GET", "POST"])
def neo_data():
    """Get Near Earth Object Data."""
    # if request.method == "POST":
    #     start_date = request.form.get("start_date")
    #     end_date   = request.form.get("end_date")
    # else:
    #     end_date   = (datetime.today()).strftime("%Y-%m-%d")
    #     timelapse  = request.args.get("timelapse", default=0, type=int)
    #     start_date = (datetime.today() - timedelta(days=timelapse)
    #                   ).strftime("%Y-%m-%d")
    start_date = date.today().strftime("%Y-%m-%d")
    end_date   = date.today().strftime("%Y-%m-%d")

    return fetch_data(start_date, end_date, "neo_data.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
