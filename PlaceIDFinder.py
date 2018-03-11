import googlemaps


class Finder:
    def __init__(self, user_key):
        self.gmaps = googlemaps.Client(key=user_key)
        self.radius = -1
        self.cord_moving = -1  # distance for coordinate to move
        self.start_lng = -1
        self.southwest_lng = -1
        self.southwest_lat = -1
        self.northeast_lng = -1
        self.northeast_lat = -1
        self.place_id_count = 0
        self.place_id_str = ""
        self.place_type = ""

    def setRadius(self, _radius):
        self.radius = _radius

    def setCoordinateMoveDistance(self, distance):
        self.cord_moving = distance

    def setSouthwestPosition(self, lng, lat):
        self.start_lng = lng
        self.southwest_lng = lng
        self.southwest_lat = lat

    def setNortheastPosition(self, lng, lat):
        self.northeast_lng = lng
        self.northeast_lat = lat

    def setPlaceType(self, type):
        self.place_type = type

    def getPlaceIDCount(self):
        return self.place_id_count

    def getPlaceIDType(self):
        return self.place_type
    
    def getPlaceIDList(self):
        return self.place_id_str.split('\n')

    def check(self):
        if self.radius <= 0 or self.cord_moving <= 0:
            print("error : you didn't set radius or coordinate move distance")
            return False
        elif (self.southwest_lng > self.northeast_lng) or \
             (self.southwest_lat > self.northeast_lat):
            print("error : There’s an error in your coordinate set")
            return False
        elif not self.place_type:
            print("error : you didn't set place type")
            return False
        else:
            return True

    def run(self):
        tmp_count = 0
        tmp_lng = self.southwest_lng
        tmp_lat = self.southwest_lat
        checker = self.check()
        while(checker):
            radar_result = self.gmaps.places_radar((tmp_lng, tmp_lat),
                                                   self.radius,
                                                   type=self.place_type)

            # 判斷results裡有無東西
            if len(radar_result['results']) > 0:
                for place in radar_result['results']:
                    if self.place_id_str.find(place['place_id']) == -1:  # 無重複
                        self.place_id_str += place['place_id'] + '\n'
                        tmp_count = tmp_count + 1
                        print('(' + str(tmp_lng) + ', ' +
                              str(tmp_lat) + '), PlaceID count=' +
                              str(tmp_count))

            if tmp_lat < self.northeast_lat:  # 判斷是否超出 最東 緯度
                if tmp_lng < self.northeast_lng:  # 判斷是否超出 最北 經度
                    tmp_lng = tmp_lng + self.cord_moving
                else:  # tmp_lng > northeast_lng 超出 最北 經度
                    tmp_lng = self.start_lng  # 恢復起始的 經度(初始化)
                    tmp_lat = tmp_lat + self.cord_moving
            else:  # tmp_lat >= northeast_lat 超出 最東 緯度
                self.place_id_count = tmp_count
                print('Search END')
                checker = False  # 結束search

    def writeToTxt(self, file_name):
        fileObject = open('./'+file_name+'.txt', 'w')
        fileObject.write(self.place_id_str)
        fileObject.close()
        print('Write END')
