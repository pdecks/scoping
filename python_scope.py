# playing around with python scoping
SOME_NUMBER = 10


def some_function():
    global SOME_NUMBER

    print "This is global SOME_NUMBER inside some_function: %s" % SOME_NUMBER

    SOME_NUMBER += 1

    print "This is global SOME_NUMBER updated inside some_function: %s" % SOME_NUMBER

    other_number = 20

    print "This is other_number defined inside some_function: %s" % other_number

    return None


def another_function():
    print "This should throw an exception:"
    try:
        print "This is other_number inside another_function: %s" % other_number

        other_number += 1

        print "This is other_number updated inside another function: %s" % other_number

    except UnboundLocalError:
        print "Yup! Welcome to the except block."
        print "other_number is not accessible in another_function because it is local to some_function"

    return None


if __name__ == "__main__":
    print "This is the global variable SOME_NUMBER, initially: %s" % SOME_NUMBER
    print "\n"

    print "Calling some_function():"
    some_function()
    print "\n"

    print "Calling another_function():"
    another_function()
