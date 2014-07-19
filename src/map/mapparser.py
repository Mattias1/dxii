import json
import urllib.request

class MapParser():
    @staticmethod
    def fromURL(url):
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return MapParser.fromJSON(response)

    @staticmethod
    def fromJSON(fp):
        obj = json.load(fp)

        mapObj = Map(obj['map_id'], obj['name'], obj['width'], obj['height'], obj['url'])

        for i, v in enumerate(obj['territories']):
            t = Territory(v['id'], v['name'], v['x'], v['y'])
            mapObj.addTerritory(t)

        for i, v in enumerate(obj['connections']):
            tFrom = mapObj.getTerritoryByID(v['from'])
            tTo = mapObj.getTerritoryByID(v['to'])
            tFrom.addConnection(tTo)

        return mapObj