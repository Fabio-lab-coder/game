import time
import random
import winsound

def Total_Game_End():
    print("\"Congratulations on completing the challenges!\"")
    time.sleep(2)
    print("\"I must admit, I am impressed\"")
    time.sleep(2)
    print("\"There were some very difficult puzzles in there\"")
    time.sleep(2)
    print("\"I think you've earned your freedom\"")
    time.sleep(2)
    print("\"GO!\"")
    time.sleep(0.5)
    print("\"NOW!\"")
    time.sleep(2)
    print("\"Before I change my mind, and I test you again!\"")
    time.sleep(2)
    print("The last door swings open, and you run for it as fast as you can.")
    time.sleep(2)
    print("The smell of fresh air drives you forwards into the bright blue sunlight.")
    time.sleep(2)
    print("")
    time.sleep(2)
    print("THE END")

score = 0

def Fabio_Puzzle():   
    def win_song():
        winsound.Beep(1046, 450) # C
        winsound.Beep(1174, 450) # D
        winsound.Beep(1318, 450) # E
        winsound.Beep(1396, 450) # F
        winsound.Beep(1318, 300) # E


    def lose_song():         
        winsound.Beep(1396, 450) # F
        winsound.Beep(1318, 450) # E
        winsound.Beep(1174, 450) # D
        winsound.Beep(1046, 450) # C
        winsound.Beep(1174, 450) # D
        

    def score_sound():
        winsound.Beep(2000, 70)
        winsound.Beep(2500, 80)
        winsound.Beep(3000, 110)

    def fail_sound():
        winsound.Beep(3000, 70)
        winsound.Beep(2500, 80)
        winsound.Beep(2000, 110)



    

    def quiz_ten():
        print("Quiz:")
        time.sleep(2)
        print("Which is the only vowel not used as the first letter in a US State??\n")
        time.sleep(2)
        choice = input(" 1 - U\n 2 - O\n 3 - I\n 4 - E\n 5 - A\n")
        global score
        if choice == "4":
            score_sound()
            print("Correct answer!.\n")
            score += 1
            time.sleep(2)
            choose_question()        
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()


    def quiz_nine():
        print("True or False:")
        time.sleep(2)
        print("The can-opener was not invented until 45 years after the tin can\n")
        time.sleep(2)
        choice = input(" 1 - False\n 2 - True\n")
        global score
        if choice == "2":
            score_sound()
            print("Correct answer!.\n")
            score += 1
            time.sleep(2)
            choose_question()                   
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()

    def quiz_eight():
        print("Quiz:")
        time.sleep(2)
        print("Which footballer has the most Instagram followers in the world - as of 2020?\n")
        time.sleep(2)
        choice = input(" 1 - Lionel Messi\n 2 - Cristiano Ronaldo\n 3 - Neymar\n")
        global score
        if choice == "2":
            score_sound()
            print("Correct answer!.\n")
            score += 1
            time.sleep(2)
            choose_question()                   
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()

    def quiz_seven():
        print("Quiz:")
        time.sleep(2)
        print("What is David Bowie’s real name?\n")
        time.sleep(2)
        choice = input(" 1 - David Evans\n 2 - David Beckam\n 3 - David Jones\n")
        global score
        if choice == "3":
            score_sound()
            print("Correct answer!.\n")
            score += 1
            time.sleep(2)
            choose_question()                 
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()


    def quiz_six():
        print("Quiz:")
        time.sleep(2)
        print("Which vitamin is the only one that you will not find in an egg?\n")
        time.sleep(2)
        choice = input(" 1 - Vitamin A\n 2 - Vitamin D\n 3 - Vitamin C\n")
        global score
        if choice == "3":
            score_sound()
            print("Correct answer!.\n")
            score += 1
            time.sleep(2)
            choose_question()                   
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()


    def quiz_five():
        print("Quiz:")
        time.sleep(2)
        print("Alberta is a province of which country?\n")
        time.sleep(2)
        choice = input(" 1 - Spain\n 2 - Canada\n 3 - Italy\n")
        global score
        if choice == "2":
            score_sound()
            print("Correct answer!.\n")
            score += 1
            time.sleep(2)
            choose_question()                   
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()

    def quiz_four():
        print("True of False:")
        time.sleep(2)
        print("There are McDonald’s in every continent except one\n")
        time.sleep(2)
        choice = input(" 1 - True\n 2 - False\n")
        global score
        if choice == "1":  
            score_sound()      
            print("Correct answer!.\n There's no McDonald’s in Antartica\n")
            score += 1
            time.sleep(2)
            choose_question()                   
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()

    def quiz_three():
        print("Quiz:")
        time.sleep(2)
        print("Which singer has the most UK Number One singles ever?\n")
        time.sleep(2)
        choice = input(" 1 - Beatles\n 2 - Take That\n 3 - Elvis Presley\n")
        global score
        if choice == "3":
            score_sound()
            print("Correct answer!.\n")        
            score += 1
            time.sleep(2)
            choose_question()                   
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()

    def quiz_two():
        print("Quiz:")
        time.sleep(2)
        print("Which country is the origin of the cocktail Mojito?\n")
        time.sleep(2)
        choice = input(" 1 - Cuba\n 2 - Mexico\n 3 - Spain\n")
        global score
        if choice == "1":
            score_sound()
            print("Correct answer!.\n")        
            score += 1
            time.sleep(2)
            choose_question()                   
        else:
            fail_sound()
            print("Wrong answer!\n")
            choose_question()

    def quiz_one():
        print("Quiz:")
        time.sleep(2)
        print("What are the five colours of the Olympic rings?\n")
        time.sleep(2)
        choice = input(" 1 - Blue, yellow, purple, green and red\n 2 - Blue, yellow, black, green and red\n 3 - Blue, yellow, black, green and purple\n")
        global score
        if choice == "2":
            score_sound()
            print("Correct answer!.\n")        
            score += 1
            time.sleep(2)
            choose_question()      
        else:
            fail_sound()       
            print(f"Wrong answer!\n")
            choose_question() 
        
    def quiz_won():
        global score
        win_song()
        print("QUIZ COMPLETE")
        time.sleep(3)
        print("Congratulations")
        time.sleep(3)
        print(f"You've got {score} correct questions in this quiz\n")
        Total_Game_End()
        # response = input("Do you want to play again? [Y/N]\n")
        # if response == "y" or response == "Y" or response == "yes" or response == "YES":
        #     score = 0
        #     start()
        # else:
        #     print("End of the game.")

    def quiz_lost():
        global score
        lose_song()
        print("QUIZ COMPLETE")
        time.sleep(3)       
        print("Unfortunately, you lost the game")
        time.sleep(3)
        print(f"You've got {score} correct questions in this quiz")
        print("You needed at least 7.")        
        time.sleep(3)
        response = input("Do you want to play again? [Y/N]")
        if response == "y" or response == "Y" or response == "yes" or response == "YES":
            score = 0
            start()
        elif response == "n" or response == "N" or response == "no" or response == "NO":
            print("End of the game.")
        else:
            print("Sorry I didn't quite catch that")
            quiz_lost


    def choose_question():
        global score
        if len(questions) == 0 and score >= 7:
            quiz_won()
        elif len(questions) == 0 and score < 7: 
            quiz_lost()
        elif questions[0] == "quiz_one":
            if len(questions) > 0:
                del questions[0]
            quiz_one()
        elif questions[0] == "quiz_two":
            if len(questions) > 0: 
                del questions[0]        
            quiz_two()
        elif questions[0] == "quiz_three":
            if len(questions) > 0: 
                del questions[0]        
            quiz_three()
        elif questions[0] == "quiz_four":
            if len(questions) > 0: 
                del questions[0]        
            quiz_four()
        elif questions[0] == "quiz_five":
            if len(questions) > 0:
                del questions[0]
            quiz_five()
        elif questions[0] == "quiz_six":
            if len(questions) > 0: 
                del questions[0]        
            quiz_six()
        elif questions[0] == "quiz_seven":
            if len(questions) > 0: 
                del questions[0]        
            quiz_seven()
        elif questions[0] == "quiz_eight":
            if len(questions) > 0: 
                del questions[0]        
            quiz_eight()
        elif questions[0] == "quiz_nine":
            if len(questions) > 0: 
                del questions[0]        
            quiz_nine()
        elif questions[0] == "quiz_ten":
            if len(questions) > 0: 
                del questions[0]        
            quiz_ten()
        
        
        


    def start(): 
        print("\n")  
        print("Welcome to this quiz game!")
        time.sleep(2)    
        print("Are you ready for this 10 quiz questions?")     
        time.sleep(2)
        print("At the end of the quiz, you'll have to score at least 7 questions to win the game.")
        time.sleep(2)   
        global questions    
        questions = [
            "quiz_one",
            "quiz_two",
            "quiz_three",
            "quiz_four",
            "quiz_five",
            "quiz_six",
            "quiz_seven",
            "quiz_eight",
            "quiz_nine",
            "quiz_ten"
        ]
        random.shuffle(questions)
        choose_question()

    

    start()


