from Shoe import Shoe
cont = "Y"
while cont == "Y" or cont == "y":
    id = input("Shoe ID: ")
    brand = int(input("Choice Brand: [1:Puma 2:Reebok 3:Convers 4:Adidas 5:Nike]"))
    if brand == 1:
        myBrand = "Puma"
        model = int(input("Choice Model: [1:Batman Suede 2:Basket Classic 3:Pokemon Rider 4:Minecraft]"))
        if model == 1:
            myModel = "Batman Suede"
        elif model == 2:
            myModel = "Basket Classic"
        elif model == 3:
            myModel = "Pokemon Rider"
        elif model == 4:
            myModel = "Minecraft"
        else:
            print("Input Wrong")
    elif brand == 2:
        myBrand = "Reebok"
        model = int(input("Choice Model: [1:Turbo Restyle 2:Zig Kinetica 3:GL 1000 4:Flexagon Force]"))
        if model == 1:
            myModel = "Turbo Restyle"
        elif model == 2:
            myModel = "Zig Kinetica"
        elif model == 3:
            myModel = "GL 1000"
        elif model == 4:
            myModel = "Flexagon Force"
        else:
            print("Input Wrong")
    elif brand == 3:
        myBrand = "Converse"
        model = int(input(
            "Choice Model: [1:Chuck Taylo All Star 2:Jack Purcell 3:Star Life Clean 4:Point Star 5:Star in Black Youth]"))
        if model == 1:
            myModel = "Chuck Taylo All Star"
        elif model == 2:
            myModel = "Jack Purcell"
        elif model == 3:
            myModel = "Star Life Clean"
        elif model == 4:
            myModel = "Point Star"
        elif model == 5:
            myModel = "Star in Black Youth"
        else:
            print("Input Wrong")
    elif brand == 4:
        myBrand = "Adidas"
        model = int(input("Choice Model: [1:Neo 2:Stan Smith Lux 3:Forum Low 4:Run Falcon]"))
        if model == 1:
            myModel = "Neo"
        elif model == 2:
            myModel = "Stan Smith Lux"
        elif model == 3:
            myModel = "Forum Low"
        elif model == 4:
            myModel = "Run Falcon"
        else:
            print("Input Wrong")
    else:
        myBrand = "Nike"
        model = int(input("Choice Model: [1:Air Force 2:Air Max Lux 3:Retro GTS 4:Free Run]"))
        if model == 1:
            myModel = "Air Force"
        elif model == 2:
            myModel = "Air Max"
        elif model == 3:
            myModel = "Retro GTS"
        elif model == 4:
            myModel = "Free Run"
        else:
            print("Input Wrong")

    myShoe = Shoe(id,myBrand,myModel)
    print(myShoe)

    cont = input("Add More?[Y/N]: ")
