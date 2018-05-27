# coding: utf-8
# @Time    : 2018/5/27
# @Author  : A1058420631
# @FileName: Location_bus.py
# @Software: pycharm

import requests
import json

network = open('Network_bus.txt', 'r')
location = open('Location_bus.txt', 'a')

line = network.readlines()
for i in line:
    number = str(i[4:7])
    # print(number)
    url = 'https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=210100&geoobj=123.346699%7C41.738768%7C123.621357%7C41.859828&keywords=' + number + '%E8%B7%AF'
    json_obj = requests.get(url)
    # print(json_obj.text)

    data = json_obj.json()
    if (data["data"]["message"]) and (data["data"]["busline_list"]):
        buslists = data["data"]["busline_list"]  # busline列表
        buslist = buslists[0]  # 选择方向


    # 公交站点
    def BusStations(buslist):
        busstation = []
        buslinename = buslist["name"]
        busstation.append(buslinename)
        stations = buslist["stations"]
        for station in stations:
            stationname = station["name"]
            stationxy = station["xy_coords"].split(";")
            busstation.append(stationname)
            busstation.append(stationxy)
        return busstation


    busstations = BusStations(buslist)
    location.writelines(str(busstations))
    location.writelines('\n')