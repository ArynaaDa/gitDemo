# Small project BMI.
# TEST for GIT

def bmi (weight, height):
    '''
    The BMI function takes weight and height as arguments
    and calculates the body mass index (BMI).

Arguments:
- weight (float): Weight in kilograms.
- height (float): Height in centimeters.

Return value:
- Body mass index (float) or None if the input is invalid.

Restrictions:
- The weight must be greater than 1.0 and must not exceed 200 kg.
- Height must be more than 1 cm and not exceed 2.5 m or 100 cm.

If the height is over 100 cm, it will be converted to meters.

BMI is calculated using the formula: BMI = weight / height^2.

Usage example:
bmi(70, 175) # Returns 22.85
    '''
    if weight < 1.0 or height < 1 or \
    weight > 200 or (height > 2.5 and height < 100):
        return
    elif height > 100:
         height = height / 100  # Conversion of height in meters.

    return round(weight / height ** 2, 2)  # Calculate BMI.


print(''' 
                        ##############
                        #            #
                        #     BMI    #
                        #            #
    This program will help you calculate your body mass index
    *********************************************************
''')

# choose = int(input('choose'))
# user_weight = float(input('Enter your weight (kg): '))
# user_height = float(input("Enter your height (cm/m):"))
print('''
    Make a choice:

 1 ---- Start calculation
-1 ---- Exit
          ''')
user_choice = int(input('---->  '))

while user_choice != -1:
    user_weight = float(input('Enter your weight (kg): '))
    user_height = float(input("Enter your height (cm/m): "))
    user_bmi = bmi(user_weight, user_height)

    if user_bmi == None:
        print(f'Sorry, you entered incorrect data {user_weight} {user_height}')
    elif user_bmi < 15.99:
        print(f'Your BMI {user_bmi} - SEVERE UNDERWEIGHT. \
Need urgent expert advice. Norm: 18.50 - 24.99. ')
    elif user_bmi < 18.50 and user_bmi > 16.00 :
        print(f'Your BMI {user_bmi} - INSUFFICIENT (DEFICIT) BODY WEIGHT. \
Need expert advice. Norm: 18.50 - 24.99. ')
    elif user_bmi < 25.99 and user_bmi > 25.00 :
        print(f'Your BMI {user_bmi} - OVERWEIGHT (PREOBESITY). \
Need expert advice. Norm: 18.50 - 24.99. ')
    elif user_bmi < 34.99 and user_bmi > 30.00 :
            print(f'Your BMI {user_bmi} - OBESITY OF THE FIRST DEGREE. \
Need expert advice. Norm: 18.50 - 24.99. ')
    elif user_bmi < 39.99 and user_bmi > 35.00 :
        print(f'Your BMI {user_bmi} - OBESITY OF THE SECOND DEGREE. \
Need expert advice. Norm: 18.50 - 24.99. ')
    elif user_bmi > 40.00 :
        print(f'Your BMI {user_bmi} - OBESITY OF THE THIRD DEGREE (MORBID). \
Need urgent expert advice. Norm: 18.50 - 24.99. ')
    else:
        print(f'Great 🎉, your BMI {user_bmi} is normal. Norm: 18.50 - 24.99. ')
    print('''
    Make a choice:

 1 ---- Start calculation
-1 ---- Exit
          ''')
    user_choice = int(input('---->  '))
    