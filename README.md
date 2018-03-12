# PlaceID-Finder

利用簡單方法搜尋指定區域內的店家 Place ID, 搜尋方法是使用google map api的[雷達搜尋](https://developers.google.com/places/web-service/search?hl=zh-tw#RadarSearchRequests)

|Name|Description|
|----|----|
|PlaceIDFinder.py|店家Place ID爬蟲|

## Dependency
|Name|Version|
|----|----|
|googlemaps|2.5.1|

## Usage % Example
先安裝 [googlempas](https://github.com/googlemaps/google-maps-services-python)

```python
pip install googlemaps
```

再來 import Finder class, 就能開始設定搜尋內容了
```python
from PlaceIDFinder import Finder
```

插入您的 Google Maps API key, 並設定 radius, displacement,＜/br＞
start_location(西南座標), end_location(東北座標) #正方形走法
```python
id_finder = Finder(key='Your API key', radius=radar_search_radius, disp=coord_move_disp, type=place_type,
                   southwest_location=(start_lng, start_lat), northeast_location=(end_lng, end_lat))
```

修改&取得 radar search 的搜尋半徑(radius)
```python
id_finder.radius = 700
_radius = id_finder.radius
```

修改&取得 座標移動距離(displacement)
```python
id_finder.displacement = 0.06
_disp = id_finder.displacement
```



