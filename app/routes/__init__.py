from flask import redirect
from app import app, api
from app.routes.auth import Login
from app.routes.blogs import Blogs, Blog
from app.routes.contact import Contact
from app.routes.projects import Projects, Project
from app.routes.skills import Skills, Skill


# auth endpoints
api.add_resource(Login, '/api/auth/login', endpoint='login')

# blogs endpoints
api.add_resource(Blog, '/api/blog/<int:id>', endpoint='blog')
api.add_resource(Blogs, '/api/blogs', endpoint='blogs')

# contact endpoints
api.add_resource(Contact, '/api/contact', endpoint='contact')

# projects endpoints
api.add_resource(Project, '/api/project/<int:id>', endpoint='project')
api.add_resource(Projects, '/api/projects', endpoint='projects')

# skills endpoints
api.add_resource(Skill, '/api/skill/<int:id>', endpoint='skill')
api.add_resource(Skills, '/api/skills', endpoint='skills')

# 404 handling


@app.errorhandler(404)
def forward(e):
    return redirect('https://www.netlify.com/')
