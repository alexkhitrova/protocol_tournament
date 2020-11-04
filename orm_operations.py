from ORM import Session,Teams
from sqlalchemy.exc import IntegrityError

def register_team(name, team, grade):
    s = Session()
    s.add(Teams(team_name=name, team_members=team, grade=grade))
    try:
        s.commit()
        return True
    except IntegrityError:
        return False

def get_table():
    s = Session()
    return s.query(Teams).all()