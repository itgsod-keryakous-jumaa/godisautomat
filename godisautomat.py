# -*- coding: utf-8 -*-
print "1 choklad 10kr"
print "2 festis 8 kr"
print "nummer for onskad vara"
nr= int(raw_input(">>>"))

if nr== 1:
    produkt = "choklad"
    summakostnad = 10
    print "betala 10 kr"



elif nr== 2:
    produkt = "festis"
    summakostnad = 8
    print "betala 8 kr"
else:
    print "ditt nummer ar fel"

#check if number is  valid

#mata in pengar

print "betala for varan"
kr= int(raw_input(">>>"))

if kr == summakostnad:
    print "tack för kopet"
elif kr < summakostnad:
    print "tyvarr for lite pengar"
else:
    print "tack tack"




#kolla om pengar motsvarar varans kostnad



#too much

#print tack tack

# for lite pengar

#tyvarr

#exakt

#tack