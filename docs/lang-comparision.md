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
    requires(amount_loaned, asset_loaned)
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
```
ask_amount: public(amount)
ask_asset: public(asset)
seller_key: public(publickey)
seller_prog: public(program)

@public
def change_price(new_amount: amount, new_asset: asset, sig: signature):
    assert check_tx_sig(seller_key, sig)
    lock_with() #####

@public
def redeem():
    lock_other_with(ask_amount, ask_asset, seller_prog)
    unlock()
```
