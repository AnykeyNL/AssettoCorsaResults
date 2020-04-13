import os
import json

resultdir = "/Users/richard/Downloads/results/"
trackname = "zandvoort_f1"
webpage = "index.html"

practice = []
qualify = []
race = []

def MakeHead():
    txt = ""
    txt = "<html><head><title>Race results</title></head>"
    txt = txt + "<body>"
    return txt

def MakeClose():
    txt = ""
    txt = "</body></html>"
    return txt


def MakeTable(rdata):
    print ("making table")
    txt = "<table>"
    txt = txt + "<tr><th align=left>Time</th><th align=left>Racer</th><th align=left>Car</th><th align=left>Date</th></tr>"
    for i in rdata:
        min = int(int(i[0])/60000)
        sec = int((int(i[0])-min*60000)/1000)
        milsec = int((int(i[0])-min*60000)-sec*1000)
        timetxt = "{}:{}.{}".format(min,sec,milsec)
        txt = txt + "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(timetxt, i[1], i[2], i[3])
    txt = txt + "</table>"
    return txt

for resultfile in os.listdir(resultdir):
    print (resultfile)
    with open(resultdir + resultfile) as json_file:
        data = json.load(json_file)
        print (data['TrackName'])
        if data['TrackName'] == trackname:
            dateinfo = resultfile.split("_")
            datetext = "{}-{}-{} {}:{}".format(dateinfo[2],dateinfo[1],dateinfo[0],dateinfo[3],dateinfo[4])
            print (datetext)
            print (data['Type'])
            for r in data['Result']:
                if data['Type'] == "PRACTICE":
                    if r['BestLap'] != 999999999:
                        practice.append([r['BestLap'], r['DriverName'], r['CarModel'], datetext])
                if data['Type'] == "QUALIFY":
                    if r['BestLap'] != 999999999:
                        qualify.append([r['BestLap'], r['DriverName'], r['CarModel'], datetext])
                if data['Type'] == "RACE":
                    if r['BestLap'] != 999999999:
                        race.append([r['BestLap'], r['DriverName'], r['CarModel'], datetext])

practice.sort()
qualify.sort()
race.sort()

f = open(webpage, "w")
f.write(MakeHead())
f.write("<h1>{}<h1>".format(trackname))

f.write("<h1>RACE<h1>")
f.write(MakeTable(race))
f.write("<h1>QUALIFY<h1>")
f.write(MakeTable(qualify))
f.write("<h1>PRACTICE<h1>")
f.write(MakeTable(practice))



f.write(MakeClose())
f.close()






