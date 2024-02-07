#!/usr/bin/env python3

print('How many units of Ionto?')

ionto = int(input())

print('How many units of ultrasound?')

ultrasound = int(input())

print('How many units of Ther Ex?')

ther_ex = int(input())

print('How many units of Neuro?')

neuro = int(input())

print('How many units of Gait?')

gait = int(input())

print('How many units of Manual?')

manual = int(input())

print('How many units of Ther Act?')

ther_act = int(input())


def unit_func(num):
    if num == 1:
        minutes = 8
    elif num > 1:
        minutes = (15 * (num -1)) + 8
    elif num == 0:
        minutes = 0
    return minutes

ionto_minutes = unit_func(ionto)

ultrasound_minutes = unit_func(ultrasound)

ther_ex_minutes = unit_func(ther_ex)

neuro_minutes = unit_func(neuro)

gait_minutes = unit_func(gait)

manual_minutes = unit_func(manual)

ther_act_minutes = unit_func(ther_act)


total_minutes = ionto_minutes + ultrasound_minutes + ther_ex_minutes + neuro_minutes + gait_minutes + manual_minutes + ther_act_minutes

print()
print()
print("Total minimum time required for desired units:")
print()
print(total_minutes)
