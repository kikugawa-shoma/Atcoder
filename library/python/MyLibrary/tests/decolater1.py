def show_args(func):
    def show(arg):
        print("arg", arg)
        print(func(arg))
    return show

@show_args
def my_sum(args):
    return sum(args)

my_sum([1, 2])


