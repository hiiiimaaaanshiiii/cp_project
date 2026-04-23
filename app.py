import os #here i am providing access to os
from flask import Flask #here i imported flask 
from flask_sqlalchemy import SQLAlchemy #db for user login n stuff
from flask_wtf import CSRFProtect
from extensions import db, csrf


def create_app(): #yahape i created a function
    app = Flask(__name__) #idhar i defined an object aur __name__ is pre-existing variable in python
    #Configurations:

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "HIMANSHI") #yahape i used dictionaries, and like secret key is my key and os.getenv, fetches value for my key else by default value is himanshi
    
    # yahape i am giving address to my database (absolute path safer hota hai)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.getcwd(), "users.db")
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #yahape i do error handling i.e. dealing w errors


    #INTIALISING EXTENSIONS
    db.init_app(app) #connecting db
    csrf.init_app(app) #adding security layer


    #REGISTERING ROUTES
    from routes import main #here i imported blueprint
    app.register_blueprint(main)


    #CREATING DATABASE
    with app.app_context():
        db.create_all() #yahape it creates db if it doesn't exist


    #error handling
    @app.errorhandler(404)
    def not_found(e):
        return {"error": "Page not found"}, 404

    @app.errorhandler(500)
    def server_error(e):
        return {"error": "Internal server error"}, 500


    return app


# yahape i Create app instance
app = create_app()


# yaha i Run server
if __name__ == "__main__":
    app.run(debug=True)