from flask import Flask, render_template, url_for, redirect
import itsdangerous
import markupsafe
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import validators, StringField, SubmitField, URLField, IntegerField, TimeField
from wtforms.validators import DataRequired, ValidationError
import json, csv, datetime


def flask_it():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdf1319'
    Bootstrap(app)
    return app


app = flask_it()

class MyForm(FlaskForm):
    cafe_name = StringField(label='*Cafe Name', validators=[validators.DataRequired(), validators.input_required()], render_kw={'placeholder': 'Enter Cafe Name'})
    cafe_location = URLField(label="Cafe Location(leave it if you don't know)", default='https://ca.fe', validators=[validators.DataRequired(), validators.URL(message="Invalid URL")], render_kw={'placeholder': 'Enter Cafe Location'})
    open_time = TimeField(label="*Open Time", validators=[validators.DataRequired()], render_kw={'placeholder': 'Enter Open Time'})
    close_time = TimeField(label="*Close Time", validators=[validators.DataRequired()], render_kw={'placeholder': 'Enter Close TIme'})
    coffee_rate = IntegerField(label="*Coffee Rate", validators=[validators.DataRequired(), validators.NumberRange(min=1, max=5, message='rate from 1 to 5')], render_kw={'placeholder': 'RATE FROM 1 to 5'})
    wifi_rate = IntegerField(label="*WIFI Rate", validators=[validators.DataRequired(), validators.NumberRange(min=1, max=5, message='rate from 1 to 5')], render_kw={'placeholder': 'RATE FROM 1 to 5'})
    power_rate = IntegerField(label="*Power Rate", validators=[validators.DataRequired(), validators.NumberRange(min=1, max=5, message='rate from 1 to 5')], render_kw={'placeholder': 'RATE FROM 1 to 5'})
    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    css_url = url_for('static', filename='css/styles.css')
    return render_template("index.html", css_url=css_url)


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = MyForm()
    to_append = []
    if form.validate_on_submit():
        to_append.append(form.cafe_name.data)
        to_append.append(f"https://map.naver.com/p/search/{form.cafe_name.data}")
        # strptime = string to time data / strftime = time data to string
        formatted_open_time = form.open_time.data.strftime("%H:%M")
        formatted_close_time = form.close_time.data.strftime("%H:%M")
        to_append.append(formatted_open_time)
        to_append.append(formatted_close_time)
        to_append.append(form.coffee_rate.data)
        to_append.append(form.wifi_rate.data)
        to_append.append(form.power_rate.data)
        with open('cafe-data.csv', 'a') as file:
            csv.writer(file).writerow(to_append)
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True, port=8080)

