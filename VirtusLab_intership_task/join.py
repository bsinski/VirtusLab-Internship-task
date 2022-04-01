def join(path1, path2, column, join_type):
    records1 = []
    records2 = []
    try:
        with open(path1, 'r') as f:
            for line in f:
                records1.append(line.rstrip('\n').split(','))
        with open(path2, 'r') as f:
            for line in f:
                records2.append(line.rstrip('\n').split(','))
    except MemoryError:
        print('cvs file to big. Try again.')
        run()
    except FileNotFoundError:
        print('There is no such a file. Try again.')
        run()
    if len(records1) == 0:
        print('There are no records in first table. Try again.')
        run()
    if len(records2) == 0:
        print('There are no records in second table. Try again.')
        run()
    labels1 = records1[0]
    labels2 = records2[0]
    records1 = records1[1:len(records1)]
    records2 = records2[1:len(records2)]
    try:
        index1 = labels1.index(column)
        index2 = labels2.index(column)
    except ValueError:
        print('There is no such column in given csv files. Try again.')
        run()
    labels2.pop(index2)
    new = [labels1 + labels2]
    if join_type == 'inner':
        for r1 in records1:
            for r2 in records2:
                if r1[index1] == r2[index2]:
                    r2.pop(index2)
                    new.append(r1 + r2)
    if join_type == 'left':
        for r1 in records1:
            is_in = False
            for r2 in records2:
                if r1[index1] == r2[index2]:
                    r2.pop(index2)
                    new.append(r1 + r2)
                    is_in = True
            if is_in == False:
                new.append(r1 + ["nan"] * (len(r2) - 1))
    if join_type == 'right':
        for r1 in records2:
            is_in = False
            for r2 in records1:
                if r1[index1] == r2[index2]:
                    r2.pop(index2)
                    new.append(r1 + r2)
                    is_in = True
            if is_in == False:
                new.append(r1 + ["nan"] * (len(r2) - 1))
    return new

def read_input():
    print('Write the command: ')
    words = input().split()
    return words

def check_input(words):
    # reading the input from the user
    if len(words) != 4 and len(words) != 5:
        print('Wrong command, wrong number of input arguments. Try again.')
        run()
    if words[0] != 'join':
        print('Wrong command. Try again.')
        run()
    if '.csv' not in words[1] or '.csv' not in words[2]:
        print('File is not a csv file. Try again.')
        run()
    if len(words) == 5:
        if words[4] != 'left' and words[4] != 'right' and words[4] != 'inner':
            print('Wrong join type. Try again.')
            run()

def write_output(results):
    for lines in results:
        print(','.join(lines))

def run():
    # main function used to wrapping evertyhing in one method
    command = read_input()
    check_input(command)
    if len(command) == 5:
        result = join(command[1], command[2], command[3], command[4])
    else:
        result = join(command[1], command[2], command[3], 'left')
    write_output(result)
def run_test(comm):
    command = comm.split()
    check_input(command)
    if len(command) == 5:
        result = join(command[1], command[2], command[3], command[4])
    else:
        result = join(command[1], command[2], command[3], 'left')
    write_output(result)