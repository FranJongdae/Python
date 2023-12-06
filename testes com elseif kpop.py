def kpop_calculator():
    print("Welcome to the Kpop Calculator!")
    like_kpop = input("Do you like Kpop? (yes/no): ").lower()

    if like_kpop == "yes":
        print("Nice, you are a Kpopper.")
        favorite_group = input("What is your favorite group? ")
        print(f"Oh, {favorite_group}?! I like it too!")
    elif like_kpop == "no":
        favorite_genre = input("What is your favorite genre of music? ")
        print(f"Oh, you like {favorite_genre}! That's cool.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        
kpop_calculator()