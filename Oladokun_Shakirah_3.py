# Author : Shakirah_Oladokun
# Assignment number & name: HW 3 Retirement Account
# Date : 2 June 2020
# Program Description: Problem Solving and programming


#Scenario:

Annual_Savings=float(input('What is your annual savings amount? '))
#Additional_Savings=Annual_Savings
while Annual_Savings < 0:
    print('Enter a positive value')
    Annual_Savings=float(input('What is your annual savings amount? '))
    if Annual_Savings == '':
        Annual_Savings = -1 # abrbitrary bad value
        print('Enter something valid')
    
    else:
        Annual_Savings == float(Annual_Savings)
        
        if (Annual_Savings < 0 or Annual_Savings <= -1 ):
            print('Enter a positive value')


Start_Year =int(input('What year do you want to start saving? '))
while Start_Year < 2020 or Start_Year > 2100:
    print('Enter a valid year')
    Start_Year =int(input('What year do you want to start saving? '))
    if Start_Year=='':
        print('Enter something valid')
    elif Start_Year < 2020 or Start_Year > 2100:
        print('Enter a valid year')
    else:
        Start_Year = int(Start_Year)

End_Year =int(input('What year do you want to stop saving? '))
while End_Year <= Start_Year or End_Year > 2100:
    print('Enter a valid year')
    End_Year =int(input('What year do you want to stop saving? '))
    if End_Year=='':
        print('Enter something valid')
    elif End_Year < 2020 or End_Year > 2100:
        print('Enter a valid year')
    else:
        Start_Year = int(Start_Year)

# Retire year can be greater or equal to end year
Retire_Year = int(input('What year did you retire? '))
while Retire_Year < 2020 or Retire_Year > 2100 or Retire_Year < End_Year:
    print('Enter a valid year')
    Retire_Year = int(input('What year did you retire? '))
    if Retire_Year=='':
        print('Enter something valid')
    elif Retire_Year < 2020 or Retire_Year > 2100 or Retire_Year < End_Year:
        print('Enter a valid year')
    else:
        Retire_Year = int(Retire_Year)
            
#Interest rate between 1% and 15% inclusive
Interest_rate=float(input('What is the interest rate? '))        
while Interest_rate < 1 or Interest_rate > 15:
    print('Enter a valid rate')
    Interest_rate=float(input('What is the interest rate? '))
    if Interest_rate < 1 or Interest_rate > 15:
        print('Enter a valid rate')
    else:
        Interest_rate= float(Interest_rate)
        
Total_Saving = Addition_Saving = Interest_Earned = 0

#print the table headings.
print()
print('Year \tAnnualSavings \tInterest     \tTotal')
print('-----------------------------------------------')

for Year in range(Start_Year, max(End_Year, Retire_Year)+1):
    #formular for the sum of the interest on the table 
    
    if Year <= End_Year:
        Additional_Savings=Annual_Savings
    else:
        Additional_Savings=0
    
    Interest_Earned = (Total_Saving + Additional_Savings)*(float(format(Interest_rate/100)))
   
    Total_Saving += Additional_Savings+Interest_Earned
   
    print(Year,'\t'+ format(Additional_Savings,',.0f')+' \t '\
          ,format(Interest_Earned,',.0f')+' \t ',format(Total_Saving,',.0f'))

