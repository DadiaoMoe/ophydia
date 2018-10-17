# Language Specifications

__Ophydia__ is inspired by __Vyper__, and simplified by removing _event_ and _@payable_. We may also support _struct-type contract arguments_ in the future.

## reserved keywords for type
| type in __equity__ | reserved keyword in __Ophydia__  | underlying type |
| - | - | - |
| Integer | integer | integer |
| Amount | amount | integer |
| Boolean | bool | boolean |
| String | string | string |
| Hash | hash | string |
| Asset | asset | string |
| PublicKey | publickey | string |
| Signature | signature | string |
| Program | program | string |

__TODO:__ support constant
```
TOTAL_SUPPLY: constant(integer) = 10000000
```

## builtin functions
+ `abs(n)` returns the absolute value of the value n.
+ `min(x, y)` returns the smallest of the two values ​​x and y.
+ `max(x, y)` returns the largest of the two values ​​x and y.
+ `size(s)` returns the size of any type of byte.
+ `concat(s1, s2)` returns the string generated from connecting the two strings s1 and s2
+ `concatpush(s1, s2)` concatenates two string-type virtual machine execution opcodes s1 and s2 (ie s2 is joined ​​behind s1) and pushes them onto the stack. The operation function is mainly used for nested contracts.
+ `below(height)` determines whether the current block height is lower than the parameter height, and returns true if it is, otherwise returns false.
+ `above(height)` determines whether the current block height is higher than the parameter height, and returns true if it is, otherwise returns false.
+ `sha3(s)` returns the hashing result of byte type string parameter s via SHA3-256.
+ `sha256(s)` returns the hashing result of byte type string parameter s via SHA-256
+ `check_tx_sig(key, sig)` verifies whether the multi-signature of the transaction is correct based on one PublicKey and one Signature.
+ `check_tx_multi_sig([key1, key2, …], [sig1, sig2, …])` verifies the multi-signature of the transaction is correct based on multiple PublicKeys and multiple Signatures.

