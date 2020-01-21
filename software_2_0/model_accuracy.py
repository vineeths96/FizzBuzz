# Open file and calculate accuracy
def model_accuracy():
    test_output = open("test_output.txt", 'r')
    output = open("Software2.txt", 'r')

    correct_count = 0
    wrong_count = 0
    total_count = 0

    while (True):
        test_output_line = test_output.readline()
        output_line = output.readline()
        if test_output_line == '' or output_line == '':
            break
        elif test_output_line == output_line:
            correct_count += 1
            total_count += 1
        else:
            wrong_count += 1
            total_count += 1

    modl_accuracy = correct_count / total_count * 100

    print("The accuracy using Software 2.0 is ", modl_accuracy)
