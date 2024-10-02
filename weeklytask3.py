usr=[{'name': 'aslam', 'id': 101, 'email': 'asd@', 'phoneno': 12345, 'password': 'asd123','dress':[]}]
mwr=[{'dress': 'shirt', 'id': 10, 'stock': 15, 'size': 'xl', 'price': 3000},{'dress': 'Jeans', 'id': 11, 'stock': 20, 'size':'m', 'price': 3500},
{'dress': 'Tshirt', 'id': 12, 'stock': 30, 'size':'l', 'price': 2000}]
def register():
    if len(usr)==0:
        id=101
    else:
        id=usr[-1]['id']+1

    email=str(input('enter the email:'))
    f1=0
    for i in usr:
        if i['email']==email:                                                                           
            f1=1                                                                                   
            register()
    if f1==0:
        print('Registration')
        name=str(input('enter the name:'))
        phoneno=int(input('enter the phone no:'))
        password=str(input('enter the password:'))
        usr.append({'name':name,'id':id,'email':email,'phoneno':phoneno,'password':password,'dress':[]})
def login():
    username=input('enter the uname:')
    password=input('enter the password:')
    f=0
    if username=='admin' and password=='admin':
        f=1
    user=''
    for i in usr:
        if username==i['email'] and password==i['password']:
            f=2
            user=i
    return f,user
def add_dress():
    if len(mwr)==0:
        id=10
    else:
        id=mwr[-1]['id']+1

    f2=0
    for i in mwr:
        if i['id']==id:                                                                           
            f2=1                                                                                   
            add_dress()
    if f2==0:
        print('Dress details')
        name=str(input('enter the dress:'))
        stock=int(input('enter the stock:'))
        size=str(input('enter the size:'))
        price=int(input('enter the price:'))
        mwr.append({'name':name,'id':id,'stock':stock,'size':size,'price':price})                                   
def view_dress():                                                                                        
    for i in mwr:
        print(i)
def update_dress():
    id=int(input('enter the id:'))
    f2=0
    for i in mwr:
        if i['id']==id:                                                                           
            f2=1                                                                                   
        stock=int(input('enter the stock:'))
        price=int(input('enter the price:'))
        i['stock']=stock
        i['price']=price
    if f2==0:
        print('invalid')
def delete_dress():
    id=int(input('enter the id:'))
    f2=0
    for i in mwr:
        if i['id']==id:                                                                           
            f2=1
            mwr.remove(i)                                                                                   
    if f2==0:
        print('invalid')
def view_user():
    for i in usr:
        print('USER')
        print('name:',i['name'])
        print('id:',i['id'])
        print('email:',i['email'])
        print('phoneno:',i['phoneno'])
def view_profile(user):
    print(user)
def update_profile(user):
    name=str(input('enter the name:'))
    phoneno=int(input('enter the phone no:'))
    user['name']=name
    user['phoneno']=phoneno
def buy_dress(user):
    id=int(input('enter the id:'))
    f=0
    for i in mwr:
        if i['id']==id:
            f=1
            i['stock']-=1
            user['dress'].append(id)
            print('dress added')
    if f==0:
        print('invalid id')
def dress_in_hand(user):
    print(user['dress'])
while True:
    print('''
    1.register
    2.login
    3.exit''')
    choice=int(input('enter the choice:'))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                1.add dress
                2.view dress
                3.update dress
                4.delete dress
                5.view user
                6.logout''')
                sub_choice=int(input('enter the choice:'))
                if sub_choice==1:
                    add_dress()
                elif sub_choice==2:
                    view_dress()
                elif sub_choice==3:
                    update_dress()
                elif sub_choice==4:
                    delete_dress()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break

        elif f==2:
            while True:
                print('''
                1.view profile
                2.view dress
                3.update profile
                4.buy dress
                5.dress in hand
                6.logout''')
                sub_choice=int(input('enter the choice:'))
                if sub_choice==1:
                    view_profile(user)
                elif sub_choice==2:
                    view_dress()
                elif sub_choice==3:
                    update_profile(user)
                elif sub_choice==4:
                    buy_dress(user)
                elif sub_choice==5:
                    dress_in_hand(user)
                elif sub_choice==6:
                    break
        else:
            print('invalid username or password')
    elif choice==3:
        break
    else:
        print('invalid choice')