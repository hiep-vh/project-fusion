# Import các routes
from app.routes.test import test
from app.routes.v1.projects import project_bp
from app.routes.v1.master import bp as master_bp
from app.routes.v1.appendix import appendix_bp
from app.routes.v1.resources import resource_bp

# Hàm để đăng ký blueprint chính với ứng dụng Flask
def init_routes(app):
    app.register_blueprint(test, url_prefix='/api')

    # v1/masters
    app.register_blueprint(master_bp, url_prefix='/api')  

    # v1/appendix
    app.register_blueprint(appendix_bp, url_prefix='/api')

    # v1/resources
    app.register_blueprint(resource_bp, url_prefix='/api')

    # v1/project
    app.register_blueprint(project_bp, url_prefix='/api')  
    