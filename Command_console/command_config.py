#Based on example from https://stackoverflow.com/questions/53156009/coap-protocol-get-method-use-python
from coapthon.client.helperclient import HelperClient
from coapthon.messages.request import Request
from coapthon import defines

print('Enter the Sprinkler Controller IPv6 address:')
host = input('$')   #example: "fd01::c392:260:37ff:fe00:fa5d"
port = 5683
print('Enter the configuration URI')
print('"control_config" for sprinkler control')
print('"sampling" for changing sampling period')
path = input('$')
#path = "control_config"

if path == "control_config":
    print ('Enter the Sprinkler control command: MANUAL_ON, MANUAL_OFF or AUTO')
elif path == "sampling":
    print ('Enter the sampling period in ms:')    

payload = input ('$')

client = HelperClient(server=(host, port))
request = Request()
request.code = defines.Codes.POST.number
request.type = defines.Types['CON']
request.destination = (host, port)
request.uri_path = path
request.payload = payload
response = client.send_request(request)
print(response.pretty_print())
client.stop()
