# Number and Types - We all used to be same.

Types in Flow basiclly same as llvm.

## Integer types:
Default value: 0

| Type  | Description |
| ----- | ---------- |
|  i8  | signed 8 bit integer
|  i16 | signed 16 bit integer
| i32 | signed 32 bit integer
| i64 | signed 64 bit integer
|  u8 | unsigned 8 bit integer
| u16 | unsigned 16 bit integer
| u32 | unsigned 32 bit integer
| u64 | unsigned 64 bit integer
| f32 | 32 bit float
| f64 | 64 bit float
| *isize | signed pointer size integer
| *usize | unsigned pointer size integer
\* Platform dependent

## Literal types
| Types | Examples |
| ----- | ------- |
| Decimal | 123 |
| Heximal | 0x12abcdef |
| Binary | 10010101b |
| float | 123.3456/0.975 |

## Boolean type
Keyword: ```bool```

range: ```true```/```false``` (default: ```false```)

## Tuple type
Form: ```(Type1, Type2, ...TypeN)```
### Examples
Declaring:
```
(i8, i16, u32) tup = (1, -1, 0xffffffff);
```
Dereferencing:
```
print(tup[0]);
// $ 1

tup[1] = 123;
```

## Array type
Form: ```[Element1, Element2, ...ElementN]```
### Examples
Declaring:
```
i8 arr1[] = [1, 2, 3, 4, 5, 65, 8];
i8 arr2[4] = [10, 9, 8, 7];
i8 arr3[] = ['apple': 5, 'orange': 0];
```
Dereferencing:
```
print(arr1[0]);
// $ 1

print(arr2[3]);
// $ 7

print(arr3['apple']);
// $ 5

print(arr3[0]);
// $ 5

arr1[1] = 123;
//arr1: [1, 123, 3, 4, 5, 65, 8]

arr3['apple'] = 4;
//arr3: ['apple': 4, 'orange': 0]
```

