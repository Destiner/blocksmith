# blocksmith
The goal of this library is to generate private Bitcoin keys. 

```
pip install blocksmith
```

## Usage
```python
import blocksmith

kg = blocksmith.KeyGenerator()
kg.seed_input('Truly random string. I rolled a dice and got 4.')
key = kg.generate_key()
print(key)
# 7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00

```
