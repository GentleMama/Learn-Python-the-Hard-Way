my_name = 'Alan Yan'
my_age = 28 # not a lie
my_height = 179 # cm
my_weight = 70 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

cm_2_inches = 2.54
lb_2_kg = 2.2046226

print "Let's talk about %s." % my_name
print "He's %d cm( %d inches) tall." % (my_height, my_height / cm_2_inches)
print "He's %d kg( %d lb) heavy." % (my_weight, my_weight * lb_2_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print 'His teeth are usually %s depending on the coffee.' % my_teeth

# this line is tricky, try to get exactly right
print "if I add %d, %d, and %d I get %d." % (
        my_age, my_height, my_weight, my_age + my_height + my_weight)
