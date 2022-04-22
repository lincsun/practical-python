<<<<<<< HEAD
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
=======
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
>>>>>>> c3b3606b64174eb1de08a843a8ae3b06bdb6414d
