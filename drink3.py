import func
import os
import time


# for continue of third drink option and first mini-game 
def brownhairwoman():
    print(" You glace to the left and see a mob group of passengers.....\n \n In that group a heavyset lady with long flowing brown hair harrasses the luggage works with spewing insults sharp enough to take a life, \n\n“My Louis Vuitton does NOT belong next to some peasant’s Walmart duffel!!!!!” she shrieks, waving her manicured claws like she’s directing a Broadway musical called Misery on the High Seas. \n\nThe luggage boy — a poor passenger-volunteer roped into “helping” because he wanted early access to the buffet — looks like he’s reconsidering every life choice since birth.\n\nThe rest of the passengers pile on. A man insists his golf clubs are “emotional support equipment.” Another woman declares her suitcase has her “medication,” though the tequila scent suggests the prescription is 80-proof.\n\nFrom the back of the mob, someone bellows: “JUST LET US TO THE BUFFET!” and the crowd surges like a zombie horde chasing meatloaf.\n\nThe brown-haired woman pauses, narrows her eyes, and spots you.\n\n“What are you staring at? Think this is funny?”\n \nYou do. But also, you value your kneecaps..")       
    time.sleep(20)
    os.system('cls' if os.name == 'nt' else 'clear')



    while True:
        user_passenger = input(" You decide too... \n 1.) Be the hero for some damn reason \n 2.) become the buffet ninja (a.k.a stealth lvl 1: hungry rat.) \n 3.) BEAT THAT DAMN WOMAN TO A PULP! HOW DARE SHE TALK TO YOU LIKE THAT!!!!!\n").lower() 
      # continue handling user_passenger here
      # e.g.
        if user_passenger == "1":
            #help with bag problem
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You chose to be the hero.")
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(2)
            print(".")
            print("Just giving you a reminder that you aren't THAT special")
            break
        elif user_passenger == "2":
          #sneak into buffet
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You chose to become the buffet ninja. WHACHOWW")
            break
        elif user_passenger == "3":
          #fight the woman
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You chose to... go full berserk..  heh...")
            
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("cmon that CLEARLY isn't an option. Lets try to at least use 1% of our brain, hm?")




# calling brownhairwoman func for story to start at the end ---->
def drink3():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("You give the tour guide a sour look and choke out a clearly sarcastic \"Thank You..\" ") 
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  print("He quickly hums in response while turning his back to you, continuing his rant before hand about the ship and everything inside it.") 
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  print("You honestly could care less considering that EVERYONE,including the passengers by the way, got map handouts of the entire ship.") 
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  print("You dont even know why there was a tour guide to begin with; especially for, what you thought at least, was each person...")
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  print("After about two hours of endless chit-chatter, you are finally released from the tour guide and his so-called \"help\" ")
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  brownhairwoman()
