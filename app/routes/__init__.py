from app import api
from app.routes.auth import Login
from app.routes.skills import Skills, Skill
from app.routes.projects import Projects

# auth endpoints
api.add_resource(Login, '/api/auth/login', endpoint='login')

# data endpoints
api.add_resource(Skill, '/api/skill/<int:id>', endpoint='skill')
api.add_resource(Skills, '/api/skills', endpoint='skills')
api.add_resource(Projects, '/api/projects', endpoint='projects')
