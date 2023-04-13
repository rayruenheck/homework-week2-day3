def shoppingcart():
    shopping_list = {}
    while True:
        print(shopping_list)
        item = input('please enter an item to add to your shopping list or type "quit" to stop: \n')
        if item.lower() == 'quit':
            break
        value = input('how many of that item would you like?: \n')
        shopping_list[item] = value
    
        del_item = input('did you make a mistake? say the name of the last item you entered to delete: or press enter to continue. \n')
        if del_item == item:
            del shopping_list[item]
        else:
            continue
        
    for item, value in shopping_list.items():
        print(f'you currently have {value} {item}\'s in your shopping list \n' )


shoppingcart()


