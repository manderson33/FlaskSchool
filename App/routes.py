from crypt import methods
from datetime import datetime

from flask import render_template,redirect,url_for,flash,request
from app import app, db
from models import Task
import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/rectangle', methods=['GET', 'POST'])
def rectangle():
    form = forms.AddRectangle()
    area = None
    perimeter = None

    if request.method == 'POST':
        try:
            length = float(form.length.data)
            width = float(form.width.data)
            if form.area.data:  # If 'Calculate Area' was clicked
                area = length * width
            if form.perimeter.data:  # If 'Calculate Perimeter' was clicked
                perimeter = 2 * (length + width)
        except ValueError:
            pass  # Handle invalid input gracefully

    return render_template('rectangle.html', form=form, area=area, perimeter=perimeter)
@app.route('/form', methods=['GET', 'POST']) # get and post
def form():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, date=datetime.utcnow())  # Save task to DB
        db.session.add(new_task)
        db.session.commit()  # Commit changes

        flash('Task added successfully!', 'success')
        return redirect(url_for('form'))  # Redirect to avoid form resubmission

        # Retrieve tasks from the database to display on the page
    tasks = Task.query.all()
    return render_template('form.html', form=form, tasks=tasks)


'''
    if form.validate_on_submit():
        # prints in the console
        print('Form submitted', form.title.data)

        # prints on the page, handled in the about page with if statement
        return render_template('about.html', form=form, title=form.title.data)
    return render_template('about.html', form=form)
'''