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
先安裝 [googlempas](https://github.com/googlemaps/google-maps-services-python)

```python
pip install googlemaps
```

再來 import Finder class, 就能開始設定搜尋內容了
```python
from PlaceIDFinder import Finder
```

插入您的 Google Maps API key
```python
id_finder = Finder('Your API key')
```

設定 radar search 的搜尋半徑
```python
id_finder.setRadius(800)
```


