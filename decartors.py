def hello(name='john'):
    print("The hello() funtion has been execuited")
    
    def greet():
        print('\t This is the greet() fun inside function')
    
    def welcome():
        print('\t This is the welcome() fun inside function')
    print('i am going to return a func')
    if name=='jon':
        print(greet())
    else:
        return welcome()
hello()