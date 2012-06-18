import urllib2
from bs4 import BeautifulSoup

def get_server_details(server, port, mount):
    server = "http://%s:%s/status.xsl?mount=/%s" % (server, port, mount)
    print "Getting info for %s" % (server)
    try:
        response = urllib2.urlopen(server)
        html = response.read()
        if html:
            soup = BeautifulSoup(html)

            info = {}
            info['stream_title'] = soup.find(text="Stream Title:").findNext('td').contents[0]
            info['stream_description'] = soup.find(text="Stream Description:").findNext('td').contents[0]
            info['content_type'] = soup.find(text="Content Type:").findNext('td').contents[0]
            info['mount_started'] = soup.find(text="Mount started:").findNext('td').contents[0]
            info['quality'] = soup.find(text="Quality:").findNext('td').contents[0]
            info['current_listeners'] = soup.find(text="Current Listeners:").findNext('td').contents[0]
            info['peak_listeners'] = soup.find(text="Peak Listeners:").findNext('td').contents[0]
            info['stream_genre'] = soup.find(text="Stream Genre:").findNext('td').contents[0]
            info['stream_url'] = soup.find(text="Stream URL:").findNext('td').findNext('a').contents[0]
            info['current_song'] = soup.find(text="Current Song:").findNext('td').contents[0]

            return info 
        else:
            print "Invalid content found"
            return None

    except urllib2.URLError:
        print "Unable to read url, please check your parameters"
        return None
get_server_details("localhost", "8000", "live")
