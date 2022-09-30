import csv

class MyProject:
  def __init__(self):
    self.prjtype = input("Enter project type: ")
    self.prjdes = input("Give project description: ")
    self.tasktype = input("Enter project task type: ")
    self.taskdes = input("Give task description")
    self.startdate = input("Enter start date: ")
    self.enddate = input("Enter end date: ")

  def dispPrj(self):
    print("Project: ", self.prjtype, "\n",
          "Project description: ", self.prjdes, "\n",
          "Task type: ", self.tasktype, "\n",
          "Start date: ", self.startdate, "\n",
          "End date: ", self.enddate, "\n")


def main():
  # initialized variables
  csvPath = ()
  prjList = []

  csvPath = dir_init()
  prjList = prj_op()
  write_csv(csvPath, prjList)

def dir_init():
  # Initialize directory objects
  dir_op = 0
  fileName = ('testfile')
  filePath = ('C:/Users/micha/Desktop/')

  # Get directory operation
  dir_op = input("Create new file?: [0 = error, 1 = create, 2 = use existing]")
  dir_op = int(dir_op)
  if(dir_op == 1):
    fileName = input("Name of file?: ")
    filePath = (str(filePath) + str(fileName))
    return filePath
  elif(dir_op == 2):
    # code needed here to navigate directory/select file path
    return
  else:
    raise Exception("Operation not valid")
    

def prj_op():
  prjqty = 0
  prjarray = []
  # code to be added to dynamically add multiple tasks to one project
  # taskqty = 0
  # taskarray = []  

  prjqty = input("how many projects would you like to add?: ")
  prjqty = int(prjqty)

  for i in range(prjqty):
    prjarray.append(MyProject())
  
  return prjarray
  
def write_csv(path, list):
    # code to be added to write a row in csv for each list element
    file = open(path)
    writer = csv.writer(file)
    data = list
    writer.writerow(data[0])
    file.close()