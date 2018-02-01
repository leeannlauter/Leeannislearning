spacing = ""


def lesson_2_1():
    space_print("Lesson 2_1")
    x = 1
    y = 2
    for i in range(0, 10):
        i = i + x + y
        space_print(i)
    space_print(x)
    space_print(y)


def lesson_2_2():
    space_print("Lesson 2_2")
    x = 0
    y = 0
    for i in range(0, 10):
        if i < 9:
            x = x + 1
        else:
            y = y + 1
    space_print(x)
    space_print(y)


def lesson_2_3():
    space_print("Lesson 2_3")
    global spacing
    spacing = "-------"
    lesson_2_1()
    lesson_2_2()


def space_print(string):
    print(spacing + str(string))


if __name__ == "__main__":
    lesson_2_3()
