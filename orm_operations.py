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
        if int(tasks[task-1]) < 0:
            tasks[task-1] = "0"
    s.query(Teams).filter(Teams.team_name == team_name).update({Teams.tasks: ' '.join(tasks)})
    s.commit()


def table(grades):
    s = Session()
    t = s.query(Teams).filter(Teams.max_grade == grades).all()
    child_list = []
    result_list = []
    for u in t:
        child_list.clear()
        child_list.append(u.__dict__['team_name'])
        for i in u.__dict__['tasks'].split():
            child_list.append(i)
        if u.__dict__['bonus_task']!=-1:
            child_list.append(u.__dict__['bonus_task'])
        result_list.append(copy.copy(child_list))
    return result_list

def junior_count(grade):
    s = Session()
    if grade == 6 or grade == 8:
        return 2
    return s.query(Teams).filter(Teams.max_grade == grade).count()


def give_bonus_point(team_name, point):
    s = Session()
    team = s.query(Teams).filter(Teams.team_name == team_name).first()
    task = team.bonus_task
    if task == -1:
        task = 0
    task = task+point
    s.query(Teams).filter(Teams.team_name == team_name).update({Teams.bonus_task: task})
    s.commit()


def get_bonus(team_name):
    s = Session()
    team = s.query(Teams).filter(Teams.team_name == team_name).first()
    return team.bonus_task



