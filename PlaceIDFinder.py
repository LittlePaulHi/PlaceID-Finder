import googlemaps


class Finder:
    def __init__(self, key=None, radius=None, disp=None, type=None,
                 southwest_location=None, northeast_location=None):

        if not key:
            raise ValueError("API key is required")

        # start location(coordinate)
        if southwest_location and isinstance(southwest_location, tuple):
            self.start_lng = southwest_location[0]
            (self.southwest_lng, self.southwest_lat) = southwest_location
        else:
            self.start_lng = self.southwest_lng = self.southwest_lat = None

        # end location(coordinate)
        if northeast_location and isinstance(northeast_location, tuple):
            (self.northeast_lng, self.northeast_lat) = northeast_location
        else:
            self.northeast_lng = self.northeast_lat = None

        self.gmaps = googlemaps.Client(key=key)
        self._radius = radius  # radius for radar search
        self._coord_moving = disp  # displacement for coordinate to move
        self._place_type = type
        self.place_id_count = 0
        self.place_id_str = ""

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if isinstance(radius, str):
            self._radius = int(radius)
        else:
            self._radius = radius

    @property
    def displacement(self):
        return self._coord_moving

    @displacement.setter
    def displacement(self, disp):
        if isinstance(disp, str):
            self._coord_moving = float(disp)
        else:
            self._coord_moving = disp

    @property
    def southwest_coord(self):
        return (self.southwest_lng, self.southwest_lat)

    @southwest_coord.setter
    def southwest_coord(self, location):
        if isinstance(location, tuple):
            self.start_lng = location[0]
            (self.southwest_lng, self.southwest_lat) = location
        else:
            raise TypeError("Location type must be tuple")

    @property
    def northeast_coord(self):
        return (self.northeast_lng, self.northeast_lat)

    @northeast_coord.setter
    def northeast_coord(self, location):
        if isinstance(location, tuple):
            (self.northeast_lng, self.northeast_lat) = location
        else:
            raise TypeError("Location type must be tuple")

    @property
    def place_type(self):
        return self._place_type

    @place_type.setter
    def place_type(self, type):
        if isinstance(type, str):
            self._place_type = type
        else:
            raise TypeError("place type must be string")

    def id_count(self):
        return self.place_id_count

    def id_list(self):
        return self.place_id_str.split('\n')

    def check(self):
        if not (self._radius and self._coord_moving):
            raise ValueError("You didn't set radius or "
                             "coordinate move displacement")
        elif not (self.southwest_lng and self.southwest_lat):
            raise ValueError("You didn't set southwest location")
        elif not (self.northeast_lng and self.northeast_lat):
            raise ValueError("You didn't set northeast location")
        elif (self.southwest_lng > self.northeast_lng) or \
             (self.southwest_lat > self.northeast_lat):
            raise ValueError("There’s an error in your coordinate sets")
        elif not self._place_type:
            raise ValueError("You didn't set the place type")

    def run(self):
        self.check()
        tmp_count = 0
        tmp_lng = self.southwest_lng
        tmp_lat = self.southwest_lat

        while(True):
            radar_result = self.gmaps.places_radar((tmp_lng, tmp_lat),
                                                   self._radius,
                                                   type=self._place_type)

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
                    tmp_lng = tmp_lng + self._coord_moving
                else:  # tmp_lng > northeast_lng 超出 最北 經度
                    tmp_lng = self.start_lng  # 恢復起始的 經度(初始化)
                    tmp_lat = tmp_lat + self._coord_moving
            else:  # tmp_lat >= northeast_lat 超出 最東 緯度
                self.place_id_count = tmp_count
                print('Search END')
                break  # 結束search

    def write_to_txt(self, file_name):
        fileObject = open('./'+file_name+'.txt', 'w')
        fileObject.write(self.place_id_str)
        fileObject.close()
        print('Write END')
