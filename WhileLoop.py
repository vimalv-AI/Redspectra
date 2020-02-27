# Testing and learning git/github program

# Enter The Initialization Value
# like in C,C++ program for(i=0;i<=10;i++) 
# Here i=0 , is changed to user input
# like blowe input code Start_Value 
Start_Value = input("Initialization value : ")
# assume Start_Value as i
i = int(Start_Value)
# Then , also user choice to defined End Value
# like in C,C++ i<=10 instend instead of 10 we assume j 
End_Value = input("Condition Value : ")
# assume Start_Value as i
j = int(End_Value)
# just Print Loop
print("LOOP")
# Now, checking condition i is less then equal to j
while i <= j: 
# Ex : if user enter 1 to assume i , and 3 to assume j
     print(str(i) * i)
# i is equal less then equal to 1 is True : so,0 print : 1         (i+1)
     i = i + 1 
# i is equal less then equal to 2 is True : so,0 print : 22        (i+1)
                                           # ( because its multiple by i : (str(i)*i) ) 
# i is equal less then equal to 2 is True : so,0 print : 333       (i+1)
                                           # ( again its multiple by i : (str(i)*i) )                              
#  (i+1) Again checking i less then equal to 4 it will FALSE so, Terminated the Loop

    
    
