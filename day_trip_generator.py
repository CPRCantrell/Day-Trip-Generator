import random as r

def main():
    #Create Ditionary
    master_dictionary = {
        "Destination": ["Atlanta", "Marietta", "Kennesaw", "Acworth", "Woodstock", "Dunwoody"],
        "Restaurant": ["Wendy's", "Sub-way", "Fogo de Chao", "Stoney River", "Rotating Sushi Bar"],
        "Entertainment": ["Concert", "Piedmont Park", "Centennial Park", "World of Coke", "Movie", "Georgia Aquarium", "Belt Line", "Atlanta Zoo"],
        "Transportation": ["Car", "Bike", "Uber", "Marta", "Friend's Car"]
    }

    #displays dictionary with key and value w/ prompt
    def display_dictionary(prompt, dictionary):
        print(f"{prompt}")
        for key, item in dictionary.items():
            print(f'{key} - {item}')

    #Validate user input
    def verify_user_response(test, valid_input):
        try: 
            return ([valid_input[key] for key in valid_input.keys() if key == test.lower()][0])
        except: 
            return verify_user_response(input(f"\nInvalid Entry \nExceptable answers are {list(valid_input.keys())}: "), valid_input)
    
    #Main system that runs program
    def run_system():
        selections = {key:r.choice(value) for (key,value) in master_dictionary.items()}

        display_dictionary("\nDay Trip: ", selections)
        if verify_user_response(input("Do you want this list: "),{"yes": True, "no": False}):
           display_dictionary("\nYou have selected The following as your plans:", selections)
           return True
    return run_system()

if __name__ == '__main__':
    while True:
        if main() : break