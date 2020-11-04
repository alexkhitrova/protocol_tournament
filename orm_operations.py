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


def give_point(team_name, task, point):
    s = Session()
    db = s.query(Teams).filter(Teams.team_name == team_name).first()
    if task==1:
        s.query(Teams).filter(Teams.team_name == team_name).update({Teams.t1: point})
    if task==2:
        s.query(Teams).filter(Teams.team_name == team_name).update({Teams.t2: point})
    if task==3:
        s.query(Teams).filter(Teams.team_name == team_name).update({Teams.t3: point})
    s.commit()
    return s.query(Teams).all()


#register_team('bestteam', 'andrew', '7')
# print(get_table())
give_point("bestteam", 1, "4")
give_point("bestteam", 3, "5")
give_point("bestteam", 2, "-1")