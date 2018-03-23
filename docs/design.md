# Design

## Program flow

```nomnoml
[<frame> Program flow|

[plant]
[micro:Bit]
[PC]
[database]

[micro:Bit] +5v -> [plant]
[micro:Bit] -> [<state>record readings]
[record readings] -> [plant]
[micro:Bit] -> [<state>send readings]
[send readings] -> [PC]
[PC] -> [<state>clean and prep data]
[clean and prep data] -> [database]
]
```

## Microbit program
a change.