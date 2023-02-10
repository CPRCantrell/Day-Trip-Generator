import random as r

def main():
    print()

    #Initializing pre-set lists
    list_of_destinations = ["Atlanta", "Marietta", "Kennesaw", "Acworth", "Woodstock", "Dunwoody"]
    list_of_restaurants = ["Wendy's", "Sub-way", "Fogo de Chao", "Stoney River", "Rotating Sushi Bar"]
    list_of_entertainment = ["Concert", "Piedmont Park", "Centennial Park", "World of Coke", "Moive", "Georgia Aquarium", "Belt Line"]
    list_of_transportation = ["Car", "Bike", "Uber", "Marta", "Friend's Car"]

    #Picks a selection at random
    def select_random_choices(list_of_choices):
        return r.choice(list_of_choices)



if __name__ == '__main__':
    main()