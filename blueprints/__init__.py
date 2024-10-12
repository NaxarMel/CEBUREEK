from blueprints.authorization.authorization_bp import authorization_bp
from blueprints.main_page.main_bp import main_bp
from blueprints.menu_page.menu_page_bp import menu_page_bp


def register_blueprint(app):
    app.register_blueprint(authorization_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(menu_page_bp)
