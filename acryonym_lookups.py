dictionary={"BRB":" Be Right Back", "LOL" : "Laugh Out Loud", "AFK" : " Away From Keyboard" , "TTYL": " Talk To You Later", "GN": " Good Night" }

def lookup():
    while True:
        get_input= input ("Enter an acronym ( enter Q to quit ): ").upper().strip()
        if get_input in dictionary :
            print (dictionary [get_input])
        if get_input == "Q" :
            print ("Exiting")
            break
        if get_input not in dictionary: 
            new_term= input(f"{get_input} is not a setup term. Would you like to add it ?: ").strip().lower()
            if new_term == "yes" :
                meaning=input (f"what does {get_input} mean? : ")
                dictionary [get_input]={meaning}
                print (f"{get_input} added to the dictionary")
            if new_term == "no":
                print ("Okay we wont add this to the dictionary ")
            if new_term != "yes" and new_term != "no":
                print ("that wasnt a valid choice ")


if __name__ == '__main__':
    lookup()
