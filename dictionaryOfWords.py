# Practice: Dictionary of Words
# Creating an empty dictionary
my_dictionary = dict()

# 
my_dictionary["boondoggle"] = "erroneous or distracting task"
my_dictionary["truncated"] = "shorten (something) by cutting of the top or the end"
my_dictionary["succinct"] = "(especially of something written or spoken) briefly and clearly expressed."
my_dictionary["alabaster"] = "a fine-grained, translucent form of gypsum, typically white, often carved"
my_dictionary["Phencyclidine"] = "angel dust, mind altering substance"

print(my_dictionary['truncated'], my_dictionary['succinct'])

for (key, value) in my_dictionary.items():
    print(f"The Definition of {key}: is {value}")

# End of Practice One
# Practice: English Idioms

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for a in idioms:
    print(a, idioms[a])