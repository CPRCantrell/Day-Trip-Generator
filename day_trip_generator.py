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
    def display_dictionary(dictionary: dict, prompt = None):
        if prompt != None:
            print(f'{prompt}')
        {print(f'{key} - {item}') for key, item in dictionary.items()}

    #Validate user input
    def verify_user_response(test, valid_input: dict):
        try: 
            return ([valid_input[key] for key in valid_input.keys() if key == test.lower()][0])
        except: 
            return verify_user_response(input(f'\nInvalid Entry \nExceptable answers are {list(valid_input.keys())}: '), valid_input)
    
    #Main system that runs program (Randomizes Selections)
    def day_trip_generator():
        selections = {key:r.choice(value) for (key,value) in master_dictionary.items()}

        display_dictionary(selections, '\nDay Trip: ')
        if verify_user_response(input('Do you want this list: '),{'yes': True, 'no': False}):
           display_dictionary(selections, '\nYou have selected The following as your plans:')
           return True
    return day_trip_generator()

if __name__ == '__main__':
    while True:
        if main() : break