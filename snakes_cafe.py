lst = ["Wings","Cookies","Spring rolls","Salmon","Steak","Meat tornado","A literal garden","Ice cream","Cake","Pie","Coffee","Tea","Unicorn tears"]

def lab():
    print(f'**************************************\n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.        **\n**\n** To quit at any time, type "quit" **\n**************************************\n\nAppetizers\n----------\n{lst[0]}\n{lst[1]}\n{lst[2]}\n\nEntrees\n-------\n{lst[3]}\n{lst[4]}\n{lst[5]}\nA {lst[6]}\n\nDesserts\n--------\n{lst[7]}\n{lst[8]}\n  {lst[9]}\n\nDrinks\n------\n{lst[10]}\n{lst[11]}\n{lst[12]}\n\n***********************************\n** What would you like to   order? **\n***********************************')

    order = []
    a = input().capitalize()
    #b = a.capitalize()
    #print(b)
    while a != 'Quit':
        if a in lst:
            order.append(a)
            print(f'** {order.count(a)} order of {a} have been added to your meal **')
        else:
            print('please order one of the stuff on the menu!!')
        a = input().capitalize()
        #b = a.capitalize()
        #print(b)
    print('thanks for your visit')
if __name__ == '__main__':
    lab()
