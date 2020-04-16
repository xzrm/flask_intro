from project import db

from project.models import BlogPost

db.create_all()

db.session.add(BlogPost("Title 1", "Description 1"))

db.session.add(BlogPost("From postgres", "Description 2"))

db.session.commit()