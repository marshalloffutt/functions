# 8-12

def make_sandwiches(*ingredients):
    """Summarize the sandwich we are about to make"""
    print("\nMaking a sandcwich with the following ingredients: ")
    for ingredient in ingredients:
        print("- " + ingredient)

make_sandwiches('jelly')
make_sandwiches('pork', 'lettuce', 'mustard')
make_sandwiches('peanut butter', 'pickles')