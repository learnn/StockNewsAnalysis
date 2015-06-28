import csv
with open('test.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        symbol = row[0].split(",")[0]
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