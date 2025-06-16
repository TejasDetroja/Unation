import json
import requests


class stubhub_event:

        def __init__(self):
            self.id_no = 0  # Initialize a counter (currently unused)
            stubhub_event.first_requests(self)  # Call the method to start fetching data

        def first_requests(self):
            # URL for the StubHub API with encoded latitude and longitude parameters
            urls = 'https://www.stubhub.com/explore?method=getExploreEvents&lat=NDAuNzEyOA%3D%3D&lon=LTc0LjAwNg%3D%3D&to=253402300799999&tlcId=2'
            
            # HTTP headers including user-agent, cookies, and referer for simulating a browser request
            headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,hi;q=0.8,gu;q=0.7',
                'content-type': 'application/json',
                'priority': 'u=1, i',
                'referer': 'https://www.stubhub.com/explore?lat=NDAuNzEyOA%3D%3D&lon=LTc0LjAwNg%3D%3D&to=253402300799999&tlcId=2&from=0',
                'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
                'Cookie': '<LARGE_COOKIE_STRING>'  # Cookie string used to simulate a logged-in session
            }

            # Sending GET request to StubHub with verification disabled
            response = requests.get(url=urls, headers=headers, verify=False)
            
            # Wrapping response text into a dict and passing to next method
            meta = {'data': response.text}
            self.data(meta)

        def data(self, meta):
            # Extract JSON string from meta dictionary
            response_data = meta['data']

            Data_items_list = list()  # Initialize list to hold all event data
            jsond = json.loads(response_data)  # Parse JSON string into Python dict

            # Loop over each event object in the JSON
            for jd in jsond['events']:

                # Safely extract all required event fields with error handling
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

                venuelst = list()  # List to store venue details

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

                # Creating dictionary for venue and appending to list
                venueitems = dict()
                venueitems['Venue_Id'] = venueId
                venueitems['Venue_Name'] = venueName
                venueitems['Venue_Location'] = formattedVenueLocation
                venuelst.append(venueitems)

                # Creating dictionary to hold all event info
                items = dict()
                items['Event_Id'] = eventid
                items['Event_Name'] = eventname
                items['Url'] = url
                items['Event_Day'] = dayOfWeek
                items['Event_time'] = formattedTime
                items['Event_Date'] = formattedDateWithoutYear
                items['Venue_Details'] = venuelst

                # Append the event item to the main list
                Data_items_list.append(items)

            # Final result dictionary with all event data
            respo_dict = dict()
            respo_dict['results'] = Data_items_list

            # Print the JSON output
            print(json.dumps(respo_dict))
            return respo_dict


if __name__ == '__main__':
    stubhub_event()  # Instantiate the class to run the whole process
