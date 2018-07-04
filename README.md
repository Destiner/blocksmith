# blocksmith
The goal of this library is to generate private keys and create Bitcoin wallet addresses from them.

```
pip install blocksmith
```

## Usage

### Generate a private key
```python
import blocksmith

kg = blocksmith.KeyGenerator()
kg.seed_input('Truly random string. I rolled a dice and got 4.')
key = kg.generate_key()
print(key)
# 7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00

```

### Create Bitcoin wallet from a private key
```python
import blocksmith

wallet = blocksmith.BitcoinWallet.generate_address(key)
print(wallet)
# 19ybJVKdJLwgy9kZnDwccg6QNNZBGbwrKa

```
