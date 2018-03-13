# PlaceID-Finder

利用簡單方法搜尋指定區域內的店家 Place ID, 搜尋方法是使用google map api的[雷達搜尋](https://developers.google.com/places/web-service/search?hl=zh-tw#RadarSearchRequests)

|Name|Description|
|----|----|
|PlaceIDFinder.py|店家Place ID爬蟲|

## Dependency
|Name|Version|
|----|----|
|googlemaps|2.5.1|

## Usage
先安裝 [googlempas](https://github.com/googlemaps/google-maps-services-python), 並下載 PlaceIDFinder.py

```python
pip install googlemaps
```

再來 import Finder class, 就能開始設定搜尋內容了
```python
from PlaceIDFinder import Finder
```

插入您的 Google Maps API key, 並設定 radius, displacement,</br>
start_location(西南座標), end_location(東北座標) #正方形對角走法
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

修改&取得 起點座標(southwest_location) 終點座標(northeast_location)
```python
id_finder.southwest_location = (22.669266, 120.341372)
_start_loc = id_finder.southwest_location  # return type is tuple

id_finder.northeast_location = (24.723396, 125.018303)
_end_loc = id_finder.northeast_location  # return type is tuple
```

修改&取得 搜尋店家類型(place_type)
```python
id_finder.place_type = 'restaurant'
_place_type = id_finder.place_type
```

執行搜尋並取得 place id總數(id_count), place id list(id_list)
```python
_id_count, _id_list = id_finder.run()

# 也可以在搜尋(run)完後, 直接取得
_id_count = id_finder.id_count()
_id_list = id_finder.id_list()
```

檢查資料有無輸入 或兩座標的輸入有無錯誤
```python
id_finder.check()
```

將 id_list 寫成txt儲存
```python
id_finder.write_to_txt('file_name')
```

## Example
以簡單例子作為範例, 搜尋區域以正方形方式下去搜尋 左下角(西南座標 A點)為起點, 右上角(東北座標 B點)為終點

```python

```

