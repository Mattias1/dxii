import mapparser

def main():
    """The main entrypoint for this application"""
    print('Loading data for map 27')
    m = mapparser.MapParser.fromURL('http://dominating12.com/lib/ajax/api/map-info.php?map_id=27')
    print('Loaded the map:', m.name)
    for v in m.territories.values():
        print(v.name, 'at', v.x, ',', v.y)

if __name__ == '__main__':
    main()