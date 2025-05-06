<h2>Code refactoring</h2>

Definition: The process of imporing code without creating new functionality that can turn a mess into a clean and simple design.
Risk: Changing code can unintentionally change functionality, so don't forget testing.

The objective is:
- the coude should be easy to read
- the naming should be clear and consistent 
- No copy paste code
- no hard coding (writing a value directly into the code itself)

Ideal process:
- First Time: Get it deployed
- Second: Take notes on pain and issues
- Third: Schedule Refactor Time
- Fourth: Learn through refactoring your own code



Example for refactoring:
**URL hardcoded**
```python
import requests

# Hard coded API URL és kulcs
url = "https://api.weather.com/data"
api_key = "12345-ABCDE"

response = requests.get(f"{url}?apikey={api_key}")
print(response.json())
```


**URL placed in a .env file**
```python
import requests
import os

url = os.getenv("API_URL")
api_key = os.getenv("API_KEY")

response = requests.get(f"{url}?apikey={api_key}")
print(response.json())
```
.evn:
```python
API_URL=https://api.weather.com/data
API_KEY=12345-ABCDE
```