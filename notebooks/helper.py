from ipywidgets import *
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from tqdm.notebook import tqdm

# from https://github.com/germanesosa/ipywidget-autocomplete/blob/master/autoFill.py
def autoFill(opts=[''], val='',txt='',placehold='Please type here...',callback=False):
    opts.append('')
    def dropFunc(value):
        if (value.new in opts):
            dropClose()
            if (callable(callback)):
                callback(value) 
        text.value = value.new                
    def dropClose():
        drop.layout.visibility='hidden'
        selDropBox.layout.visibility='hidden'            
        selDropBox.layout.display='none'         
    def textFunc(value):
        matched = False
        if (len(value.new)>len(value.old)):
            # if (len(value.new)>2):
            word = value.new
            out = [word]
            for mystring in opts:
                if word.lower() in mystring.lower(): 
                    if (mystring.lower()==word.lower()):
                        matched = True
                    out.append(mystring)
            if (not matched):
                drop.layout.visibility='visible'
                selDropBox.layout.visibility='visible'
                selDropBox.layout.display='flex'
                out.append('')
                drop.options=out 
            else:
                dropClose()
        
    drop = Select(
                options=opts,
                value=val,
                rows=10,
                description=txt,
                disabled=False,
           )     
    text = Text(
                value=val,
                placeholder=placehold,
                description=txt,
                disabled=False,    
            )         
    drop.observe(dropFunc, names='value')
    text.observe (textFunc,names='value')
    selTextBox = Box([text])
    selDropBox = Box([drop], layout = Layout(display='none', top='-32px', visibility='hidden', flex_flow='column'))
    return (VBox([selTextBox, selDropBox],layout = Layout(display='flex', flex_flow='column'))) 


def query_address(parkruns):
    
    geolocator = Nominatim(user_agent="my_email@my_server.com")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries = 0, swallow_exceptions = True)

    locations = {}
    for parkrun in tqdm(parkruns.values):
        location1 = geocode(f'{parkrun} parkrun, Australia')

        if location1 is not None:
            locations[parkrun] = location1.address
            continue

        location2 = geocode(f'{parkrun}, Australia')
        if location2 is not None:
            locations[parkrun] = location2.address
            continue

        locations[parkrun] = None
    
    return locations


def get_state(parkrun, address):
    
    state_dict = {
        'Australian Capital Territory': 'ACT', 
        'New South Wales': 'NSW', 
        'Northern Territory': 'NT',
        'Queensland': 'QLD',
        'South Australia': 'SA', 
        'Tasmania': 'TAS',
        'Victoria': 'VIC',
        'Western Australia': 'WA'
    }
    
    if address is not None:
        for k, v in state_dict.items():
            if k in address:
                return v
    
    return input(f"Couldn't identify state for {parkrun}\nPlease look up what state {parkrun} is in:\n")
