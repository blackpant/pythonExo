from sys import argv

#script, first, second, third = argv
try:
    while True:
        vava = raw_input("Tell me anything you want :")
        print vava
        if vava == "code" :
            exit(0)
except Exception:
    print "Erreur reessaye tu as pas le choix xD !!."

