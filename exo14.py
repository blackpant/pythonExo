from sys import argv

#I add the Try/Except to the exercise.
try:
    script, user_name = argv
    prompt = '> '

    print "Hi %s, I'm the %s script." % (user_name, script)
    print "I'd like to ask you a few questions."
    print "Do you like me (yes/no)%s?" % user_name
    likes = raw_input(prompt)

    #I add to the exercise the yes or no part and the exit part if no is the response
    if likes == "no":
        print "OK , GoodBy So it was not a plesure...-_-"
        exit(0)

    print "Where do you live %s?" % user_name
    lives = raw_input(prompt)

    print "What kind of computer do you have?"
    computer = raw_input(prompt)

    print """
    Alright, so you said %r about liking me.
    You live in %r.  Not sure where that is.
    And you have a %r computer.  Nice.
    """ % (likes, lives, computer)

except Exception:
    print "Veulliez entrer votre non SVP!!!"
