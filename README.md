# blocksmith
The goal of this library is to generate private keys and create Bitcoin and Ethereum wallet addresses from them.

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

key = '7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00'

address = blocksmith.BitcoinWallet.generate_address(key)
print(address)
# 1JUP2bjfVexDif2m5fgyjHFrV9FE494REN

```

### Create Ethereum wallet from a private key
```python
import blocksmith

key = '7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00'

address = blocksmith.EthereumWallet.generate_address(key)
print(address)
# 0x1269645a46a3e86c1a3c3de8447092d90f6f04ed

checksum_address = blocksmith.EthereumWallet.checksum_address(address)
print(checksum_address)
# 0x1269645a46A3e86c1a3C3De8447092D90f6F04ED

```
