import csv

# Project class
class MyProject:
  def __init__(self):
    self.prjtype = input("Enter project type: ")
    self.prjdes = input("Give project description: ")
    self.tasktype = input("Enter project task type: ")
    self.taskdes = input("Give task description")
    self.startdate = input("Enter start date: ")
    self.enddate = input("Enter end date: ")

  # Display project details method
  def dispPrj(self):
    print("Project: ", self.prjtype, "\n",
          "Project description: ", self.prjdes, "\n",
          "Task type: ", self.tasktype, "\n",
          "Start date: ", self.startdate, "\n",
          "End date: ", self.enddate, "\n")

# Program driver (main function)
def main():
  csvPath = ()                  # initialize csv file pathway
  prjList = []                  # initialize array of project classes

  csvPath = get_dir()          # get directory path to csv file
  prjList = prj_op()            # get list of projects
  write_csv(csvPath, prjList)   # save project data in csv

# Get directory path
def get_dir():
  # Initialize directory objects
  dir_op = 0
  fileName = ('testfile')
  filePath = ('C:/Users/micha/Desktop/')

  # Get directory operation
  dir_op = input("Create new file?: [0 = error, 1 = create, 2 = use existing]") # Get directory action
  dir_op = int(dir_op)
  # Create new file                          
  if(dir_op == 1):                            
    fileName = input("Name of file?: ")
    filePath = (str(filePath) + str(fileName))
    return filePath
  # Use existing file
  elif(dir_op == 2):
    # code needed here to navigate directory/select file path
    return
  # Error path - Invalid input
  else:
    raise Exception("Operation not valid")
    
# Get project details
def prj_op():
  # Initialize project objects
  prjqty = 0
  prjarray = []
  # code to be added to dynamically add multiple tasks to one project
  # taskqty = 0
  # taskarray = []  

  # Get qty of projects to add
  prjqty = input("how many projects would you like to add?: ")
  prjqty = int(prjqty)

  # Get project data for each project
  for i in range(prjqty):
    prjarray.append(MyProject())
  
  # Return project list
  return prjarray
  
# Write project data to csv
def write_csv(path, list):
    # code to be added to write a row in csv for each list element
    file = open(path,'w')       # Get path and create file
    writer = csv.writer(file)   # Get file operation
    data = list                 # Get project list
    writer.writerow(data[0])    # Write project list data to file
    file.close()                # Close file