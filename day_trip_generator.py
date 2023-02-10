import random as r

def main():
    print()

    #Create Ditionary
    master_dictionary = {
        "Destination": ["Atlanta", "Marietta", "Kennesaw", "Acworth", "Woodstock", "Dunwoody"],
        "Restaurant": ["Wendy's", "Sub-way", "Fogo de Chao", "Stoney River", "Rotating Sushi Bar"],
        "Entertainment": ["Concert", "Piedmont Park", "Centennial Park", "World of Coke", "Moive", "Georgia Aquarium", "Belt Line"],
        "Transportation": ["Car", "Bike", "Uber", "Marta", "Friend's Car"]
    }
    selections = {}

    #Picks a selection at random
    def select_random_choice(list_of_choices):
        return r.choice(list_of_choices)

    #displays dictionary with key and value
    def display_dictionary(dictionary):
        for key, item in dictionary.items():
            print(f'{key} - {item}')

    def fill_dictionary(dictionary):
        new_dict = {key:select_random_choice(value) for (key,value) in dictionary.items()}
        return new_dict

    #Validate user input
    def verify_user_response(prompt, valid_input = {}):
        test = input(f"{prompt}: ").lower()
        value_test = list({key:value for (key,value) in valid_input.items() if key == test}.values())
        if len(value_test) > 0:
            return value_test[0]

        print()
        print("Invalid Entry")
        print(f"Exceptable answers are {list(valid_input.keys())}")
        verify_user_response(prompt, valid_input)
    
    #Main code
    while True:
        selections = fill_dictionary(master_dictionary)
        print("Day Trip: ")
        display_dictionary(selections)
        
        if verify_user_response("Do you want this list",{"yes": True, "no":False}):
            print()
            break

        print()
    
    print("You have selected: ")
    display_dictionary(selections)
    print("as your day plans!")
    print()

if __name__ == '__main__':
    main()