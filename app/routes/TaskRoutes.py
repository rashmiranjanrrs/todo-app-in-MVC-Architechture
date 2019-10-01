from app.controller.TaskController import TaskController
from todo.app.controller import UserController
from flask import  Blueprint

taskroutes = Blueprint("taskroutes", __name__)

@taskroutes.route('/addtask', methods=['POST'])
def addtask():
    return TaskController.addtask()

@taskroutes.route('/taskdone', methods=['GET'])
def markdone():
    return TaskController.markdone()

@taskroutes.route('/deletetask', methods=['POST'])
def deletetask():
    return TaskController.deletetask()

@taskroutes.route('/showtasks', methods=['GET'])
def alltasks():
    return TaskController.alltasks()



