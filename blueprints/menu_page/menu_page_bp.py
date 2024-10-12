from flask import Blueprint, render_template
from blueprints.utils import create_context

menu_page_bp = Blueprint('menu_page_bp', __name__,
                         template_folder='templates',
                         static_folder='static')


@menu_page_bp.route('/menu')
def menu_page():
    context = create_context('Menu')

    return render_template('menu.html', **context)
