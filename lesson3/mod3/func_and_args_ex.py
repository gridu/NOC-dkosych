#!/usr/bin/python3

def func1(a1, a2):
    print("func1: " + str(a1) + ", " + str(a2))


def func2(a1, a2, a3="hello", a4=42):
    print("func2: " + str(a1) + ", " + str(a2) + ", " + str(a3) + ", " + str(a4))


def func3(a1, a2, *, a3="hello", a4=42):
    print("func3: " + str(a1) + ", " + str(a2) + ", " + str(a3) + ", " + str(a4))


func1(33, 44)
# func1(33)
# func1(33,44,55)
func2(33, 44, "goodbye", 99)
func2(33, 44, "goodbye")
func2(33, 44)
func2(44, 55, a4=99)
func3(66, 77)
# func3(66,77,"goodbye")
func3(66, 77, a3="goodbye")
func3(66, 77, a4=99, a3="goodbye")
