from app import api
from app.routes.auth import Login
from app.routes.projects import Projects

# auth endpoints
api.add_resource(Login, '/api/auth/login', endpoint='login')

# projects endpoints
api.add_resource(Projects, '/api/projects', endpoint='projects')