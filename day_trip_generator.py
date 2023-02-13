import random as r

#Create Ditionary
master_dictionary = {
    "Destination": ["Atlanta", "Marietta", "Kennesaw", "Acworth", "Woodstock", "Dunwoody"],
    "Restaurant": ["Wendy's", "Sub-way", "Fogo de Chao", "Stoney River", "Rotating Sushi Bar"],
    "Entertainment": ["Concert", "Piedmont Park", "Centennial Park", "World of Coke", "Movie", "Georgia Aquarium", "Belt Line", "Atlanta Zoo"],
    "Transportation": ["Car", "Bike", "Uber", "Marta", "Friend's Car"]
}
months = {'January': 31,'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
#Choose selections at random
def select_random_option(dictionary: dict):
    return {key:r.choice(value) for (key,value) in dictionary.items()}

#displays dictionary with key and value w/ prompt
def display_dictionary(dictionary: dict, prompt = None):
    if prompt != None:
        print(f'{prompt}')
    for key, item in dictionary.items():
        print(key, end=' - ')
        if type(item) == dict:
            print()
            {print(f'\t{within_key}: {within_item}') for within_key, within_item in item.items()}
        else:
            print(item)

#Validate user input
def verify_user_response(test, valid_input: dict):
    try: 
        return ([valid_input[key] for key in valid_input.keys() if key == test.lower().replace(' ','')][0])
    except: 
        return verify_user_response(input(f'\nInvalid Entry \nExceptable Entry: {list(valid_input.keys())}: '), valid_input)

#Validate date input
def validate_date(date, data_needed: str):

    #verify date is long enough
    if validate_date_data(len(date.replace(' ','')),valid_length = len(data_needed)):

        #verify input are int
        try: month, day, year = [int(value) for value in date.split('/')]
        except: return validate_date_error(data_needed)

        #input is within range
        if validate_date_data(month, 12, 2):
            month = ([key for key in months.keys()][month - 1])
            if validate_date_data(len(str(year)), valid_length= 4):
                day_range = int([value for key,value in months.items() if key == month][0])
                if month == 'February' and year%4 == 0 : day_range += 1

                #date is in range for month
                while not validate_date_data(day,max_value= day_range):
                    try: day = int(input(f'\nIn the month of {month} date must be between 1 - {day_range}: '))
                    except: continue

                #return valid date
                return str(f'{month} {day}, {year}')
    return validate_date_error(data_needed)

def validate_date_data(data, max_value:int = None, valid_length:int = None):
    if valid_length == None:
        if 1<= data<= max_value:
            return True
    elif max_value == None:
        if 0<len(str(data)) <= valid_length:
            return True
    elif 0<len(str(data)) <= valid_length and 1<= data<= max_value:
        return True
    return False

#Error in date validation
def validate_date_error(data_needed):
    validate_date(input(f'\nInvadi Entery\nEntry must be put in as followed[{data_needed}]: '), data_needed)

    
#main Program
def main():
    #Plan / Save mutiple trips
    saved_plans = {}
    while True:
        #Query on day trip
        while True:
            selections = select_random_option(master_dictionary)
            display_dictionary(selections, '\nDay Trip: ')
            if verify_user_response(input('Would you like to save this trip: '),{'yes': True, 'no': False}):
                display_dictionary(selections, '\nYou have selected The following as your plans:')
                break       

        saved_plans[validate_date(input('To save these plans please provide a date (MM/DD/YYYY): '),'MM/DD/YYYY')] = selections
        if verify_user_response(input('\nWould you like to make plans for other days: '),{'yes': False, 'no': True}):
            break

    display_dictionary(saved_plans, '\nWhat you have planned!')
            
if __name__ == '__main__':
    main()