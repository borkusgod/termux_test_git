# classes file for fman
# import from functions file to keep organized
from functions import *
from text_vars import *


class ProfTester:
    def __init__(self, first):
        self.first = first

    def class_meth_call(self):
        return self.first * 2


class ProjectManager:
    def __init__(self,
                 project_name,
                 folder_name):
        self.project_name = project_name
        self.folder_name = folder_name


