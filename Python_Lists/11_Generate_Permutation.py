'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for Generating Permutation.


'''
def permute(lst):
    """
    Description:
        This Program will take an list as a input and it will generate no of ways to arrange the list items
    Parameter:
        lst-it contains a list of the numbers
    Return:
        None
    """
    if len(lst) == 0:
        return [[]]
    
    result = []
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]
        for perm in permute(remaining):
            result.append([current] + perm)
    
    return result

def main():

  my_list = [1, 2, 3]
  perms = permute(my_list)

  for perm in perms:
    print(perm)

if __name__=="__main__":
   main()
