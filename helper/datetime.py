
import calendar
import datetime
 
def convertUnixTime():
    date = datetime.datetime.now(datetime.UTC)
    utc_time = calendar.timegm(date.utctimetuple())
    return utc_time