from app import api
from app.routes.auth import Login
from app.routes.skills import Skills, Skill
from app.routes.projects import Projects, Project

# auth endpoints
api.add_resource(Login, '/api/auth/login', endpoint='login')

# skills endpoints
api.add_resource(Skill, '/api/skill/<int:id>', endpoint='skill')
api.add_resource(Skills, '/api/skills', endpoint='skills')

# projects endpoints
api.add_resource(Project, '/api/project/<int:id>', endpoint='project')
api.add_resource(Projects, '/api/projects', endpoint='projects')
