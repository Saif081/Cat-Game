cat_attributes = {
    "Hunger": 100,
    "intelligence": 10,
    "energy": 100,
    "weight": 12,
    # change the inital values above
}

# Take the user inputs for name and colour:
name = input("Enter name: ")
colour = input("What colour is your cat: ")
print ("{name} is")
print (colour)
# ...
# start the while loop
while True:
    # Finish the string below
    option = input(f"What would you like to do? 1. Play with {name} 2. Train {name} 3. Feed {name} 4. show {name}'s stats")

    if option == '1':
        cat_attributes["energy"] = cat_attributes["energy"] - 5
        cat_attributes["Hunger"] = cat_attributes["Hunger"] - 5
        print(f"{name} has lost 5 energy and hunger points")
        pass
    
    elif option == '2':
        cat_attributes["intelligence"] += 5
        cat_attributes["energy"] = cat_attributes["energy"] - 5
        print(f"{name} has gained 5 intelligence points bhut has lost 5 energy points")
        pass
    
    elif option == '3':
        cat_attributes["Hunger"] = 100
    
    elif option == '4':
        print(f"Intellgience: {cat_attributes['intelligence']}\nWeight: {cat_attributes['weight']}\nEnergy: {cat_attributes['energy']}")
    
    else:
        print("Invalid option\n{name} is now sad)")

        pass

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        print(f"{name} has passed away due to fatal insomnia")
        break
    elif cat_attributes["energy"] < 30:
        sleep = input(f"{name} is now tired, would you like ot put {name} to sleep? y/n")
        if sleep.lower() == 'y':
            cat_attributes["energy"] = 100