def Lowai_Puzzle():
    def opened_door():
        time.sleep(2)
        print("Well done! You have successfully opened the door.")
        time.sleep(2)
        start_game()
    def pestol_chosen():     
        time.sleep(2)   
        print("as soon as the pistol fell down you notice the note stuck behind it")
        time.sleep(4)
        print("the note says {the glass is bullet proof save the bullets for your self")
        time.sleep(5)
        print("you lost, you gonna die lonely but you still can use the bullets hahah")
        response = input("Would you like to play again? [Y/N] ")
        if response == "Y" or response == "y" or response == "Yes" or response == "yes" or response == "YES":
            level_one()
        elif response == "N" or response == "n" or response == "No" or response == "no" or response == "NO":
            print("Thank you for playing.")
        else:
            print("sorry I didn't quite catch that")  
            pestol_chosen()

    def key_3_chosen():
        time.sleep(2)
        print("You just have your key in hand")
        time.sleep(2)
        print("oops the Key you have chosen doesn`t open neither the main or small door")
        time.sleep(5)
        print("you lost, You gonna die lonely hahaha")
        response = input("Would you like to play again? [Y/N] ")
        if response == "Y" or response == "y" or response == "Yes" or response == "yes" or response == "YES":
            level_one()
        elif response == "N" or response == "n" or response == "No" or response == "no" or response == "NO":
            print("Thank you for playing.")
        else:
            print("sorry I didn't quite catch that")  
            key_3_chosen()

    def key_2_chosen():
        time.sleep(2)
        print("as you try to open the main door you can feel how it fits perfectly.")
        time.sleep(2)
        print("Congratulations you just finished this game, you entered the room.")
        print("")
        time.sleep(2)
        print("Loading next puzzle...Please wait...")
        time.sleep(5)
        Fabio_Puzzle()
    def key_pestol_chosen():
        time.sleep(2)
        print("You have just £4 pound in your budget.")
        time.sleep(2)
        answer = input("again which key would you like to choose [key_2/key_3]: ")
        if answer == "2" or answer == "key_2" or answer == "Key_2" or answer == "KEY_2" or answer == "Two" or answer == "TWO" or answer == "two":
            key_2_chosen()
        elif answer == "3" or answer == "key_3" or answer == "Key_3" or answer == "KEY_3" or answer == "Three" or answer == "THREE" or answer == "three":
            key_3_chosen()
        else:
            print("you lose. ")
            start_game()         
    def key_1_chosen():
        time.sleep(3)
        print("clever choice but you can`t get the pistol anymore, the bad news is the key you`ve just got can`t open the main door.")
        time.sleep(9)
        print("the good news however you found out, that the key is for the small door.")
        time.sleep(9)
        print("as you enter the safe room full with garbage you start looking for anything that might help.")
        time.sleep(9)
        print("evetually you found one note that says {to travel in time you have to be faster than speed of light}. ")
        time.sleep(9)
        print("well done, you figured out and found your way to the lamp.")
        time.sleep(9)
        print("broke the lamp and found one pound which you gonna add to your bodget.")
        time.sleep(9)
        answer = input("Now that your budget  is £4, which key you wanna pay for [key_2/key_3]: ")
        time.sleep(2)
        if answer =="1" or answer == "key_1" or answer == "Key_1" or answer == "KEY_1" or answer == "One" or answer == "ONE" or answer == "one":
            print("you already have the key and wasted your money for nothing, the game is over.")
            start_game()
        elif answer == "pistol" or answer == "Pistol" or answer == "PISTOL" or answer == "The_pistol" or answer == "THE_PISTOL" or answer == "the_pistol":
            key_pestol_chosen()
        elif answer == "2" or answer == "key_2" or answer == "Key_2" or answer == "KEY_2" or answer == "Two" or answer == "TWO" or answer == "two":
            key_2_chosen()
        elif answer == "3" or answer == "key_3" or answer == "Key_3" or answer == "KEY_3" or answer == "Three" or answer == "THREE" or answer == "three":
            key_3_chosen()
        else:
            print("you are wasting your time. ")
        key_pestol_chosen()
    def level_one():
        time.sleep(2)
        print("You just walked in through the Door.")
        time.sleep(4)
        print("To the left a small door, In front of you the main Door and to the right stand a big Drink machine fixed to the wall")
        time.sleep(9)
        print("the drink machine contains three bottles which have keys inside and in one empty gap there is a pistol. ")
        time.sleep(8)
        print("as you look forther you find £5 coins spread on the floor")
        time.sleep(7)
        print("Now the pistol you can get for £5 the whole budget.")
        time.sleep(7)
        print("but the keys inside the bottles have diffrent value")
        time.sleep(7)
        print("key_1 for £2, key_2 for £3 and key_3 for £4")
        time.sleep(7)
        response = input("what choise would you like to go for first? [1/2/3/pistol]: ")
        time.sleep(2)
        if response == "1" or response == "key_1" or response == "Key_1" or response == "KEY_1" or response == "One" or response == "ONE" or response == "one":
            key_1_chosen()
        elif response == "2" or response == "key_2" or response == "Key_2" or response == "KEY_2" or response == "Two" or response == "TWO" or response == "two":
            key_2_chosen()
        elif response == "3" or response == "key_3" or response == "Key_3" or response == "KEY_3" or response == "Three" or response == "THREE" or response == "three":
            key_3_chosen()
        elif response == "pistol" or response == "Pistol" or response == "The pistol":
            pestol_chosen()
        else:
            print("Thank you for playing.")
            start_game()   
        #NOTE: These functions commented out are placeholders for these if/else statements to perform an action.
    def start_game():
        print("hello and welcome to my game.")
        time.sleep(2)
        global name
        time.sleep(2)
        name = input("what is your name?")
        time.sleep(2)
        print(f"hello {name}, it`s great to meet you.")
        time.sleep(2)
        print("my name is chucky")
        time.sleep(2)
        response = input("are you ready to play? [Y/N]: ")
        time.sleep(2)
        if response == "Y" or response == "y" or response == "Yes" or response == "yes" or response == "YES":
            print("Great! let`s begin then shall we.")
            level_one()
        else:
            print("Thank you for playing.")
            start_game()
    start_game()   

Keys = 0
Broomhandle = 0
Tape =0
Hairdryer = 0
Screwdriver = 0
Broom_Screwdriver = 0
Door_Check = 0
Tool_Check = 0
Fan_Check = 0
Room_Check = 0

