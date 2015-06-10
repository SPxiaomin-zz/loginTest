from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.Integer)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        retunr False

    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)    
