# skcrackme_1 by sknine9

### https://crackmes.one/crackme/5ab77f5333c5d40ad448c0d9

Crackme made in Java, uses DES symmetric cipher algorithm (twice, with different initial secret keys). 
Crackme might be run using: `java -cp SKCrackMe.jar eu.sknine.skcrackme1.KClass`
Steps below describe algorithm in same order as in crackme, solution uses steps in reversed order.


```mermaid
graph LR
    A["get login"] ---> B["for each char delete -89, eg. 78 - (-89), create bytes array "]
    B --> C["using cipher DES and key 13248657 encrypt previously created bytes array"]
    C --> D["using cipher DES and key 13377331 encrypt once again bytes array, this time previously encrypted bytes array"]
    D --> E["Final bytes array is password (each number be separated by space)"]
```