Tool_Check_2 = 0
Fan_Check_2 = 0
Vent_Check = 0
Broom_Check = 0
def Alex_Puzzle():
    options_1 = ["[1. Look at Door]", "[2. Look at Toolbox]", "[3. Look at Ceiling Fan]", "[4. Look Around The Room]"]
    options_2 = ["[1. Use Door]", "[2. Use Toolbox]", "[3. Use Ceiling Fan]", "[4. Use Vent]", "[5. Get Broomhandle]", "[6. Inventory]"]
    Inventory = []
    Inventory_Options = ["[1. Leave Inventory]", "[2. Use Items]"]
    

    def Alex_Puzzle_End():
        print("The heavy steel door swings open")
        time.sleep(2)
        print("Freedom is just one step closer...")
        print("")
        time.sleep(2)
        print("Loading next puzzle...Please wait...")
        time.sleep(5)
        print("")
        Lowai_Puzzle()

    def Alex_Puzzle_Stage_Two():
        global Keys
        global Broomhandle
        global Tape
        global Hairdryer
        global Screwdriver
        global Broom_Screwdriver
        global Tool_Check_2
        global Fan_Check_2
        global Vent_Check
        global Broom_Check 
        print("There's nothing else to look at in this room")
        time.sleep(2)
        print("Time to find my way out of here")
        print(*options_2, sep = "\n")
        print("[ALL MENU OPTIONS CAN BE CHOSEN BY NUMBER, BUT ALL INVENTORY OPTIONS MUST BE CHOSEN BY NAME]")
        Action = input("What do you want to do? - ")
        if Action == "1" or Action == "Use Door" or Action == "use door" or Action == "Use door" or Action == "use Door" or Action == "USE DOOR":
            print("you approach the door again")
            if  Keys == 0:
                print("you can't unlock any of the locks yet, so there's no point in trying the door.")
                time.sleep(2)
                Alex_Puzzle_Stage_Two()
            elif Keys == 1:
                print("You only have one key so far, you need another to get out of here.")
                time.sleep(2)
                Alex_Puzzle_Stage_Two()
            elif Keys == 2:
                print("You have both of the keys, time to get the hell out of here")
                time.sleep(2)
                Alex_Puzzle_End()
        elif Tool_Check_2 == 1 and Action == "2" or Action == "Use Toolbox" or Action == "use toolbox" or Action == "Use toolbox" or Action == "use Toolbox" or Action == "USE TOOLBOX":
            print("I already have everything from the toolbox, there's no point checking again")
            Alex_Puzzle_Stage_Two()
        elif Action == "2" or Action == "Use Toolbox" or Action == "use toolbox" or Action == "Use toolbox" or Action == "use Toolbox" or Action == "USE TOOLBOX":
            print("You crouch down in front of the rusted toolbox and open it's lid.")
            time.sleep(2)
            print("You're not entirely sure how all of these items are going to help you escape from this room,")
            time.sleep(2)
            print("But you take them all anyway, you never no what you might need.")
            Tape = 1
            Screwdriver = 1
            Hairdryer = 1
            options_2.remove("[2. Use Toolbox]")
            Tool_Check_2 = 1
            Inventory.insert(2, "You have a roll of tape")
            Inventory.insert(3, "You have a rusty screwdriver")
            Inventory.insert(4, "You Have a Battery Powered Hairdryer")
            time.sleep(2)
            Alex_Puzzle_Stage_Two()
        elif Fan_Check_2 == 1 and Action == "3" or Action == "Use Ceiling Fan" or Action == "use ceiling fan" or Action == "Use ceiling fan" or Action == "use Ceiling fan" or Action == "use Ceiling Fan" or Action == "use ceiling Fan" or Action == "USE CEILING FAN":
            print("I already have the key from the Ceiling Fan, I don't think there's anything more I can do with that")
            Alex_Puzzle_Stage_Two()
        elif Action == "3" or Action == "Use Ceiling Fan" or Action == "use ceiling fan" or Action == "Use ceiling fan" or Action == "use Ceiling fan" or Action == "use Ceiling Fan" or Action == "use ceiling Fan" or Action == "USE CEILING FAN":
            if Broom_Screwdriver == 1:
                print("I take the Screwdriver attached to the end of the Broomhandle and carefully reach it up to the key.")
                time.sleep(4)
                print("It takes a few tries and a lot of swearing, but I eventually manage to hook the key over the screwdriver and bring it down to my level")
                time.sleep(3)
                print("Now I have one of the keys I need to get out of here.")
                Keys += 1
                options_2.remove("[3. Use Ceiling Fan]")
                Fan_Check_2 = 1
                Inventory.insert(0, "I have {} keys".format(Keys))
                if Keys == 2:
                    Inventory.remove("I have 1 keys")
                Alex_Puzzle_Stage_Two()
            elif Broomhandle == 1 and Screwdriver == 1:
                print("I think I have everything I need to get that key down.")
                Alex_Puzzle_Stage_Two()
            elif Broomhandle == 0:
                print("I can't reach the fan from down here, I'll have to find some other way of getting that key down")
                Alex_Puzzle_Stage_Two()
            elif Broomhandle == 1:
                print("I might be able to get that key down if I could get something narrow enough through it")
                Alex_Puzzle_Stage_Two()
        elif Vent_Check == 1 and Action == "4" or Action == "Use Vent" or Action == "use vent" or Action == "Use vent" or Action == "use Vent" or Action == "USE VENT":
            print("I already have the key from the vent, I don't think there's anything else stuck in there.")
            Alex_Puzzle_Stage_Two()
        elif Action == "4" or Action == "Use Vent" or Action == "use vent" or Action == "Use vent" or Action == "use Vent" or Action == "USE VENT":
            print("I crouch down in front of the vent near the door")
            time.sleep(2)
            print("Behind the vent cover, I can see a small fan slowly rotating.")
            time.sleep(2)
            print("I can also hear a slight echo coming from somewhere, maybe this connects to the other vent")
            time.sleep(2)
            print(Inventory)
            Vent_Choice = input("What item should I use on the vent? - ")
            if Vent_Choice == "Hairdryer" or Vent_Choice == "hairdryer" or Vent_Choice == "HAIRDRYER" or Vent_Choice == "Battery Powered Hairdryer" or Vent_Choice == "BATTERY POWERED HAIRDRYER" or Vent_Choice == "battery powered hairdryer":
                print("I point the oddly modified Hairdryer at the vent and switch it on")
                time.sleep(2)
                print("It emits a harsh whirring noise as it blows hot air through the vent system")
                time.sleep(2)
                print("I can hear the Ceiling Fan spinning faster behind me as it is blasted with air")
                time.sleep(2)
                print("Suddenly, I hear a loud rattling, as something shoots out of the vent over my head")
                time.sleep(2)
                print("I turn around to see a key has been shot onto the floor")
                Keys += 1
                options_2.remove("[4. Use Vent]")
                Vent_Check = 1
                Inventory.insert(0, "I have {} keys".format(Keys))
                if Keys == 2:
                    Inventory.remove("I have 1 keys")
                Alex_Puzzle_Stage_Two()
            else:
                print(f"I'm not sure what I hoped to accomplish by sticking {Vent_Choice} into that vent.")
                Alex_Puzzle_Stage_Two()
        elif Broom_Check == 1 and Action == "5" or Action == "Get Broomhandle" or Action == "get broomhandle" or Action == "Get broomhandle" or Action == "get Broomhandle" or Action == "GET BROOMHANDLE":
            print("I already grabbed the Broomhandle, I don't think I should put it back.")
            Alex_Puzzle_Stage_Two()
        elif Action == "5" or Action == "Get Broomhandle" or Action == "get broomhandle" or Action == "Get broomhandle" or Action == "get Broomhandle" or Action == "GET BROOMHANDLE":
            print("You walk over to grab the broken Broomhandle.")
            time.sleep(2)
            print("It feels heavy and solid in your hands, and is a little over a metre long.")
            time.sleep(2)
            Broomhandle = 1
            options_2.remove("[5. Get Broomhandle]")
            Broom_Check = 1
            Inventory.insert(1, "You Have a broken section of broomhandle")
            Alex_Puzzle_Stage_Two()
        elif Action == "6" or Action == "Inventory" or Action == "inventory" or Action == "INVENTORY":
            if len(Inventory) == 0:
                print("You have nothing in your inventory")
                Alex_Puzzle_Stage_Two()
            else:
                print(Inventory, sep = "\n")
                time.sleep(2)
                print(*Inventory_Options)
                time.sleep(2)
                Inventory_Choice = input("What would you like to do? - ")
                if Inventory_Choice == "2" or Inventory_Choice == "Use Items" or Inventory_Choice == "use items" or Inventory_Choice == "Use items" or Inventory_Choice == "use Items" or Inventory_Choice == "USE ITEMS":
                    Item_Choice_1 = input("Which item would you like to use? - ")
                    if Item_Choice_1 == "Broomhandle" or Item_Choice_1 == "broomhandle" or Item_Choice_1 == "BROOMHANDLE" and Broomhandle == 1:
                        print("I think I could use this Broomhandle with something else")
                        time.sleep(2)
                        Item_choice_2 = input("What can I use this with? - ")
                        if Item_choice_2 == "Screwdriver" or Item_choice_2 == "screwdriver" or Item_choice_2 == "SCREWDRIVER":
                            print("I use the tape and attach the screwdriver to the end of the Broomhandle, now I might be able to get that key!")
                            Broomhandle = 0
                            Inventory.remove("You Have a broken section of broomhandle")
                            Tape = 0
                            Inventory.remove("You have a roll of tape")
                            Screwdriver = 0
                            Inventory.remove("You have a rusty screwdriver")
                            Broom_Screwdriver = 1
                            Inventory.insert(-1, "You have a screwdriver, taped to the end of a broken Broomhandle")
                            Alex_Puzzle_Stage_Two()
                        elif Item_choice_2 == "Tape" or Item_choice_2 == "tape" or Item_choice_2 == "TAPE":
                            print("I might be able to attach something to this Broomhandle, but what?")
                            Alex_Puzzle_Stage_Two()
                        else:
                            print("I don't think those go together")
                            Alex_Puzzle_Stage_Two()
                    elif Item_Choice_1 == "Screwdriver" or Item_Choice_1 == "screwdriver" or Item_Choice_1 == "SCREWDRIVER" and Broomhandle == 1:
                            print("I think I could use this Screwdriver with something else")
                            time.sleep(2)
                            Item_choice_2 = input("What can I use this with? - ")
                            if Item_choice_2 == "Broomhandle" or Item_choice_2 == "broomhandle" or Item_choice_2 == "BROOMHANDLE":
                                print("I use the tape and attach the screwdriver to the end of the Broomhandle, now I might be able to get that key!")
                                Broomhandle = 0
                                Inventory.remove("You Have a broken section of broomhandle")
                                Tape = 0
                                Inventory.remove("You have a roll of tape")
                                Screwdriver = 0
                                Inventory.remove("You have a rusty screwdriver")
                                Broom_Screwdriver = 1
                                Inventory.insert(-1, "You have a screwdriver, taped to the end of a broken Broomhandle")
                                Alex_Puzzle_Stage_Two()
                            elif Item_choice_2 == "Tape" or Item_choice_2 == "tape" or Item_choice_2 == "TAPE":
                                print("I might be able to attach this Screwdriver to something, but what?")
                                Alex_Puzzle_Stage_Two()
                            else:
                                print("I don't think those go together")
                                Alex_Puzzle_Stage_Two()
                    else:
                        print("I'm not sure what I can do with that yet.")
                        Alex_Puzzle_Stage_Two()
                elif Inventory_Choice == "1" or Inventory_Choice == "Leave Inventory" or Inventory_Choice == "leave inventory" or Inventory_Choice == "Leave inventory" or Inventory_Choice == "leave Inventory" or Inventory_Choice == "LEAVE INVENTORY":
                    print("You close your inventory")
                    time.sleep(2)
                    Alex_Puzzle_Stage_Two()
                else:
                    print("I didn't recognise that command")
                    time.sleep(2)
                    Alex_Puzzle_Stage_Two()
        elif Action == "Kick Door" or Action == "kick door" or Action == "Kick door" or Action == "kick Door" or Action == "KICK DOOR":
            print("Out of frustration, you let out a scream of anger and charge at the door")
            time.sleep(2)
            print("You leap into the air and kick out with all your might!")
            rand_num = random.randint(1,101)
            if rand_num == 100:
                print("The door burst apart as you crash through it. You don't have time for these stupid puzzles!")
                
                Alex_Puzzle_End()
            else:
                print("You crash into the door and fall limply to the floor. I don't know what else you expected to happen really.")
                time.sleep(2)
                Alex_Puzzle_Stage_Two()
        else:
            print(f"Sorry, I'm not quite sure what you meant by {Action}, would you mind trying again?")
            time.sleep(2)
            Alex_Puzzle_Stage_Two()

            
    def Alex_Puzzle_Start():
        global Door_Check
        global Tool_Check
        global Fan_Check
        global Room_Check
        if len(options_1) == 0:
            Alex_Puzzle_Stage_Two()
        else:
            print(*options_1, sep = "\n")
            Look_At = input("What do you look at? - ")
            if  Door_Check == 0 and Look_At == "1" or Look_At == "Look at Door" or Look_At == "look at door" or Look_At == "Look at door" or Look_At == "look at Door" or Look_At == "LOOK AT DOOR":
                print("You stand in front of the door and give it a quick scan.")
                time.sleep(2)
                print("It seems to be built into a sturdy steel frame, not likely to be kicked down.")
                time.sleep(2)
                print("A slight breeze can be felt blowing from the crack beneath the door")
                time.sleep(2)
                print("On the right side of the door is a simple door handle, but underneath it are 2 solid looking locks.")
                time.sleep(2)
                print("Clearly you'll need to find the keys")
                options_1.remove("[1. Look at Door]")
                time.sleep(2)
                Door_Check += 1
                Alex_Puzzle_Start()
            elif Door_Check == 1 and Look_At == "1" or Look_At == "Look at Door" or Look_At == "look at door" or Look_At == "Look at door" or Look_At == "look at Door" or Look_At == "LOOK AT DOOR":
                print("I've aleady looked at the Door, I don't need to look at it again.")
                Alex_Puzzle_Start()
            elif Tool_Check == 1 and Look_At == "2" or Look_At == "Look at Toolbox" or Look_At == "look at toolbox" or Look_At == "Look at toolbox" or Look_At == "look at Toolbox" or Look_At == "LOOK AT TOOLBOX" :
                print("I've aleady looked at the Toolbox, I don't need to look at it again.")
                Alex_Puzzle_Start()
            elif Tool_Check == 0 and Look_At == "2" or Look_At == "Look at Toolbox" or Look_At == "look at toolbox" or Look_At == "Look at toolbox" or Look_At == "look at Toolbox" or Look_At == "LOOK AT TOOLBOX":
                print("On the floor in front of you is a rusty old toolbox.")
                time.sleep(2)
                print("You nudge the lid open with your foot, inside you find:")
                time.sleep(2)
                print("A roll of electrical tape, a rusty screwdriver and a... battery powered hair dryer?")
                time.sleep(2)
                print("What these could be for, you have no idea, but they might come in handy later.")
                options_1.remove("[2. Look at Toolbox]")
                time.sleep(2)
                Tool_Check = +1
                Alex_Puzzle_Start()
            elif Fan_Check == 1 and Look_At == "3" or Look_At == "Look at Ceiling Fan" or Look_At == "look at ceiling fan" or Look_At == "Look at ceiling fan" or Look_At == "look at Ceiling fan" or Look_At == "look at Ceiling Fan" or Look_At == "look at ceiling Fan" or Look_At == "LOOK AT CEILING FAN":
                print("I've aleady looked at the Ceiling Fan, I don't need to look at it again.")
                Alex_Puzzle_Start()
            elif Fan_Check == 0 and Look_At == "3" or Look_At == "Look at Ceiling Fan" or Look_At == "look at ceiling fan" or Look_At == "Look at ceiling fan" or Look_At == "look at Ceiling fan" or Look_At == "look at Ceiling Fan" or Look_At == "look at ceiling Fan" or Look_At == "LOOK AT CEILING FAN":
                print("Hanging from the roof is a battered old Ceiling Fan.")
                time.sleep(2)
                print("It spins lethargically, propelled by some mysterious breeze.")
                time.sleep(2)
                print("You spend some time pondering what might be causing it to spin, when you notice something...")
                time.sleep(2)
                print("THERE! Hanging from one of the blades of the fan is a key!")
                time.sleep(2)
                print("It's too high out of your reach though, you'll have to find some way to get it down.")
                options_1.remove("[3. Look at Ceiling Fan]")
                time.sleep(2)
                Fan_Check = +1
                Alex_Puzzle_Start()
            elif Room_Check == 1 and Look_At == "4" or Look_At == "Look Around The Room" or Look_At == "look around the room" or Look_At == "Look around the room" or Look_At == "look around the Room" or Look_At == "LOOK AROUND THE ROOM" or Look_At == "Look Around the room" or Look_At == "Look Around The room"or Look_At == "look Around the room" or Look_At == "look Around The room" or Look_At == "look Around The room" or Look_At == "Look Around The Room" or Look_At == "look around The room" or Look_At == "look around The Room" or Look_At == "look Around The room":
                ("I've aleady looked around the Room, I don't need to look around it again.")
                Alex_Puzzle_Start()
            elif Room_Check == 0 and Look_At == "4" or Look_At == "Look Around The Room" or Look_At == "look around the room" or Look_At == "Look around the room" or Look_At == "look around the Room" or Look_At == "LOOK AROUND THE ROOM" or Look_At == "Look Around the room" or Look_At == "Look Around The room"or Look_At == "look Around the room" or Look_At == "look Around The room" or Look_At == "look Around The room" or Look_At == "Look Around The Room" or Look_At == "look around The room" or Look_At == "look around The Room" or Look_At == "look Around The room":
                print("You take a look around the room.")
                time.sleep(2)
                print("You actually notice a few things you'd missed at first glance.")
                time.sleep(2)
                print("Leaning against the right wall is what looks like a broken broomhandle.")
                time.sleep(2)
                print("And on the far wall there are two vents near the door.")
                time.sleep(2)
                print("One of the vents is at floor level, while the other is much higher on the wall, almost at level with the ceiling fan.")
                options_1.remove("[4. Look Around The Room]")
                time.sleep(2)
                Room_Check += 1
                Alex_Puzzle_Start()
            elif Look_At == "skip" or Look_At == "Skip" or Look_At == "SKIP":
                Alex_Puzzle_Stage_Two()
            else:
                print("Sorry, I didn't recognise that input, please try again.")
                time.sleep(2)
                Alex_Puzzle_Start()
                
    def Alex_Puzzle_Intro():
            print("In front of you is a dark stone room.")
            time.sleep(2)
            print("Inside the room is a small tool box agaist the left wall, and a slowly spinning ceiling fan hanging above you.")
            time.sleep(3)
            print("At the other end of the room is a locked door.")
            time.sleep(2)
            Alex_Puzzle_Start()

    Alex_Puzzle_Intro()

