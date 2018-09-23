# Preprocessor


| Name | As variable | As region | Description | 
| ----------------- | ----------| --- | ---- |
| @bind | -- | -- | Binding keyword, same as ```#define something xxx``` in C. Able to pair with ```@end```.
| @if | -- | -- | If condition, must pair with ```@else```, ```@elif``` or ```@end``` |
| @else | -- | -- | Else condition, must pair with ```@end``` |
| @end | -- | -- | Represent the end of the region |
| @elif | -- | -- | Else-if condition, must pair with ```@else```, ```@elif``` or ```@end```
| @env | collections | -- | Store environment variables |
| @projectRoot | string | -- | Absolute path of workspace |
| @pwd | string | Relative path of this file (relative to PROJECT_ROOT) 
| @file | string | -- | File name with extension |
| @path | string | -- | Path of file (relative path to @workspace) |
| @date | string | -- | Full date in string |
| @year | string/u16 | -- | Current year |
| @month | string/u8 | -- | Current month |
| @day | string/u8 | -- | Current day in this month |
| @time | string | -- | Current time |
| @hour12 | string/(u8 hr, bool am,pm) | -- | Hour in 12-hour clock |
| @hour24 | string/u8 | -- | Hour in 24-hour clock |
| @minute | string/u8 | -- | Current minute |
| @second | string/u8 | -- | Current second |
| @interprete | bool | True | State of interprete mode |
| @compile | bool | True | State of compile mode |
| @graphic | bool | True | State of graphical simulation mode |
| @warn | -- | -- | Print warning message |
| @error | -- | -- | Print error message and pause. |
| @msg | -- | -- | Print message |
| @line | u32 | -- | Line number |
| @pos | u32 | -- | Position in line |
| @capture | string | -- | Capture string in specfic position or binding |
| @align() | -- | -- | Modify memory align | 

```
NOTE:
first solve branch, then solve bindings, final operator
```

## As variable
Code:
```
if @interprete {
    print("will call when in Interprete mode");
}
```
Processed code:

The ```'if true'``` will be gone after optimisation
```
if true {
    print("will call when in Interprete mode");
}
```
Or

Code:
```
bool isDebug = @interprete;
```
Processed code:
```
//In compile mode
bool isDebug = false;
//In interprete mode
```

## As region
Code:
```
@if @interprete
    print("This line will only appear when in interprete mode");
@else
    print("This line will only appear when in compile mode");
@end
```

Processed code(Compile mode):
```
print("This line will only appear when in compile mode");
```
Processed code(Interprete mode):
```
print("This line will only appear when in interprete mode");
```