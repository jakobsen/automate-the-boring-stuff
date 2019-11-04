"""As a toy program, this simple traffic light procedure demonstrates
assertions that may save you from making simple errors when programming.
To run the program without checking the assertions, use the -O option
when calling python from the terminal.
"""

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switchLights(stoplight):
    assert 'red' in stoplight.values(), "Neither light is red!"
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'


print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)