# coding=utf-8
from django.utils import timezone
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
        parsed = json.loads(output, object_pairs_hook=OrderedDict)
#        print parsed['retVal']['0001']['mday'], "\n"
#        print parsed['retVal']['0001']['mday'].encode('utf-8'), "\n"
        for i, val in parsed['retVal'].iteritems():
            print val
            sno = val['sno'].encode('utf-8')
            sna = val['sna'].encode('utf-8')
            sarea = val['sarea'].encode('utf-8')
            lat = val['lat'].encode('utf-8')
            lng = val['lng'].encode('utf-8')
            ar = val['ar'].encode('utf-8')
            sareaen = val[u'sareaen'].encode('utf-8')
            snaen = val[u'snaen'].encode('utf-8')
            aren = val[u'aren'].encode('utf-8')
            tot = val[u'tot'].encode('utf-8')
            sbi = val[u'sbi'].encode('utf-8')
            mday = val[u'mday'].encode('utf-8')
            bemp = val[u'bemp'].encode('utf-8')
            act = val[u'act'].encode('utf-8')
            print mday
            print type(mday)
            
            mday_parsed = datetime.datetime.strptime(mday, "%Y%m%d%H%M%S")

            c = station.objects.filter(sno__startswith=sno)
            if c is None:
                a = station(0, sno, sna, sarea, lat, lng, ar, sareaen, snaen, aren)
                a.save()

            b = info(0, sno, tot, sbi, mday_parsed, bemp, act)
            b.save()
            d = info.objects.filter(mday__gt=datetime.date.today())
            d.delete()
#        print type(parsed)
        threading.Timer(5, test).start()

test()
