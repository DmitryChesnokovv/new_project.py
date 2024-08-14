def test_function ():
    def inner_function():
        print("Я в области видимости функйции test_function")

    inner_function()

test_function()

inner_function() #Эта строка вызовет ошибку, так как inner_function не существует вне test_function