x = "There are %d types of people."
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! '%r'" % "hahaha i got you!!!"

print joke_evaluation

w = "This is the left side of ..."
e = "a string with a right side."

print w+e
