from zeep import Client
from zeep.transports import Transport
from zeep.exceptions import Fault

#input County and Town parameters
County = raw_input('Please enter the county. For example: West Yorkshire ')
Town = raw_input('Please enter a town name to verify does it match the county. For example: Leeds ')

def Webservice_Test():
    # UK location webservice
    client = Client('http://www.webservicex.net/uklocation.asmx?WSDL')

    try:
        result = client.service.GetUKLocationByCounty(County)
        # Print the result
        print('It returns ' + str(result))
        # Verify the result
        assert Town in result, 'The input town does not match the result.'
        print('Pass. The town is included in the same county.')
    except Fault as exc:
        print(exc.message)

Webservice_Test()
