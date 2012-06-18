from bottle import route, run
from pprint import pprint
import pyicequery, json

@route('/icequery/:serveraddress/:serverport/:mountpoint')
def index(serveraddress, serverport, mountpoint):
    ret = pyicequery.get_server_details(serveraddress, serverport, mountpoint)
    pprint (ret)
    return json.dumps(ret)

@route('/icequery/:serveraddress/:serverport/:mountpoint/:item')
def index(serveraddress, serverport, mountpoint):
    return '<b>Hello %s!</b>' % serveraddress

run(host='109.104.118.84', port=8080)

