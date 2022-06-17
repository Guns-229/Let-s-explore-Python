from flask import (Flask, render_template, stream_with_context,
                   request, url_for, Response)
import json
import time
import _thread
status = {
    "upload": "Pending",
    "processing": "Pending",
    "upload_to_bucket": "Pending"

}

data_files = []
video_files = []
# Initialize the Flask application
app = Flask(__name__)


def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    return rv


@app.route("/running_status")
def running_status():
    def generate():
        data = json.dumps(status)
        yield "event: display\n"
        yield f'data: {data}\n\n'

    # return Response(generate(), mimetype='application/json')
    return Response(generate(), mimetype="text/event-stream")


@app.route("/display")
def generate_images():

    def generate():
        flg = False
        # data_files =
        while data_files:
            flg = True
            i = data_files.pop()
            # time.sleep(3)
            # yield f"data: '/static/imgs/{i}'\n\n"
            data = json.dumps({"file_name": f"/static/imgs/{i}", "time_stamp": "10: 02"})
            yield "event: display\n"
            yield f'data: {data}\n\n'

    # return Response(generate(), mimetype='application/json')
    return Response(generate(), mimetype="text/event-stream")


def process_video(video_file):
    print(f"processing video: {video_file}")x
    data = ["101720.jpg", "11640.jpg", "12760.jpg", "38040.jpg",
            "64200.jpg", "76080.jpg", "8160.jpg", "83160.jpg"]
    while data:
        time.sleep(5)
        data_files.insert(0, data.pop())


def process_queue():
    while True:
        while video_files:
            video_file = video_files.pop()
            process_video(video_file)


def schedule_task(file_name):
    status['upload'] = "Executing"
    video_files.insert(0, file_name)
    _thread.start_new_thread(process_queue, ())


@app.route('/show_images', methods=['GET', "POST"])
def show_images():
    if request.method == "POST":
        schedule_task("video.mp4")
        return "['ok']"
    return render_template('index.html')


# Run the app :)
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8020"),
        debug=True
    )
