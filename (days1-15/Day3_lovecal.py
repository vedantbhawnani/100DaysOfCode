def lovecal():
    p1 = input(("What's your name?")).lower()
    p2 = input(("Who's your crush?")).lower()
    true = 0
    love = 0
    check1 = ['l', 'o', 'v', 'e']
    check2 = ['t', 'r', 'u', 'e']
    for char in p1:
        if char in check1:
            love += 1
        if char in check2:
            true += 1
    for char in p2:
        if char in check1:
            love += 1
        if char in check2:
            true += 1
    loveScore = int(str(love)+str(true))
    if (loveScore < 10) or (loveScore > 90):
        print(
            f"Your love score is {loveScore}, you go together like coke and sprite.")
    elif (loveScore <= 60) or (loveScore >= 40):
        print(f"Your love score is {loveScore}, you are alright together.")
    else:
        print(f"Your score is {loveScore}")

lovecal()
