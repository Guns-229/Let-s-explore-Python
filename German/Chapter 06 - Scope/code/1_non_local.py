### Non Locals: gets the nearest available variables 
# as `a` we are getting from inner and `b` we are getting from `outer`
d = 10

def outer():
    a = 0
    b = 1

    def inner():
        """
            a: 20   `local` 
            b: 1    `non local` 
        """
        a = 20

        def innermost():
            nonlocal a
            nonlocal b
            print(a, b)
            a = 200
            b = 11111
            
        print("Executing innermost")
        innermost()
        print("back in inner")
        print(a, b)
        print("done executing")
        
    print(a, b)
    inner()
    print(a, b)

try:
    outer()
except Exception as e:
    print(e)