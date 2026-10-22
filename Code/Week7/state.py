def print_state(average_score):
    if average_score > 85 and average_score < 100:
        print("Very Good!")
    elif average_score > 50 and average_score <= 85 :
        print("Good!")
    elif average_score <= 50 :
        print("Try more!")