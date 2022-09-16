#this is overnest, a code that uses nested loops to make a full list of every single digit in any based
#as defined by the user. A beginner's project, but making it was fun and i like it, so its here.
r = 1
print("Welcome to overnest, made by tanuki!")
# no clue why i ask it first, just did things in the same order i remenbered them
try:
    r = int(input("use all numbers as equal or select each one individually?(0/1): "))
except: #in case of error, it will guess that it is 1 and keep going.
    print("im gonna take that as a 1 [ERR1]")
# it will ask for a diplay mode
try :
        ii = int(input("full, short or spaced? 0/1/2: "))
except:
    print("YOU FOOKING BASTARD [ERR2]")
# then will ask for the numbers to nest
# if the awnser up there is 0, it will just skip this
# turns out that using anything bigger than 3 in any of the digits it probably just fill the comand line
# to a point where you cant even se the first command
if r == 1:
    try:
        ia = int(input("first: "))
        ib = int(input("second: "))
        ic = int(input("third: "))
        id = int(input("fourth: "))
        ig = int(input("last: "))
    except:
        print("wtf u doin [ERR3]")
# if the awnser was 0
elif r == 0:
    try:
        ee = int(input("number: "))
        ia = ee
        ib = ee
        ic = ee
        id = ee
        ig = ee
    except:
        print("legit how [ERR4]")
else:
    print("lmao [ERR7]")
# this is the actual nest. i used "ig" after the "id" bcs its hard to deal with "if" as a variable
try:
    for iaa in range(ia):
        for ibb in range(ib):
            for icc in range(ic):
                for idd in range(id): 
                    for igg in range(ig): # if you know a better way to do this pls tell me
                        if ii == 0:
                            print("first at " + str(iaa) + " second at " + str(ibb) + " third at " + str(icc) + " fourth at " + str(idd) + " last at " + str(igg)) # l o n g
                        elif ii == 2:
                            print(iaa, ibb, icc, idd, igg) # 0, 2, 1. the perfect "if" order
                        elif ii == 1:
                            print(str(iaa)+str(ibb)+str(icc)+str(idd)+str(igg))
                        else:
                            print("bruh, wtf [ERR6]")
except:
    print("you fooked up [ERR5]")
    # yes i know my error reports are stupidly ineficient
print("done!")
