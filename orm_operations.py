from ORM import Session, Teams
from sqlalchemy.exc import IntegrityError
import copy


def register_team(name, team, grades, max_grade):
    s = Session()
    s.add(Teams(team_name=name, team_members=team, grades=grades, max_grade=max_grade))
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
        tasks[task-1] = str(int(tasks[task-1]) - 1)
    else:
        tasks[task - 1] = str(point + int(tasks[task - 1]))
    s.query(Teams).filter(Teams.team_name == team_name).update({Teams.tasks: ' '.join(tasks)})
    s.commit()


def table(grades):
    s = Session()
    if grades == 89:
        t = s.query(Teams).filter(Teams.max_grade > 7).all()
    if grades == 67:
        t = s.query(Teams).filter(Teams.max_grade < 8).all()
    child_list = []
    result_list = []
    for u in t:
        child_list.clear()
        child_list.append(u.__dict__['team_name'])
        for i in u.__dict__['tasks'].split():
            child_list.append(i)
        result_list.append(copy.copy(child_list))
    return result_list
