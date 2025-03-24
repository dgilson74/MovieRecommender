#Dictionary which stores genres as keys and 5 recommendations per key as values.
films_by_genre = {"Action": [("The Dark Knight", 9.0, "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman, James Gordon and Harvey Dent must work together to put an end to the madness."), ("The Lord of the Rings: The Return of the King", 9.0, "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring."), ("Inception", 8.8, "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster."), ("The Matrix", 8.7, "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence."), ("Star Wars: Episode V - The Empire Strikes Back", 8.7, "After the Empire overpowers the Rebel Alliance, Luke Skywalker begins his Jedi training with Yoda. At the same time, Darth Vader and bounty hunter Boba Fett pursue his friends across the galaxy.")], "Comedy": [("The Truman Show", 8.2, "An insurance salesman is oblivious of the fact that his entire life is a TV show and his family members are mere actors. As he starts noticing things and uncovers the truth, he decides to escape."), ("The Big Lebowski", 8.1, "Jeff 'The Dude' Lebowski, mistaken for a millionaire of the same name, seeks restitution for his ruined rug and enlists his bowling buddies to help get it."), ("Deadpool & Wolverine", 8.0, "Deadpool is offered a place in the Marvel Cinematic Universe by the Time Variance Authority, but instead recruits a variant of Wolverine to save his universe from extinction."), ("Groundhog Day", 8.0, "A narcissistic, self-centered weatherman finds himself in a time loop on Groundhog Day."), ("The Hangover", 7.7, "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.")], "Drama": [("The Shawshank Redemption", 9.3, "A banker convicted of uxoricide forms a friendship over a quarter century with a hardened convict, while maintaining his innocence and trying to remain hopeful through simple compassion."), ("Pulp Fiction", 8.9, "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."), ("Fight Club", 8.8, "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more."), ("Forrest Gump", 8.8, "The history of the United States from the 1950s to the '70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart."), ("Interstellar", 8.7, "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.")], "Horror": [("Alien", 8.5, "After investigating a mysterious transmission of unknown origin, the crew of a commercial spacecraft encounters a deadly lifeform."), ("The Shining", 8.4, "A family heads to an isolated hotel for the winter, where a sinister presence influences the father into violence. At the same time, his psychic son sees horrifying forebodings from both the past and the future."), ("The Thing", 8.2, "A research team in Antarctica is hunted by a shape-shifting alien that assumes the appearance of its victims."), ("Saw", 7.6, "Two men awaken to find themselves on the opposite sides of a dead body, each with specific instructions to kill the other or face consequences. These two are the latest victims of the Jigsaw Killer."), ("The Cabin in the Woods", 7.0, "A group of kids go to a remote cabin in the woods where their fate is unknowingly controlled by technicians as part of a world-wide conspiracy where all horror movie clichés are revealed to be part of an elaborate sacrifice ritual.")], "Sci-Fi": [("The Prestige", 8.5, "After a tragic accident, two stage magicians in 1890s London engage in a battle to create the ultimate illusion while sacrificing everything they have to outwit each other."), ("Back to the Future", 8.5, "Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown."), ("V for Vendetta", 8.1, "In a future British dystopian society, a shadowy freedom fighter, known only by the alias of 'V', plots to overthrow the tyrannical government - with the help of a young woman."), ("The Martian", 8.0, "An astronaut becomes stranded on Mars after his team assume him dead, and must rely on his ingenuity to find a way to signal to Earth that he is alive and can survive until a potential rescue."), ("Gravity", 7.7, "Dr Ryan Stone, an engineer on her first time on a space mission, and Matt Kowalski, an astronaut on his final expedition, have to survive in space after they are hit by debris while spacewalking.")] , "Thriller": [("Seven", 8.6, "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives."), (" The Silence of the Lambs", 8.6, "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims."), ("Shutter Island", 8.2, "Teddy Daniels and Chuck Aule, two US marshals, are sent to an asylum on a remote island in order to investigate the disappearance of a patient, where Teddy uncovers a shocking truth about the place."), ("Gone Girl", 8.1, "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent."), ("Donnie Darko", 8.0, "After narrowly escaping a bizarre accident, a troubled teenager is plagued by visions of a man in a large rabbit suit who manipulates him to commit a series of crimes.")]}

#Makes it easy to grab a specific genre from the dictionary
genres = [genre for genre in films_by_genre.keys()]

def user_genre():
    response_found = False
    while response_found != True:
        response = input("\nWhich genre of movie would you like recommendations for? Type the first letter of the genre to receive recommendations if they exist.\n\n")
        if response == "quit":
            goodbye()
            exit()
    #The next couple of lines would need changed if multiple genres have the same starting letter
        for genre in genres:
            if genre[0] == response.upper():
                response_found = True
                response = str(genre)
    
        if response_found == True:
            available_genre = input(f"\n{response} is the only movie genre we have recommendations for that matches your choice. Is {response} the genre you wish to explore? \n\nEnter 'y' for Yes or 'n' for No\n\n")
            if available_genre == "y":
                return response
            elif available_genre == "quit":
                goodbye()
                exit()
            else:
                response_found = False
                print("Let's try this again.")
        else:
            print("\nThere are no matching movie genres!\n")
            print("The available genres are :\n")
            for genre in genres:
                print(genre)
                print()
            
def welcome():
    print("______________________________________________________")
    print("\nWelcome to your #1 source for movie recommendations!\n\nWe hope you find some excellent movies to watch!\nEnter 'quit' to leave the application at any time.")

def more_recommendations():
    valid = False
    while valid == False:
        more_rec = input("\nDo you want more recommendations?\n\nEnter 'y' for Yes or 'n' for No\n\n")

        if more_rec == "y":
            return True
        
        elif more_rec == "n":
            return False
        
        elif more_rec == "quit":
            goodbye()
            exit()

        else:
            print("\nInvalid choice.")

    

def goodbye():
    print("\nThanks very much for using the film recommendation service. Goodbye!")

def present_recommendations(user_choice):
    choice = user_choice

    print("\nHere are the movie recommendations:\n ")

    count = 0

    for film in films_by_genre[choice]:
        count += 1
        print()
        print(f"Movie Title {count}- " + str(film[0]))
        print("Viewer Rating - " + str(film[1]))
        print("________________________________________")
    
    film_num = input("\nTo see a brief description of a film type the movie title number: \n\n")
    if film_num == "quit":
        exit()

    print("\n"+ films_by_genre[choice][int(film_num) - 1][2])

def main_app():
  welcome()
  more = True

  while more:
      user_choice = user_genre()
      present_recommendations(user_choice)
      more = more_recommendations()
  goodbye()


main_app()
