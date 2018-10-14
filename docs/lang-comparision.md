# Comparisons between Equity & Ophydia

## RevealPreimage

__Equity__

```
contract RevealPreimage(hash: Hash) locks amount of asset {
  clause reveal(string: String) {
    verify sha3(string) == hash
    unlock amount of asset
  }
}
```

__Ophydia__

```
h: public(hash)

@public
def reveal(s: string):
    assert sha3(s) == h
    unlock() // TODO: seems doing nothing
```


## LoanCollateral

__Equity__

```
contract LoanCollateral(assetLoaned: Asset,
                        amountLoaned: Amount,
                        repaymentHeight: Integer,
                        lender: Program,
                        borrower: Program) locks collateral {
  clause repay() requires payment: amountLoaned of assetLoaned {
    lock payment with lender
    lock collateral with borrower
  }
  clause default() {
    verify above(repaymentHeight)
    lock collateral with lender
  }
}
```

__Ophydia__

```
asset_loaned: public(asset)
amount_loaned: public(amount)
repayment_height: public(integer)
lender: public(program)
borrower: public(program)

@public
def repay():
    # requires has been removed in equity
    # requires(amount_loaned, asset_loaned)
    lock_other_with(amount_loaned, asset_loaned, lender)
    lock_with(borrower)

@public
def default():
    assert above(repayment_height)
    lock_with(lender)
```


## AssignVar

__Equity__

```
contract TestAssignVar(result: Integer) locks valueAmount of valueAsset {
  clause LockWithMath(first: Integer, second: Integer) {
    define calculate: Integer = first
    assign calculate = calculate + second
    verify result == calculate
    unlock valueAmount of valueAsset
  }
}
```

__Ophydia__

```
result: public(integer)

@public
def lock_with_math(first: integer, second:integer):
    calculate = first
    calculate = calculate + second # TODO: `+=`
    assert result = calculte
    unlock()
```


## IfNesting

__Equity__

```
contract TestIfNesting(a: Integer, count:Integer) locks valueAmount of valueAsset {
  clause check(b: Integer, c: Integer, d: Integer) {
    verify b != count
    if a > b {
        if d > c {
           verify a > d
        }
        verify d != b
    } else {
        verify a > c
    }
    verify c != count
    unlock valueAmount of valueAsset
  }
  clause cancel(e: Integer, f: Integer) {
    verify a != e
    if a > f {
      verify e > count
    }
    verify f != count
    unlock valueAmount of valueAsset
  }
}
```

__Ophydia__

```
a: public(integer)
count: public(integer)

@public
def check(b: integer, c:integer, d: integer):
    assert b!= count
    if a > b:
        if d > c:
            assert a > d
        assert d != b
    else：
        assert a > c
    assert c != count
    unlock()

@public
def cancel(e: integer, f:integer):
    assert a != e
    if a > f:
        assert e > count
    assert f != count
    unlock()
```


## PriceChanger

__Equity__

```
contract PriceChanger(askAmount: Amount, askAsset: Asset, sellerKey: PublicKey, sellerProg: Program) locks valueAmount of valueAsset {
  clause changePrice(newAmount: Amount, newAsset: Asset, sig: Signature) {
    verify checkTxSig(sellerKey, sig)
    lock valueAmount of valueAsset with PriceChanger(newAmount, newAsset, sellerKey, sellerProg)
  }
  clause redeem() {
    lock askAmount of askAsset with sellerProg
    unlock valueAmount of valueAsset
  }
}
```

__Ophydia__

Ohydia doesn't not support recusive contract, and therefore is more secure (contract deployer cannot change the rules unless deploying a new contract).


## LockWith2of3Keys

__Equity__

```
contract LockWith3Keys(pubkey1, pubkey2, pubkey3: PublicKey) locks amount of asset {
  clause unlockWith2Sigs(sig1, sig2: Signature) {
    verify checkTxMultiSig([pubkey1, pubkey2, pubkey3], [sig1, sig2])
    unlock amount of asset
  }
}
```

__Ophydia__

```
pubkey1: public(publickey)
pubkey2: public(publickey)
pubkey3: public(publickey)

@public
def unlock_with_2sigs(sig1: signature, sig2: signature):
    assert check_tx_multi_sig([pubkey1, pubkey2, pubkey3], [sig1, sig2])
    unlock()
```


## TestConstantMath

__Equity__

```
contract TestConstantMath(result: Integer, hashByte: Hash, hashStr: Hash, outcome: Boolean) locks valueAmount of valueAsset {
  clause calculation(left: Integer, right: Integer, boolResult: Boolean) {
    verify result == left + right + 10
    verify hashByte == sha3(0x31323330)
    verify hashStr == sha3('string')
    verify !outcome
    verify boolResult && (result == left + 20)
    unlock valueAmount of valueAsset
  }
}
```

__Ophydia__

```
result: public(integer)
byte_hash: public(hash)
str_hash: public(hash)
outcome: public(boolean)

@public
def calculation(left: integer, right: integer, bool_result: boolean):
    assert result == left + right + 10
    assert byte_hash == sha3(0x31323330)
    assert str_hash == sha3('string')
    assert !outcome
    assert bool_result && (result == left + 20)
    unlock()
```
