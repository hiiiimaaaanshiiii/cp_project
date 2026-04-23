from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


#SIGNUP FORM

class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=20)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=4, max=20)
        ]
    )

    submit = SubmitField("Sign Up")


#LOGIN FORM

class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField("Login")


#CRIME REPORT FORM

class CrimeReportForm(FlaskForm):
    location = StringField(
        "Location",
        validators=[
            DataRequired(),
            Length(min=3, max=100)
        ]
    )

    crime_type = SelectField(
        "Crime Type",
        choices=[
            ("Harassment", "Harassment"),
            ("Stalking", "Stalking"),
            ("Assault", "Assault"),
            ("Domestic Violence", "Domestic Violence")
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField("Report Crime")