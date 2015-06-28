f = open("symbols_db.txt", "r")

lines = f.readlines()

items = []

for line in lines:
    it = line.split(",")[1]
    if it not in items:
        items.append(it)

for i in items:
    symbol = i
    print "========================="
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2015"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2014"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2013"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2012"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2011"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2010"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2009"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2008"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2007"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2006"
    print "http://www.moneycontrol.com/mccode/news/searchresult.php?str=" + symbol + "&durationType=Y&Year=2005"