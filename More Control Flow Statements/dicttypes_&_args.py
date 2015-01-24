def dictionary_and_args_list(*arguements, **dictionary_def_list):
    print("list of arguements")
    for arg in arguements:
        print(arg)
    print("\n")
    keys = dictionary_def_list.keys()




















    ++++++++
    for arg2 in keys:
        print(arg2, ":", keys[arg2])
	
dictionary_and_args_list("hi", "bambi", "doodle", shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")
