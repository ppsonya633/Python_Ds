
'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for Creating Dictionary from string.


'''
def count_value(list):
    count=0
    for i in list:
        if i.get("success")==True:
            count+=1
    print(count)

def main():
    data= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False
















, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    count_value(data)
main()
