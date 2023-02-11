import random as r

def main():
    #Create Ditionary
    master_dictionary = {
        "Destination": ["Atlanta", "Marietta", "Kennesaw", "Acworth", "Woodstock", "Dunwoody"],
        "Restaurant": ["Wendy's", "Sub-way", "Fogo de Chao", "Stoney River", "Rotating Sushi Bar"],
        "Entertainment": ["Concert", "Piedmont Park", "Centennial Park", "World of Coke", "Moive", "Georgia Aquarium", "Belt Line"],
        "Transportation": ["Car", "Bike", "Uber", "Marta", "Friend's Car"]
    }

    #displays dictionary with key and value w/ prompt
    def display_dictionary(prompt, dictionary):
        print(f"{prompt}")
        for key, item in dictionary.items():
            print(f'{key} - {item}')

    #Validate user input
    def verify_user_response(prompt, valid_input = {}):
        test = input(f"{prompt}: ").lower()
        value_test = list({key:value for (key,value) in valid_input.items() if key == test}.values())
        if len(value_test) > 0:
            return value_test[0]

        print(f"\nInvalid Entry \nExceptable answers are {list(valid_input.keys())}")
        verify_user_response(prompt, valid_input)
    
    #Main code
    def run_system():
        selections = {key:r.choice(value) for (key,value) in master_dictionary.items()}
        
        display_dictionary("\nDay Trip:", selections)
        if verify_user_response("Do you want this list",{"yes": True, "no":False}):
           display_dictionary("\nYou have selected The following as your plans:", selections)
        else:
            run_system()

    run_system()

if __name__ == '__main__':
    main()