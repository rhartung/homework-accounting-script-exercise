"""Print out all the melons in our inventory."""


from melons import melon_data


# def print_melon(name, seedless, price):
#     """Print each melon."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


for melon, data in melon_data.iteritems():
    print melon.upper()

    for data, value in data.iteritems():
        print "{}: {}".format(data, value)

    print "*" * 30
