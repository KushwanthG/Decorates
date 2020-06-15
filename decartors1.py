def Class(original):
    def wrap():
        print("some code before the execute")
        original()
        print('some code after code')
    return wrap()
def Class2():
    print("I want them")
Class(Class2)