# Practice: Dictionary of Words
# Creating an empty dictionary
my_dictionary = dict()

# 
my_dictionary["boondoggle"] = "erroneous or distracting task"
my_dictionary["truncated"] = "shorten (something) by cutting of the top or the end"
my_dictionary["succinct"] = "(especially of something written or spoken) briefly and clearly expressed."
my_dictionary["alabaster"] = "a fine-grained, translucent form of gypsum, typically white, often carved"
my_dictionary["Phencyclidine"] = "angel dust, mind altering substance"

for (key, value) in my_dictionary.items():
    print(f'{key}: {value}')