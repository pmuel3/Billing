#!/usr/bin/env python3

print("Minimum number of minutes needed for billing")
print()
print("How many units of Ther Ex?")
ex = int(input())
print("How many units of Neuro?")
neuro = int(input())
print("How many units of Gait?")
gait = int(input())
print("How many units of Manual?")
manual = int(input())
print("How many units of Ther Act?")
act = int(input())

#ther ex
ex_minimum = 0
if ex == 1:
	ex_minimum = 8
elif ex == 2:
	ex_minimum = 23
elif ex == 3:
	ex_minimum = 38
elif ex == 4:
	ex_minimum = 53

#Neuro
neuro_minimum = 0
if neuro == 1:
	neuro_minimum = 8
elif neuro == 2:
	neuro_minimum = 23
elif neuro == 3:
	neuro_minimum = 38
elif neuro == 4:
	neuro_minimum = 53

#Gait
gait_minimum = 0
if gait == 1:
	gait_minimum = 8
elif gait == 2:
	gait_minimum = 23
elif gait == 3:
	gait_minimum = 38
elif gait == 4:
	gait_minimum = 53


#manual
manual_minimum = 0
if manual == 1:
	manual_minimum = 8
elif manual == 2:
	manual_minimum = 23
elif manual == 3:
	manual_minimum = 38
elif manual == 4:
	manual_minimum = 53

#Ther Act
act_minimum = 0
if act == 1:
	act_minimum = 8
elif act == 2:
	act_minimum = 23
elif act == 3:
	act_minimum = 38
elif act == 4:
	act_minimum = 53

print()
print()


#total
min_total_time = (ex_minimum + neuro_minimum + gait_minimum + manual_minimum + act_minimum)
print("Minimum total time required:", min_total_time, "minutes")
print()
print()
