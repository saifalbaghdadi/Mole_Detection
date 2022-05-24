from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "saifibrtybvibsidsaif"
    app.config["MAX_CONTENT_LENGTH"] = (16 * 1024 * 1024)
    
    from project.views import views
    # from predict import create_model
    app.register_blueprint(views, url_prefix='/')
    
    return app