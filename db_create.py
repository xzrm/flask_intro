from app import db

from models import BlogPost

db.create_all()

db.session.add(BlogPost("Title 1", "Description 1"))
# db.session.add(BlogPost("Title 2", "Description 2"))

db.session.commit()