def James_Puzzle():
    import sys,time,os 

    def end_game():
        time.sleep(2)
        print("GAME OVER YOU WERE KILLED BY THE GATEKEEPER")
        time.sleep(2)
        start_over = input ("would you like to try again [Y/N]:")
        if start_over == "y" or start_over == "Y":
            print("lets play".upper())
            start_level()
        elif start_over == "N" or start_over == "n": 
            print(" i though that would be you answer ".upper()) 
            end_game()
        else: #this else statement added by Kim
            print("Why do you proceed to test my patients!".upper())
            end_game() 

    # def next_level():
    #     time.sleep(2)
    #     if next_level == "Y" or next_level == "y":
    #         print("starting next puzzle")
    #     elif next_level == "N" or next_level == "n":
    #         print("Game Over")
    #     else:
    #         print("you will be trapped here forever..... and a day")
    #     next_level()
        
    text = "Hello and welcome to doors of darkness, you will now be entering into strange room\n\
            the likes of witch you have never seen before, you step foward into the room...\n\
            an see what seems to be four large oak doors each with a unique glow "

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


    def door_d_choosen():
        print("")
        time.sleep(2)
        print("hmmm... door D for the doomed it is says the old man")
        time.sleep(2)
        print("many have choosen this path befor but most tend not too succeed the the old man persists")
        print("")
        print("     __________  ")
        time.sleep(0.3)
        print("   |  __ D __  | ")
        time.sleep(0.3)
        print("   | |  | |  | | ")
        time.sleep(0.3)
        print("   | |  | |  | | ")
        time.sleep(0.3)
        print("   | |__| |__| | ")  
        time.sleep(0.3)
        print("   |  __   __  | ") 
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ") 
        time.sleep(0.3)
        print("   | |__| |__| |  ")  
        time.sleep(0.3)
        print("   | __________|  ") 
        print("")
        print("will you! says the gatekeeper")
        time.sleep(2)
        print("go forth says the gatekeeper standing by the choosen door")
        time.sleep(2)
        print("you approach the door for some unkown reason feeling confident about your choice")
        time.sleep(2)
        print("you open the door exposing the portal close you eyes an jump stright in")
        time.sleep(2)
        print("the cunning old gate keeper smiles to himself")
        time.sleep(2)
        print("you open your eyes and see nothing, no light, no dark, there are now sounds, you feel nothing")
        time.sleep(2)
        print("")
        print("              ...")
        time.sleep(0.2)
        print("            ;::::;")
        time.sleep(0.2)
        print("           ;::::; :;")
        time.sleep(0.2)
        print("         ;:::::'   :;")
        time.sleep(0.2)
        print("        ;:::::;     ;.")
        time.sleep(0.2)
        print("       ,:::::'       ;           OOO")
        time.sleep(0.2)
        print("       ::::::;       ;           OOOOO")
        time.sleep(0.2)
        print("       ;:::::;       ;           OOOOOO")
        time.sleep(0.2)
        print("      ,;::::::;     ;'         / OOOOOOO")
        time.sleep(0.2)
        print("      ;:::::::::`. ,,,;.      /  / DOOOOOO")
        time.sleep(0.2)
        print("    .';:::::::::::::::::;,   /  /     DOOOO")
        time.sleep(0.2)
        print("   ,::::::;::::::;;;;::::;, /  /        DOOO               You are neither dead or alive  ")
        time.sleep(0.2)
        print(";`::::::`'::::::;;;::::: ,#/  /          DOOO                  A fate worse than death ")
        time.sleep(0.2)
        print(":`:::::::`;::::::;;::: ;::#  /            DOOO        And in this state you will remain for eternity ")
        time.sleep(0.2)
        print("::`:::::::`;:::::::: ;::::# /              DOO                        And a day ")
        time.sleep(0.2)
        print("`:`:::::::`;:::::: ;::::::#/               DOO")
        time.sleep(0.2)
        print(" :::`:::::::`;; ;:::::::::##                OO")
        time.sleep(0.2)
        print(" ::::`:::::::`;::::::::;:::#                OO")
        time.sleep(0.2)
        print("  :::::`::::::::::::;'`:;::#                O")
        time.sleep(0.2)
        print("   :::::`::::::::;' /  / `:#")
        time.sleep(0.2)
        print("  ::::::`:::::;'  /  /   `#")
        print("")
        print("you are neither dead or alive but somewhere inbetween a fate worse than death in this state you will remain for eternity and a day")
        time.sleep(2)
        print("you journy has ended")
        time.sleep(2)
        start_over = input ("would you like to try again [Y/N]:") 
        if start_over == "y" or start_over == "Y":
            print("lets play".upper())
            start_level()
        elif start_over == "N" or start_over == "n": 
            print(" i though that would be your answer ".upper()) 
            end_game()
        else:
            print("Why do you proceed to test my patients!".upper())
            end_game() #changed from door_d_chosen() to end_game() to make game more logical

    #####################################################################

    def door_c_choosen():
        time.sleep(2)
        print("")
        print("As you please door C it is exclaims the gatekeeper")
        time.sleep(2)
        print("this was a dark devilish looking door with some strange markrings etched into the wood")
        print("")
        print("     __________  ")
        time.sleep(0.3)
        print("   |  __ C __  | ")
        time.sleep(0.3)
        print("   | |  | |  | | ")
        time.sleep(0.3)
        print("   | |  | |  | | ")
        time.sleep(0.3)
        print("   | |__| |__| | ")  
        time.sleep(0.3)
        print("   |  __   __  | ") 
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ") 
        time.sleep(0.3)
        print("   | |__| |__| |  ")  
        time.sleep(0.3)
        print("   | __________|  ") 
        print("")
        print("just remmber things aren't always as they seem he says while ushering you towards the door")
        time.sleep(2)
        print("you head towrdas the with anticpation unusure weather to enter")
        time.sleep(2)
        print("don't be afraid of the unkown, the man says, the only thing garuenteed in this life is death")
        time.sleep(2)
        print("uncomforted by the mans advice heeding his words of wisdom you take a leap of faith ")
        time.sleep(2)
        print("or is it stupidity")
        time.sleep(2)
        print("you open the door eyes close and accept you fate....")
        time.sleep(2)
        print("a monment passes your eyes opene wide and you are not dead")
        time.sleep(2)
        print("you release you are out the room amazing! ")
        time.sleep(2)
        print("")
        print("      Yoohoo freedom!  .")
        time.sleep(0.5)
        print("                             -._ O /         ")
        time.sleep(0.5)
        print("                                ` '          ")
        time.sleep(0.5)
        print("                               / \           ")
        time.sleep(0.5)
        print("                               ())           ")
        time.sleep(0.5)
        print("    __     _..--.. .-'`-.     .-d-b-.       ")
        time.sleep(0.5)
        print(" --'  `_.-'       ``.._. `  .'       `.  _.")
        time.sleep(0.5)
        print("    .-'                               ,-' ")
        print("")
        time.sleep(1)
        print("But where are you? Is this the end of the beging or the beging of the end")
        time.sleep(1)
        print("Your journey continues...")
        print("")
        time.sleep(2)
        print("Loading next puzzle...Please wait...")
        time.sleep(5)
        print("")
        Alex_Puzzle()
        

    ###############################################################

    def door_b_choosen():
        print("")
        time.sleep(2)
        print("Aaah... door B, Fine choice")
        time.sleep(2)
        print("")
        print("     __________  ")
        time.sleep(0.3)
        print("   |  __ B __  | ")
        time.sleep(0.3)
        print("   | |  | |  | | ")
        time.sleep(0.3)
        print("   | |  | |  | | ")
        time.sleep(0.3)
        print("   | |__| |__| | ")  
        time.sleep(0.3)
        print("   |  __   __  | ") 
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ") 
        time.sleep(0.3)
        print("   | |__| |__| |  ")  
        time.sleep(0.3)
        print("   | __________|  ") 
        print("")
        print("Or is it?! says the gatekeeper")
        time.sleep(2)
        print("you may proceed he says raising an arm pointing to the door with his crooked hands")
        time.sleep(2)
        print("you approach the door and feel a sinister chill down your back")
        time.sleep(2)
        print("you open the door exposing the portal close you eyes an jump stright in")
        time.sleep(2)
        print("the cunning old gate keeper smiles to himself")
        time.sleep(2)
        print("you open your eyes and see nothing, no light, no dark, there are now sounds, you feel nothing")
        time.sleep(2)
        print("")
        print("              ...")
        time.sleep(0.2)
        print("            ;::::;")
        time.sleep(0.2)
        print("           ;::::; :;")
        time.sleep(0.2)
        print("         ;:::::'   :;")
        time.sleep(0.2)
        print("        ;:::::;     ;.")
        time.sleep(0.2)
        print("       ,:::::'       ;           OOO")
        time.sleep(0.2)
        print("       ::::::;       ;           OOOOO")
        time.sleep(0.2)
        print("       ;:::::;       ;           OOOOOO")
        time.sleep(0.2)
        print("      ,;::::::;     ;'         / OOOOOOO")
        time.sleep(0.2)
        print("      ;:::::::::`. ,,,;.      /  / DOOOOOO")
        time.sleep(0.2)
        print("    .';:::::::::::::::::;,   /  /     DOOOO")
        time.sleep(0.2)
        print("   ,::::::;::::::;;;;::::;, /  /        DOOO               You are neither dead or alive   ")
        time.sleep(0.2)
        print(";`::::::`'::::::;;;::::: ,#/  /          DOOO                  A fate worse than death      ")
        time.sleep(0.2)
        print(":`:::::::`;::::::;;::: ;::#  /            DOOO        And in this state you will remain for eternity  ")
        time.sleep(0.2)
        print("::`:::::::`;:::::::: ;::::# /              DOO                        And a day            ")
        time.sleep(0.2)
        print("`:`:::::::`;:::::: ;::::::#/               DOO")
        time.sleep(0.2)
        print(" :::`:::::::`;; ;:::::::::##                OO")
        time.sleep(0.2)
        print(" ::::`:::::::`;::::::::;:::#                OO")
        time.sleep(0.2)
        print("  :::::`::::::::::::;'`:;::#                O")
        time.sleep(0.2)
        print("   :::::`::::::::;' /  / `:#")
        time.sleep(0.2)
        print("  ::::::`:::::;'  /  /   `#")
        print("")
        time.sleep(2)
        print("you journy has ended")
        time.sleep(2)
        start_over = input ("would you like to try again [Y/N]:")
        if start_over == "y" or start_over == "Y":
            print("lets play".upper())
            start_level()
        elif start_over == "N" or start_over == "n": 
            print(" i though that would be you answer ".upper()) 
            end_game()
        else:
            print("Why do you proceed to test my patients!".upper())
            end_game() #change made by Kim to make game more logical

    ###################################################################

    def door_a_choosen():
        print("")
        time.sleep(2)
        print("hmmm... Door A the voice says")
        time.sleep(2)
        print("")
        print("     __________  ")
        time.sleep(0.3)
        print("   |  __ A __  | ")
        time.sleep(0.3)
        print("   | |  | |  | | ")
        time.sleep(0.3)
        print("   | |  | |  | | ")
        time.sleep(0.3)
        print("   | |__| |__| | ")  
        time.sleep(0.3)
        print("   |  __   __  | ") 
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | | ") 
        time.sleep(0.3)
        print("   | |__| |__| |  ")  
        time.sleep(0.3)
        print("   | __________|  ") 
        print("")
        print("wise choice")
        time.sleep(4)
        print("Or not! heckles the voice")
        time.sleep(2)
        print("You walk towards door A, you feel the engery of something strange")
        time.sleep(2)
        print("you pull open the door and are blinded by the light pulsing from the portal")
        time.sleep(2)
        print("you put a hand in  an are instanly engulfed by its engergy, your scared you close your eyes")
        time.sleep(2)
        print("suddenly you a feel calm, opening your eyes you realise you have been looped back to the gate keeper")
        time.sleep(2)
        print("I thought id be seeing you again says the gate keeper")
        time.sleep(2)
        print("In order to continue your journy you will have first choose a door")
        door_choice = input ("which door will you choose, which fate will you seek! [A, B, C or D]:")
        time.sleep(2)
        if door_choice == "A" or door_choice == "a":
            door_a_choosen()
        elif door_choice == "B" or door_choice == "b":
            door_b_choosen() 
        elif door_choice == "C" or door_choice == "c":
            door_c_choosen()
        elif door_choice == "D" or door_choice == "d":
            door_d_choosen()   
        else: 
            print("Why do you proceed to test my patients!".upper())
            end_game()
            

    ###################################################################
    def start_level():
        # global name
        # time.sleep(3)
        # print("you enter a strange room the likes of witch you have never seen before")
        # time.sleep(2)
        # print("Hello I have been expecting you for some time, A voice from the shadows mutters")
        # time.sleep(3)
        # print ("you step foward into the room and see what seems to be four large oak doors each with a unique glow")
        time.sleep(1)
        print("")
        print("     __________      __________        __________       __________  ")
        time.sleep(0.3)
        print("   |  __ A __  |    |  __ B __  |    |  __ C __  |    |  __ D __  | ")
        time.sleep(0.3)
        print("   | |  | |  | |    | |  | |  | |    | |  | |  | |    | |  | |  | | ")
        time.sleep(0.3)
        print("   | |  | |  | |    | |  | |  | |    | |  | |  | |    | |  | |  | | ")
        time.sleep(0.3)
        print("   | |__| |__| |    | |__| |__| |    | |__| |__| |    | |__| |__| | ")  
        time.sleep(0.3)
        print("   |  __   __  |    |  __   __  |    |  __   __  |    |  __   __  | ") 
        time.sleep(0.3)
        print("   | |  | |  | |    | |  | |  | |    | |  | |  | |    | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | |    | |  | |  | |    | |  | |  | |    | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | |    | |  | |  | |    | |  | |  | |    | |  | |  | | ")  
        time.sleep(0.3)
        print("   | |  | |  | |    | |  | |  | |    | |  | |  | |    | |  | |  | | ") 
        time.sleep(0.3)
        print("   | |__| |__| |    | |__| |__| |    | |__| |__| |    | |__| |__| | ")  
        time.sleep(0.3)
        print("   | __________|    | __________|    | __________|    | __________| ") 
        print("")
        print("In front of you is four doors, behind each door there is portal. A voice says")
        time.sleep(2)
        print("The voice explains that there are four portals one of which will lead you through to the next leg of you journy")
        time.sleep(2)
        print("Another two will lead you astray to an inevatable fate worse than death it's self! says the voice")
        time.sleep(2)
        print("The last door is a dimension loop that sumon you back to the gate keeper me! murmers the voice menacingly")
        time.sleep(2)
        print("")  
        print("                        /\    A ")
        time.sleep(0.2)
        print("                       /__\   I      O  o")
        time.sleep(0.2)
        print("                      //..\\   I     .")
        time.sleep(0.2)
        print("                      \].`[/  I")
        time.sleep(0.2)
        print("                      /l\/l\ (I    .  O")
        time.sleep(0.2)
        print("                     /. ~~ ,\/I          .               In order to continue your journy  ")
        time.sleep(0.2)
        print("                     \\L__j^\/ I       o                 You will have first choose a door")
        time.sleep(0.2)
        print("                      \/--v}  I     o   .")
        time.sleep(0.2)
        print("                      |    |  I   _________")
        time.sleep(0.2)
        print("                      |    |  I c(`       ')o")
        time.sleep(0.2)
        print("                      |    l  I   \.     ,/   ")   
        time.sleep(0.2)
        print("                    _/j  L l\_!  _//^---^\\_")
        time.sleep(0.2)
        print("                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                          GATE KEEPER")
        print("")
        # print("In order to continue your journy you will have first choose a door")
        door_choice = input ("which door will you choose, which fate will you seek! [A, B, C or D]:")
        time.sleep(2)
        if door_choice == "A" or door_choice == "a":
            door_a_choosen()
        elif door_choice == "B" or door_choice == "b":
            door_b_choosen() 
        elif door_choice == "C" or door_choice == "c":
            door_c_choosen()
        elif door_choice == "D" or door_choice == "d":
            door_d_choosen()   
        else: 
            print("Why do you proceed to test my patients!".upper())
            door_choice = input ("which door will you choose, which fate will you seek! [A, B, C or D]:")   
            time.sleep(2)
            if door_choice == "A" or door_choice == "a":
                door_a_choosen()
            elif door_choice == "B" or door_choice == "b":
                door_b_choosen() 
            elif door_choice == "C" or door_choice == "c":
                door_c_choosen()
            elif door_choice == "D" or door_choice == "d":
                door_d_choosen()   
            else: 
                print("Why do you proceed to test my patients!".upper())   
                end_game()

    start_level()
    ##################################################################

