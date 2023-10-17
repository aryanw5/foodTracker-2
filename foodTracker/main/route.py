from flask import Blueprint, render_template, request, redirect, url_for

from foodtracker.models import Food, Log
from foodtracker.extensions import db

from datetime import datetime 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    logs = Log.query.order_by(Log.date.desc()).all()

    log_dates = []

    for log in logs:
        proteins = 0
        carbs = 0
        fats = 0
        calories = 0

        for food in log.foods:
            proteins += food.proteins
            carbs += food.carbs 
            fats += food.fats
            calories += food.calories

        log_dates.append({
            'log_date' : log,
            'proteins' : proteins,
            'carbs' : carbs,
            'fats' : fats,
            'calories' : calories
        })

    return render_template('index.html', log_dates=log_dates)

@main.route('/add')
def add():
     return render_template('add.html')

@main.route('/')
def view():
     return render_template('view.html')