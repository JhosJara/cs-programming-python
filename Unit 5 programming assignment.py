import math

def my_sqrt(a):
    x = a/2
    while True:
        approx_sqrt = (x + a/x)/2
        if approx_sqrt == x:
            return approx_sqrt
            break
        x = approx_sqrt
    print(list_a(range(1,25)))


def test_sqrt(list_a):
    # We are formulating a table to compute the outcomes
    line1a = "a"
    line1b = "my_sqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"

    space1 = "| "
    space2 = "| "
    space3 = "| "

    line2a = "---"
    line2b = "---------"
    line2c = "---------"
    line2d = "----"

    print(line1a, space1, line1b, space2, line1c, space3, line1d)
    print(line2a, space1, line2b, space2, line2c, space3, line2d)

    for a in list_a:
        col1= float(a)
        col2= my_sqrt(a)
        col3= math.sqrt(a)
        col4 = abs(my_sqrt(a) - math.sqrt(a))
        print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)
test_sqrt(range(1,25))