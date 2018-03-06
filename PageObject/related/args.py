def fun_args1(args):
    print("args is %s"%args)

def fun_args2(args1,args2):
    print("args1 is %s args2 is %s"%(args1,args2))

def fun_args(*args):
    for value in args:
        print("args:",value)

fun_args1("python")

fun_args2("selenium","Hello")

fun_args("我","爱","python")