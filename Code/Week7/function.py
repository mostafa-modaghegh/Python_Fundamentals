''' math_score = float(input("Math score: "))
english_score = float(input("English score: "))
programming_score = float(input("Programming score: "))

average = (math_score + english_score + programming_score)/3

if average > 85 and average < 100:
    print("Very Good!")
elif average > 50 and average <= 85 :
    print("Good!")
elif average <= 50 :
    print("Try more!")
'''

def get_inputs():
    math_score = float(input("Math score: "))
    english_score = float(input("English score: "))
    programming_score = float(input("Programming score: "))
    return math_score , english_score , programming_score

def cal_average(math , english , programming):
    average = (math + english + programming)/3 
    return average

def state(average_score):
    if average_score > 85 and average_score < 100:
        print("Very Good!")
    elif average_score > 50 and average_score <= 85 :
        print("Good!")
    elif average_score <= 50 :
        print("Try more!")



math , english , programming = get_inputs()
average = cal_average(math , english , programming)
state(average)