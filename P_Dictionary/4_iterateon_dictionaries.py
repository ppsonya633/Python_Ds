'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for iteration on dictionary.


'''
def iterate_onDictionary(dictionary):
    """
    Description:
        This Program will take an dict as a input and it will run for loop on that
    Parameter:
        dict
    Return:
        None
    """
    for key,value in dictionary.items():
        print(f"{key} {value}")

def main():
    sample=dict(pratik=22,harshu=18,niru=16,samu=14)
    iterate_onDictionary(sample)

main()