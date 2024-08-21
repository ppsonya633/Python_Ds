'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for concatenate two dictionary.


'''

def concatenate_dictionary(dict1,dict2,dict3):
    """
    Description:
        This program will take a 3 dictionary as a parameter and it will concate them
    Parameter:
        dict1,dict2,dict3:type:dict
    Return:
        dict"""
    
#  ** is used for unpacking the list
    result={**dict1,**dict2,**dict3}

    return result

def main():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}

    result=concatenate_dictionary(dic1,dic2,dic3)
    print(result)
main()

