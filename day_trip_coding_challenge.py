import random as r

while "yes" != input('\nHow about this for your day trip?\n'+
    str({key2:r.choice(value2) for (key2,value2) in 
        {
            "Destination": ["Atlanta", "Marietta", "Kennesaw", "Acworth", "Woodstock", "Dunwoody"], 
            "Restaurant": ["Wendy.s", "Sub-way", "Fogo de Chao", "Stoney River", "Rotating Sushi Bar"], 
            "Entertainment": ["Concert", "Piedmont Park", "Centennial Park", "World of Coke", "Movie", "Georgia Aquarium", "Belt Line", "Atlanta Zoo"], 
            "Transportation": ["Car", "Bike", "Uber", "Marta", "Friend.s Car"]
            }.items()
        }.items()
    )[13:-3].replace(" (","").replace("),","\n").replace(",",":").replace("\"","").replace("'","").replace(".","'")
+"\nWhat do you think [Yes, No]: ") : continue