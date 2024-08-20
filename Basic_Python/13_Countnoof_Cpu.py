'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Count no of cpu cycles.

'''
import os
import multiprocessing

def get_cpu_count():

    """
    Description:
        This Function will Print the cpu counts
    Parameter:
        None
    Return:
        None
    """
    cpucount=os.cpu_count()
    print(cpucount)
    cpucountm=multiprocessing.cpu_count()
    print(cpucountm)

def main():
    get_cpu_count()

main()