def football ():
    attempts = int(input("Please enter the number of passing attempts made: "))
    # input number of passing yards (passing yards)
    passingYards = float(input("Please enter the number of passing yards: "))
    completions = int(input("Please enter the number of completed passing attempts: "))
    # input the number of passes for a touchdown (touchdown passes)
    touchdownPasses = int(input("Please enter the number of passes for a touchdown: "))
    # input number of times the ball was intercepted
    interceptions = int(input("Please enter the number of times the ball wast intercepted: "))
    # set perfect passer to 158.3
    perfectPasser = 158.3
    perfectPasser = float(perfectPasser)
    # calculate QB rate and set to "rating"
    rating = 100 * (5 * (completions / attempts - 0.3) + 0.25 * (passingYards / attempts - 3) +
                    20 * (touchdownPasses / attempts) + 2.375 - (25 * interceptions / attempts)) / 6
    rating = float(rating)
    # return rating
    return rating

def quidditch ():
    # input how many goals were scored
    goals = input("Please enter how many goals were scored: ")
    # input if the snitch was caught
    isSnitch = "Was the snitch caught?: "
    # if snitch was caught
    if isSnitch == "yes":
        # set snitch to 30
        snitch = 30
        snitch = int(snitch)
    # else snitch was not caught
    else:
        # set snitch to 0
        snitch = 0
        snitch = int(snitch)
    # calculate total score -- goal*10 + snitch
    totalScore = goals *10 + snitch
    totalScore = int(totalScore)
    # return total score
    return totalScore


def gymnastics():
    # input execution score 1
    e1 = input("Please enter the first execution score: ")
    e1 = int(e1)
    # input execution score 2
    e2 = input("Please enter the second execution score: ")
    e2 = int(e2)
    # input execution score 3
    e3 = input("Please enter the third execution score: ")
    e3 = int(e3)
    # input execution score 4
    e4 = input("Please enter the fourth execution score: ")
    e4 = int(e4)
    # input execution score 5
    e5 = input("Please enter the fifth execution score: ")
    e5 = int(e5)
    difficulty = input("Please enter the difficulty score: ")

    if e1 < e2 and e1 < e3 and e1 < e4 and e1 < e5:
        lowest = e1
    elif e2 < e1 and e2 < e3 and e2 < e4 and e2 < e5:
        lowest = e2
    elif e3 < e1 and e3 < e2 and e3 < e4 and e3 < e5:
        lowest = e3
    elif e4 < e1 and e4 < e2 and e4 < e3 and e4 < e5:
        lowest = e4
    else:
        lowest = e5


    if e1 > e2 and e1 > e3 and e1 > e4 and e1 > e5:
        highest = e1
    elif e2 > e1 and e2 > e3 and e2 > e4 and e2 > e5:
        highest = e2
    elif e3 > e1 and e3 > e2 and e3 > e4 and e3 > e5:
        highest = e3
    elif e4 > e1 and e4 > e2 and e4 > e3 and e4 > e5:
         highest = e4
    else:
        highest = e5

    average = ( e1 + e2 + e3 + e4 + e5 - highest - lowest )/3
    totalScore = average + difficulty
    return totalScore


def main():

    #input
    sport = input("Which sport do you want to calculate?: ")
    sport = sport.strip().lower()

    if sport != "football" and sport != "quidditch" and sport != "gymnastic":
        print("Answer is invalid")
    elif sport == "football":
        rating = football()
        if rating == 158.3:
            print(" You are a prefect passer ")
    else:
        print("your rating is" , rating )


    if sport == "quidditch":
     totalScore = quidditch ()
     print("total score is", totalScore)


    if sport == "gymnastic":
     gymnastic()
     print("Your total score is", totalScore )
    else:
     print("Invaild try again")


main()