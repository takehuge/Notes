# To switch between cases

def one():
    return "January"
def two():
    return "February"

def mthconvertor(argument):
    switcher = {
        1: one,
        2: two
    }
    func = switcher.get(argument, lambda:"Invalid value")
    return func()

print(mthconvertor(1))
print(mthconvertor(2))
print(mthconvertor(3))