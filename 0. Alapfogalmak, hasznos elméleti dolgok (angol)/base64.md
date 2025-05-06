<h2>Base64 encoding</h2> 

**What is base64?**
- a group of binary-to-text encoding schemes that transforms binary data into a sequence of printable characters, limited to a set of 64 unique characters. More specifically, the source binary data is taken 6 bits at a time, then this group of 6 bits is mapped to one of 64 unique characters.
- is a format designed to prevent communication mishaps during the transfer of binary information. 
<br>

![base64](img/base64.png)


**Process:**
- the data is converted to a stream of ASCII characters, which van then be transmitted and decoded
- the resultant string is always larger than the original (base64 is not a compression algorithm)
- it does not encrypt information - it encodes and decodes

**Uses:**
- encoding image/media data
- SSL certificates
- email transmissions
- virtually any transfer of information that requires special controll characters to be escaped
- store images in databases
- store binary data in json or xml

**Example:**
- go to your browser and search for images in google
- if you hover over pictures and inspect it with the elements section in developer tools you will see something like this:
```html
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAnsB9tFWiGUAAAAASUVORK5CYII=" alt="Transparent PNG">
```


This can be done in python easily:
```python
import base64

with open("example.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode("utf-8")
    print(f'data:image/png;base64,{encoded}')
```


The character set is built on having 6 places and 64 comes from all the variants we can have with this many 