from flask import Flask

app = Flask(__name__)


@app.route("/signup", methods=["POST"])
def signup():
    @app.errorhandler(404)
    def not_found(error):
        return {"message": "Not Found"}, 404

    @app.errorhandler(500)
    def server_error(error):
        return {"message": "Internal Server Error"}, 500


@app.route("/kanban", methods=["GET"])
def get_kanban():
    # Code to fetch and return the Kanban board goes here
    return {"message": "Kanban board"}, 200
