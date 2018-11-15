from flask import Flask, render_template
from utils import sensor
from flask_wtf import FlaskForm


class MyForm(FlaskForm):
    name = StringField('Desired Temperature')

temp_sensor = sensor.Sensor()

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def hello():
    form = MyForm()
    temp = temp_sensor.get_temp()
    
    if form.validate_on_submit():
        return redirect(render_template('landing.html'))
    
    return render_template('index.html', temperature=temp, form=form)

if __name__ == '__main__':
    app.run()