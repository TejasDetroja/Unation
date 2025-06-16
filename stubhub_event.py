import json
import scrapy
import requests
from scrapy.cmdline import execute
from stubhub_event.items import stubhub_event
from scrapy.selector import Selector


class stubhub_event(scrapy.Spider):
    name = 'stubhub_event'

    def start_requests(self):

        urls = 'https://www.stubhub.com/explore?method=getExploreEvents&lat=NDAuNzEyOA%3D%3D&lon=LTc0LjAwNg%3D%3D&to=253402300799999&tlcId=2'
        yield scrapy.FormRequest(url=urls, callback=self.parse)

    def parse(self, response):

        Data_items_list = list()
        jsond = json.loads(response)
        for jd in jsond['events']:

            try:
                eventid = int(jd['eventId'])
            except Exception as e:
                eventid = ""
                print("Somethin want wron in event id", e)
            try:
                eventname = jd['name'].strip()
            except Exception as e:
                eventname = ""
                print("Somethin want wron in event name", e)
            try:
                url = jd['url']
            except Exception as e:
                url = ""
                print("Somethin want wron in event url", e)
            try:
                dayOfWeek = jd['dayOfWeek']
            except Exception as e:
                dayOfWeek = ""
                print("Somethin want wron in event dayOfWeek", e)
            try:
                formattedTime = jd['formattedTime']
            except Exception as e:
                formattedTime = ""
                print("Somethin want wron in event formattedTime", e)
            try:
                formattedDateWithoutYear = jd['formattedDateWithoutYear']
            except Exception as e:
                formattedDateWithoutYear = ""
                print("Somethin want wron in event formattedDateWithoutYear", e)

            venuelst = list()
            try:
                venueId = int(jd['venueId'])
            except Exception as e:
                venueId = ""
                print("Somethin want wron in event venueId", e)
            try:
                venueName = jd['venueName'].strip()
            except Exception as e:
                venueName = ""
                print("Somethin want wron in event venueName", e)
            try:
                formattedVenueLocation = jd['formattedVenueLocation']
            except Exception as e:
                formattedVenueLocation = ""
                print("Somethin want wron in event formattedVenueLocation", e)
            try:
                event_imageUrl = jd['imageUrl']
            except Exception as e:
                event_imageUrl = ""
                print("Somethin want wron in event imageUrl", e)
            try:
                priceClass = jd['priceClass']
            except Exception as e:
                priceClass = ""
                print("Somethin want wron in event priceClass", e)
            try:
                categoryId = jd['categoryId']
            except Exception as e:
                categoryId = ""
                print("Somethin want wron in event categoryId", e)
            venueitems = dict()
            venueitems['Venue_Id'] = venueId
            venueitems['Venue_Name'] = venueName
            venueitems['Venue_Location'] = formattedVenueLocation
            venuelst.append(venueitems)


            # items = QuotesItem()
            items = dict()
            items['Event_Id'] = eventid
            items['Event_Name'] = eventname
            items['Url'] = url
            items['Event_Day'] = dayOfWeek
            items['Event_time'] = formattedTime
            items['Event_Date'] = formattedDateWithoutYear
            items['Venue_Details'] = venuelst
            Data_items_list.append(items)
            # yield items

        # TODO :: End Code Here -------
        respo_dict =  dict()
        respo_dict['results'] = Data_items_list
        print(json.dumps(respo_dict))
        return respo_dict


if __name__ == '__main__':
    execute('scrapy crawl stubhub_event'.split())
