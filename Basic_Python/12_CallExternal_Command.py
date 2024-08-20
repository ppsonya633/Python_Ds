'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Call External Command



'''
import subprocess
def call_external_command(command):
   """ 
   Discription:
       This Function Will take any command as a argument and it will run using subprocess module
   Argument:
      command:(str)
   Return:
      None
   """
   try:
      result=subprocess.run(command,capture_output=True,text=True,check=True,shell=True)
      print("Command Output:")
      print(result.stdout)
   except subprocess.CalledProcessError as e:
      print(f"an error occured : {e}")

def main():
   command=input("Enter a command")
   call_external_command('dir')

main()