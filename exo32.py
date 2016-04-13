the_count = [1, 2, 3, 4, 5 ]
fruits = ['apples', 'oranges', 'pears', 'abricots']
change = [1, 'pennies',2,'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "count : %d" % number

for fruit in fruits:
    print "fruit name : %s" % fruit

for i in change:
    print "data : %r" % i

elements = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

for i in elements :
    print "element was : %d" % i
