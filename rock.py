import random
while True:
    choice = input("what is your choice ")
    choice = choice.lower()
    choices = ['rock','paper','scissors']
    computer_choice = random.choice(choices)
    print(computer_choice)

    choice_dict = {'rock':0,'paper':1,'scissors':2}
    choice_index = choice_dict.get(choice,3)
    computer_index = choice_dict.get(computer_choice)
    print(choice_index,computer_index)

    result_matrix = [[0,2,1]
                    ,[1,0,2],
                    [2,1,0],
                    [3,3,3]]
    # print(result_matrix)
    result_index = result_matrix[choice_index][computer_index]
    print(result_index)
    result_messages = ['it is a tie','You win','sorry you lose','invalid choice try again']
    result = result_messages[result_index]
    print(result)
    print()