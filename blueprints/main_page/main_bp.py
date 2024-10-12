from flask import render_template, Blueprint
from blueprints.utils import create_context

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def index():
    context = create_context('Home Page')

    return render_template('authorization.html', **context)
