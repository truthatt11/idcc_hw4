# coding=utf-8
import time, threading
import json
import datetime
import urllib
from types import *
import gzip
from collections import OrderedDict
from map.models import station, info 

#gzip -d -f < youbike > youbike.txt
#aa = datetime.datetime.strptime(mday, "%Y%m%d%H%M%S")
def test():
    urllib.urlretrieve('http://data.taipei/youbike', 'youbike.gz');
    with gzip.open('youbike.gz', 'r') as f:
        output = f.read()
        parsed = json.loads(output, object_pairs_hook=OrderedDict);
#        print parsed['retVal']['0001']['mday'], "\n"
#        print parsed['retVal']['0001']['mday'].encode('utf-8'), "\n"
        for i, val in parsed['retVal'].iteritems():
#            print val
            zsno = val['sno'].encode('utf-8')
            zsna = val['sna'].encode('utf-8')
            zsarea = val['sarea'].encode('utf-8')
            zlat = val['lat'].encode('utf-8')
            zlng = val['lng'].encode('utf-8')
            zar = val['ar'].encode('utf-8')
            zsareaen = val[u'sareaen'].encode('utf-8')
            zsnaen = val[u'snaen'].encode('utf-8')
            zaren = val[u'aren'].encode('utf-8')
            ztot = val[u'tot'].encode('utf-8')
            zsbi = val[u'sbi'].encode('utf-8')
            zmday = val[u'mday'].encode('utf-8')
            zbemp = val[u'bemp'].encode('utf-8')
            zact = val[u'act'].encode('utf-8')
#            print zmday
#            print type(zmday)
            
            mday_parsed = datetime.datetime.strptime(zmday, "%Y%m%d%H%M%S")

            c = station.objects.filter(sno__startswith=zsno)
            if not c:
                print "c is", c
                a = station(sno=zsno, sna=zsna, sarea=zsarea, lat=zlat, lng=zlng, ar=zar, sareaen=zsareaen, snaen=zsnaen, aren=zaren)
                a.save()

            b = info(sno=zsno, tot=ztot, sbi=zsbi, mday=mday_parsed, bemp=zbemp, act=zact)
            b.save()
            d = info.objects.filter(mday__lt=datetime.date.today())
            d.delete()
#        print type(parsed)
    threading.Timer(5, test).start()

test()
