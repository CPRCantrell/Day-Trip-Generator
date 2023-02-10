import random as r

def main():
    print()

    #Initializing pre-set lists
    list_of_destinations = ["Atlanta", "Marietta", "Kennesaw", "Acworth", "Woodstock", "Dunwoody"]
    list_of_restaurants = ["Wendy's", "Sub-way", "Fogo de Chao", "Stoney River", "Rotating Sushi Bar"]
    list_of_entertainment = ["Concert", "Piedmont Park", "Centennial Park", "World of Coke", "Moive", "Georgia Aquarium", "Belt Line"]
    list_of_transportation = ["Car", "Bike", "Uber", "Marta", "Friend's Car"]
    master_list = [list_of_destinations, list_of_restaurants, list_of_entertainment, list_of_transportation]
    options_in_master_list = ["Destination", "Restaurant", "Entertainment", "Transportation"]

    #Picks a selection at random
    def select_random_choices(list_of_choices):
        return r.choice(list_of_choices)

    #Prints selection
    def display_selected_items(item, selected):
        print(f'{item} - {selected}')

    def verify_user_response():
        pass

    #collects user response
    def user_response(prompt, exceptable_responses = []):
        if len(exceptable_responses) != 0:
            response = "empty"
            print(f'{prompt}?')
            while True:
                print("Exceptable answers are [", end ="")
                for answer in exceptable_responses:
                    print(f"{answer}] ", end ="")
                response = input("Response: ")
                for answer in exceptable_responses:
                    if response.lower() == answer:
                        return answer
                    else:
                        print("Invalid Entry")

        return input(f'{prompt}: ')

    selections = []
    while True: 
        for lists in master_list:
            selections.append(select_random_choices(lists))

        print("Day Trip: ")
        for i in range(len(selections)):
            display_selected_items(options_in_master_list[i],selections[i])
        
        response = user_response("Would You like to take this trip or reroll",["yes", "no", "n","y"])
        if response == "yes" or response == 'y':
            break
    
    print("You have selected: ")
    for i in range(len(selections)):
        display_selected_items(options_in_master_list[i],selections[i])
    print("as your day plans!")

if __name__ == '__main__':
    main()