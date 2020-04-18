from flask import render_template, Blueprint
from flask_split import ab_test, finished

ab_test_bp = Blueprint('ab_test_bp', __name__)

@ab_test_bp.route('/')
def index():
    return render_template('index.html')

@ab_test_bp.route('/primary_button_click')
def check_primary_btn_click():
    finished('primary_btn_text')
    return render_template('thanks.html')

@ab_test_bp.route('/secondary_button_click')
def check_secondary_btn_click():
    finished('secondary_btn_text')
    return render_template('thanks.html')

@ab_test_bp.route('/ab_test_full_page')
def check_full_page():
    return render_template(ab_test('page_checker','page1.html', 'page2.html'))