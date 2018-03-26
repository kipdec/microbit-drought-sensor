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
```nomnoml
[<frame> microbit |

[drought_sensor |
- s0_val : int
- s1_val : int
- s2_val : int

|
+ get_data() : boolean
+ send_data() : boolean
+ modulate() : void
+ calibrate() : void
- get_sensor_val(sensor int) : void
- set_sensor_val(sensor int, value int) : void

]

[get_data() : boolean |
|
+ read_sensor(sensor int) : boolean
]

]
```