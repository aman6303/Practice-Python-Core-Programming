## Master Table of Python Built-ins

| Function | Purpose | Core Behavior | Inputs | Output | Exceptions | Perf Notes |
|---------|----------|---------------|--------|---------|------------|------------|
| abs() | Numeric normalization | Returns absolute value | number | number | TypeError | O(1) |
| all() | Boolean consensus | True if all items truthy | iterable | bool | TypeError | Linear |
| any() | Boolean detection | True if any item truthy | iterable | bool | TypeError | Short-circuit |
| ascii() | Escape formatter | Returns escaped representation | object | str | — | O(n) |
| bin() | Binary encoder | Converts int → binary | int | str | TypeError | O(log n) |
| bool() | Boolean coercion | Converts value to bool | any | bool | — | O(1) |
| bytearray() | Mutable bytes | Creates mutable byte array | bytes/iterable/int | bytearray | ValueError | O(n) |
| bytes() | Immutable bytes | Creates bytes object | bytes/iterable/int | bytes | ValueError | O(n) |
| callable() | Callability test | Checks if object callable | object | bool | — | O(1) |
| chr() | Unicode lookup | Codepoint → character | int | str | ValueError | O(1) |
| classmethod() | Class-level binding | Converts fn → class method | function | method | — | O(1) |
| compile() | Code compilation | Converts source → bytecode | src, mode | code | SyntaxError | High cost |
| complex() | Complex builder | Creates complex number | real, imag | complex | ValueError | O(1) |
| delattr() | Delete attribute | Removes attribute | obj, name | None | AttributeError | O(1) |
| dict() | Dict initializer | Creates dictionary | mapping/iterable | dict | — | O(n) |
| dir() | Introspection | Lists attributes | object | list | — | O(n) |
| divmod() | Div + mod | Returns quotient & remainder | a, b | tuple | TypeError | O(1) |
| enumerate() | Indexed generator | Yields (index, value) | iterable | iterator | — | O(1) |
| eval() | Expression execution | Evaluates string as expression | string | any | Many | Risky |
| exec() | Code execution | Runs dynamic Python code | string | None | Many | Risky |
| filter() | Predicate filter | Filters items via function | fn, iterable | iterator | — | Linear |
| float() | Float coercion | Converts to float | any | float | ValueError | O(1) |
| format() | Value formatting | Applies format spec | value, format_spec | str | — | O(n) |
| frozenset() | Immutable set | Creates frozenset | iterable | frozenset | TypeError | O(n) |
| getattr() | Attribute getter | Reads attribute | obj, name | any | AttributeError | O(1) |
| globals() | Global namespace | Returns globals dict | — | dict | — | O(1) |
| hasattr() | Attribute check | True if object has attr | obj, name | bool | — | O(1) |
| hash() | Hash value | Returns hash | obj | int | TypeError | O(1) |
| help() | Help viewer | Launches help() | object | screen | — | Slow |
| hex() | Hex encoder | Converts int → hex | int | str | TypeError | O(log n) |
| id() | Identity | Memory address ID | obj | int | — | O(1) |
| input() | User input | Reads console input | prompt | str | EOFError | IO-bound |
| int() | Int coercion | Converts to int | any | int | ValueError | O(n) |
| isinstance() | Type check | Checks object type | obj, type | bool | TypeError | O(1) |
| issubclass() | Inheritance check | Validates subclass | cls, base | bool | TypeError | O(1) |
| iter() | Iterator builder | Converts to iterator | object | iterator | TypeError | O(1) |
| len() | Size metric | Returns length | object | int | TypeError | O(1) |
| list() | List constructor | Creates list | iterable | list | TypeError | O(n) |
| locals() | Local namespace | Returns locals dict | — | dict | — | O(1) |
| map() | Transform pipeline | Applies fn across iterable | fn, iterable | iterator | — | Linear |
| max() | Max value | Largest element | iterable | value | ValueError | O(n) |
| min() | Min value | Smallest element | iterable | value | ValueError | O(n) |
| memoryview() | Zero-copy view | Creates memory view | obj | mv | TypeError | O(1) |
| next() | Iterator step | Returns next item | iterator | value | StopIteration | O(1) |
| object() | Base object | Creates base object | — | object | — | O(1) |
| oct() | Octal encoder | int → oct string | int | str | TypeError | O(log n) |
| open() | File opener | Opens files | path, mode | file | OSError | IO-bound |
| ord() | Codepoint lookup | char → codepoint | char | int | TypeError | O(1) |
| pow() | Power | Computes power (mod optional) | a, b, mod | number | ValueError | O(log n) |
| print() | Output writer | Prints data | values | None | — | IO-bound |
| property() | Managed attribute | Creates property | fget,fset,fdel | property | — | O(1) |
| range() | Sequence generator | Zero-cost numeric range | start,stop,step | range | ValueError | O(1) |
| repr() | Official string | Developer representation | obj | str | — | O(n) |
| reversed() | Reverse iterator | Iterates backward | seq | iterator | — | O(1) |
| round() | Rounding | Rounds float | number, ndigits | number | — | O(1) |
| set() | Mutable set | Creates set | iterable | set | TypeError | O(n) |
| setattr() | Attribute setter | Adds/updates attribute | obj, name, value | None | — | O(1) |
| slice() | Slice descriptor | Creates slice | start,stop,step | slice | — | O(1) |
| sorted() | Sorting engine | Returns sorted list | iterable | list | TypeError | O(n log n) |
| staticmethod() | Static binding | Declares static method | fn | method | — | O(1) |
| str() | String builder | Converts to string | any | str | — | O(n) |
| sum() | Aggregation | Sums items | iterable | number | TypeError | Linear |
| super() | Parent proxy | Calls parent methods | type, obj | super | — | O(1) |
| tuple() | Immutable sequence | Creates tuple | iterable | tuple | — | O(n) |
| type() | Type access/creation | Gets type or builds class | obj / args | type | TypeError | O(1) |
| vars() | Namespace accessor | Returns __dict__ | obj | dict | TypeError | O(1) |
| zip() | Parallel iterator | Zips iterables | iterables | iterator | — | Linear |
| __import__() | Import hook | Low-level import | name, globals | module | ImportError | Rare |
