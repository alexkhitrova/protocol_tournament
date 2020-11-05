from ORM import Session, Teams
from sqlalchemy.exc import IntegrityError


def register_team(name, team, grade, max_grade):
    s = Session()
    s.add(Teams(team_name=name, team_members=team, grades=grade, max_grade=max_grade))
    try:
        s.commit()
        return True
    except IntegrityError:
        return False


def give_point(team_name, task, point):
    s = Session()
    team = s.query(Teams).filter(Teams.team_name == team_name).first()
    tasks = team.tasks
    tasks = tasks.split()
    if int(tasks[task - 1]) > 0:
        return 0
    if point == -1:
        tasks[task - 1] = str(int(tasks[task-1]) - 1)
    else:
        tasks[task - 1] = str(point + int(tasks[task - 1]))
    s.query(Teams).filter(Teams.team_name == team_name).update({Teams.tasks: ' '.join(tasks)})
    s.commit()