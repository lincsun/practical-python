# Where is My Bus
#
# exercise 1.4

if __name__ == '__main__':
    import urllib.request

    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
    from xml.etree.ElementTree import parse

    doc = parse(u)

    for pt in doc.findall('.//pt'):
        print(pt.text)
