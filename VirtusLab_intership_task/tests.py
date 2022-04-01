import join
def test_1():
    # normal scenario inner
    command = 'join addresses.csv addresses2.csv id inner'
    join.run_test(command)


def test2():
    # default scenario left
    command = 'join addresses.csv addresses2.csv id'
    join.run_test(command)

def test3():
    # normal scenario right
    command = 'join addresses.csv addresses2.csv id right'
    join.run_test(command)

def test4():
    # unkown column
    command = 'join addresses.csv addresses2.csv uknown left'
    join.run_test(command)

def test5():
    # empty file
    command = 'join addresses.csv empty.csv id left'
    join.run_test(command)

def test6():
    # wrong file
    command = 'join addresses.csv wrong.csv id left'
    join.run_test(command)

def test7():
    # not csv file
    command = 'join addresses.txt addresses2.csv id left'
    join.run_test(command)

def test8():
    # wrong command
    command = 'join_to_file addresses.txt addresses2.csv id left'
    join.run_test(command)