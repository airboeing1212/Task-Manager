import sys
import os
import json
import datetime
import time


argv = sys.argv



json_name = "file.json" #change your file name if you want to

current_dir = os.getcwd()
list_dir = os.listdir(current_dir)

data = {'task_manager' : []}
temp_data =  {
            'id' : 0,
            'description' : None,
            'status' : None,
            'createdAt' : None, 
            'updatedAt' : None,
        }


def add(arg,read):

    try:
        if arg[3] == 'status' :
            for i in['todo', 'done', 'in-progress']:
                if i == arg[4]:
                    status = arg[4]
                else:
                    status = 'todo'

            print('you gave a invalid status')
            print('status is todo')              
        else:
            status = 'todo'
    except:
        status = 'todo'
    num = max(task['id'] for task in read['task_manager']) if read['task_manager'] else 0 

    temp_data['id'] = num + 1
    temp_data['description'] = arg[2]
    temp_data['status'] = status
    temp_data['createdAt'] = datetime.datetime.now().isoformat()
    temp_data['updatedAt'] = None

    return temp_data


def update(arg, read, mark=None):

    ıd = arg[2]
    red = read
    red['task_manager'][int(ıd) - 1]['description'] = arg[3]

    red['task_manager'][int(ıd) - 1]['updatedAt'] = datetime.datetime.now().isoformat()

    return red
    
def delete(arg, read):
    ıd = int(arg[2])

    read['task_manager'] = [task for task in read['task_manager'] if task['id'] != ıd]
    return read

def mark(arg, read):
    
    new = str(arg[1]).split('-',1)[1]
    ıd = int(arg[2])
    read['task_manager'][ıd - 1]['status'] = new

    return read

def list(arg, read):

    
    if len(arg) == 2:
    

        for i in read['task_manager']:
            print('-----------')
            print(f'your {i['id']}. task')
            print(i)
            print('-----------')

    elif arg[2] == 'done':
        for i in read['task_manager']:
            if i['status'] == 'done':
                print('-------------')
                print('you have completed this tasks')
                print(i)
                print('-------------')
    elif arg[2] == 'todo':
        for i in read['task_manager']:
            if i['status'] == 'todo':
                print('-------------')
                print(' you have to do these')
                print(i)            
    elif arg[2] == 'in-progress':
        for i in read['task_manager']:
            if i['status'] == 'in-progress':
                print('--------------')
                print('IN PROGRESS')
                print(i)
    else:
        print('please enter a valid status')
        print('(todo), (done), (in-progress)')

if json_name not in list_dir:
    with open(json_name, "w") as f:
        json.dump(data, f, indent=4)
    with open(json_name, 'r') as f:
        red_data = json.load(f)

else:
    print("json file found")
    with open(json_name, 'r')as f:
        red_data = json.load(f)



def task_track(arg):

    try:
        if arg[1] == "add":
            
            red_data['task_manager'].append(add(arg,red_data))
            return red_data
            
        elif arg[1] == "update":
            return update(arg, red_data)

        elif arg[1] == "delete":
            return delete(arg, red_data)
        
        elif str(arg[1]).split('-')[0] == 'mark':
            return mark(arg, red_data)
        
        elif arg[1] == 'list':
            list(arg, red_data)
            return red_data
        else:
            print('please enter a valid action')
            return red_data
    except Exception as E:
        print('plese enter the arguments correct')
        return red_data



new_data = task_track(argv)

with open(json_name, 'w')as f:
    json.dump(new_data, f, indent=4)

