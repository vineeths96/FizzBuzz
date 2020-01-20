def fizzbuzz(fname):
    try:
        input_file = open(fname, 'r')
    except:
        print("Input file does not exist. Please try again.\n")
        exit()

    output_file = open("Software1.txt", 'w')

    for line in input_file:
        num = int(line)
        if num%15 == 0:
            output_file.write("fizzbuzz\n")
        elif num%3 == 0:
            output_file.write("fizz\n")
        elif num%5 == 0:
            output_file.write("buzz\n")
        else:
            output_file.write(str(num) + "\n")

    input_file.close()
    output_file.close()
