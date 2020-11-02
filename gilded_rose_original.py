# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 1 and item.quality < 50:
                    item.quality = item.quality + 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 11 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 6 and item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 1:
                    item.quality = item.quality - item.quality
            else:
                if item.quality > 0:
                    item.quality = item.quality - 1
                if item.sell_in < 1 and item.quality > 0:
                    item.quality = item.quality - 1
            item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
