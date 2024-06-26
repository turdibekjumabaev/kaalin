# Kaalin

<p>
    The string methods provided by the Python programming language are primarily tailored for English language usage, which might not seamlessly suit the needs of other languages such as Karakalpak. Consequently, to bridge this gap, you can employ this library to avail a range of functions specifically designed to accommodate the intricacies of the Karakalpak language. 
</p>

## Example
```python
from kaalin import Latin

kaa = Latin('BÁHÁR')

print(kaa.upper())      # BÁHÁR
print(kaa.lower())      # báhár
print(kaa.isupper())    # True
print(kaa.islower())    # False
print(kaa.isalpha())    # True
print(kaa.isdigit())    # False
```
```python
from kaalin import Number, NumberRangeError

kaa_num = Number()

try:
    print(kaa_num.to_word(533_525))         # bes júz otız úsh mıń bes júz jigirma bes
    print(kaa_num.to_word(894_236_671))     # segiz júz toqsan tórt million eki júz otız altı mıń altı júz jetpis bir
except NumberRangeError as e:
    print("San shegaradan asıp ketti!")
```
<br>

<p>
    <i>
        Kaalin is an open-source project, welcoming contributions and suggestions from anyone interested. Whether you're a seasoned developer or a newcomer, your input can help improve and expand the project's capabilities. Feel free to join the community, contribute code, suggest enhancements, or provide feedback to make Kaalin even better. Together, we can make a difference in empowering users with powerful tools and resources.
    </i>
</p>

[Contribute to the project](https://github.com/turdibekjumabaev/kaalin)