def Kim_Puzzle():
    print("You enter a room. There are four items on a table and four symbols on the far wall.")
    time.sleep(3)
    print("On the table are a ring with a red stone that seems to pulse with energy,")
    time.sleep(3)
    print("a bottle of what looks like water,")
    time.sleep(2)
    print("a beautiful green jewel the size of a fist,")
    time.sleep(2)
    print("and a silver and copper staff that crackles with magical power.")
    time.sleep(4)
    print()
    print("The symbols on the wall are in the shape of a golden sun,")
    time.sleep(3) 
    print("a pale crescent moon,")
    time.sleep(2)
    print("a green and verdant tree")
    time.sleep(2) 
    print("and a bird, black like a crow.")
    time.sleep(4)
    print()
    print("A voice speaks to you.")
    time.sleep(2)
    print("\033[1;35;40m \"Welcome to the Chamber of Elements!")
    time.sleep(2)
    print("Four items are on the table, four symbols on the wall and four elements that mark your fate.")
    time.sleep(4)
    print("Each of the items represents an element.")
    time.sleep(3)  
    print("\033[0;31;40m The ring is fire.  \033[1;33;40m The staff is air.  \033[0;34;40m The bottle contains water.  \033[1;32;40m The gemstone symbolises earth.")
    time.sleep(5)
    print("\033[1;35;40m You must choose which item to use on which symbol.")
    time.sleep(3)  
    print("Shoot with the ring and the staff.  Throw the bottle of water.  Place the gemstone.")
    time.sleep(5)
    print("Choose wisely.  Match up each item with each symbol correctly and the door to your exit will be revealed.")
    time.sleep(4)
    print("Make a mistake and something unpleasant will occur.\"")
    time.sleep(2)

    items = ["Ring", "Staff", "Jewel", "Bottle"]
    symbols = ["Sun", "Moon", "Tree", "Bird"]

    def element_room_complete():
        print()
        print("\033[0;37;40m The wall where the symbols were descends into the floor with a grinding noise of stone against stone.")
        time.sleep(4)
        print("This reveals the door that leads out of the room")
        time.sleep(3)
        print("The voice says \033[1;35;40m \"Well done.  You have opened the way.")
        time.sleep(3)
        print("Your exit is revealed.  You can now leave the Chamber of Elements.\" \033[0;37;40m")
        print("")
        time.sleep(2)
        print("Loading next puzzle...Please wait...")
        time.sleep(5)
        print("")
        James_Puzzle()

    def use_ring():
        print()
        use = input(f"\033[0;31;40m Which item do you want to use it on?  {', '.join(symbols)}? ")
        if use == "Sun" or use == "sun":
            print("You point the ring at the sun symbol.  Fire shoots out and hits it.")
            time.sleep(3)
            print("You hear a click.  The symbol fades into the grey stone.")
            time.sleep(3)
            print("The voice says \033[1;35;40m \"Well done.  You have opened the way of fire.\"")
            time.sleep(3)
            items.remove("Ring")
            symbols.remove("Sun")
            if len(items) == 0:
                element_room_complete()
            else:
                choose_item()
        elif use.capitalize() in symbols: 
            print(f"You point the ring at the {use.lower()} symbol.")
            time.sleep(2)
            print("The flames that shoot from the ring reflect off the symbol and hit you, scorching your skin.")
            time.sleep(4)
            print("\033[1;35;40m \"Try again,\" \033[0;31;40m says the voice with a sinister chuckle.")
            time.sleep(2)
            choose_item()
        else:
            print("Option not available.  Please choose from one of the symbols on the wall.")
            use_ring()
        

    def use_staff():
        print()
        use = input(f"\033[1;33;40m Which item do you want to use it on?  {', '.join(symbols)}? ")
        if use == "Bird" or use == "bird":
            print("You point the staff at the bird symbol.  Lightning shoots out and strikes it.")
            time.sleep(3)
            print("You hear a click.  The symbol fades into the grey stone.")
            time.sleep(3)
            print("The voice says \033[1;35;40m \"Well done.  You have opened the way of air.\"")
            time.sleep(3)
            items.remove("Staff")
            symbols.remove("Bird")
            if len(items) == 0:
                element_room_complete()
            else:
                choose_item()
        elif use.capitalize() in symbols:
            print(f"You point the staff at the {use.lower()} symbol.")
            time.sleep(2)
            print("The lightning that shoots from the ring reflects off the symbol and strikes back at you painfully.")
            time.sleep(4)
            print("\033[1;35;40m \"Try again,\" \033[1;33;40m says the voice with a sinister chuckle.")
            time.sleep(2)
            choose_item()
        else:
            print("Option not available.  Please choose from one of the symbols on the wall.")
            use_staff()

    def use_jewel():
        print()
        use = input(f"\033[1;32;40m Which item do you want to use it on?  {', '.join(symbols)}? ")
        if use == "Tree" or use == "tree":
            print("You place the gemstone into the tree symbol.  The symbol pushes back into the stone.")
            time.sleep(3)
            print("You hear a click.  Grey stone covers where the symbol once was.")
            time.sleep(3)
            print("The voice says \033[1;35;40m \"Well done.  You have opened the way of earth.\"")
            time.sleep(3)
            items.remove("Jewel")
            symbols.remove("Tree")
            if len(items) == 0:
                element_room_complete()
            else:
                choose_item()
        elif use.capitalize() in symbols:
            print(f"You place the gemstone into the {use.lower()} symbol.")
            time.sleep(2)
            print("Nothing happens.  The symbol pushes back for a second and then pops back out again.")
            time.sleep(4)
            print("The room shakes for a couple of minutes, as if from an earthquake.")
            time.sleep(4)
            print("\033[1;35;40m \"Try again,\" \033[1;32;40m says the voice with a sinister chuckle.")
            time.sleep(2)
            choose_item()
        else:
            print("Option not available.  Please choose from one of the symbols on the wall.")
            use_jewel()

    def use_bottle():
        print()
        use = input(f"\033[0;34;40m Which item do you want to use it on?  {', '.join(symbols)}? ")
        if use == "Moon" or use == "moon":
            print("You throw the bottle at the moon symbol.  It smashes against it and breaks.")
            time.sleep(3)
            print("You hear a click.  The symbol fades into the grey stone.")
            time.sleep(3)
            print("The voice says \033[1;35;40m \"Well done.  You have opened the way of water.\"")
            time.sleep(3)
            items.remove("Bottle")
            symbols.remove("Moon")
            if len(items) == 0:
                element_room_complete()
            else:
                choose_item()
        elif use.capitalize() in symbols:
            print(f"You throw the bottle at the {use.lower()} symbol.")
            time.sleep(2)
            print("The bottle smashes against the symbol and spills its contents but does not break.")
            time.sleep(4)
            print("Water sprinkles from the ceiling, drenching you utterly.  The bottle refills with water.")
            time.sleep(4)
            print("\033[1;35;40m \"Try again,\" \033[0;34;40m says the voice with a sinister chuckle.")
            time.sleep(2)
            choose_item()
        else:
            print("Option not available.  Please choose from one of the symbols on the wall.")
            use_bottle()


    def choose_item():
        print() 
        choice = input(f"\033[0;37;40m What item do you wish to use? ({', '.join(items)})? ")
        if choice == "R" or choice == "r" or choice == "ring" or choice == "Ring":
            if "Ring" in items:
                use_ring()
            else:
                print("You have already successfully used that item.  Please choose one of the others.")
                time.sleep(3)
                choose_item()
        elif choice == "S" or choice == "s" or choice == "staff" or choice == "Staff":
            if "Staff" in items:
                use_staff()
            else:
                print("You have already successfully used that item.  Please choose one of the others.")
                time.sleep(3)
                choose_item()
        elif choice == "W" or choice == "w" or choice == "water" or choice == "Water" or choice == "bottle" or choice == "Bottle" or choice == "water bottle" or choice == "Water Bottle" or choice == "Water bottle" or choice == "water Bottle":
            if "Bottle" in items:
                use_bottle()
            else:
                print("You have already successfully used that item.  Please choose one of the others.")
                time.sleep(3)
                choose_item()
        elif choice == "J" or choice == "j" or choice == "jewel" or choice == "Jewel" or choice == "gem" or choice == "Gem" or choice == "gemstone" or choice == "Gemstone" or choice == "stone" or choice == "Stone":
            if "Jewel" in items:
                use_jewel()
            else:
                print("You have already successfully used that item.  Please choose one of the others.")
                time.sleep(3)
                choose_item()
        else:
            print("Sorry but that option is not available.  Try again")
            choose_item()

    choose_item()

def Total_Game_Start():
    print("You wake up in a dark room, with no idea how you got there.")
    time.sleep(2)
    print("You lie there on the cold stone floor, before a mysterious voice calls out to you")
    time.sleep(2)
    print("\"I hope you're smarter than the last one we tested!\"")
    time.sleep(2)
    print("\"He never made it past the first chamber\"")
    time.sleep(2)
    print("\"If freedom is what you seek, then you must earn it!\"")
    time.sleep(2)
    print("\"Each Chamber has been designed by my colleagues to test your knowledge, wit, logic and memory...\"")
    time.sleep(4)
    print("\"Let us hope that you please them...\"")
    time.sleep(2)
    print("The voice fades away, and a door before you grinds open")
    time.sleep(2)
    print("revealing beyond it, a dark corridor that connects to the first chamber...")
    print("")
    time.sleep(2)
    print("Loading first puzzle...Please wait...")
    time.sleep(5)
    print("")
    Kim_Puzzle()

Total_Game_Start()
