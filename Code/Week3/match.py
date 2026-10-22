weather = "rainy"

match weather:
    case "sunny":
        print("Good for date!")
    case "rainy":
        print("You need an umbrella")
    case _:
        print("incorrect input")
    
