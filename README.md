# BlackoutWake

![pr](Assets/A5%20-%201.png)
>### I'm so digital ... blackout? time to zzzzzz. when it's on i go again.
Blackouts are a big nuisance to us digital people. When everything shuts down, our best bet would be to catch up to our sleeping backlog. _"What about if we oversleep?"_ well, BlackoutWake helps by informing you when the power turns on.

BlackoutWake was Ideated in a saga of blackouts cutting internet, charging and every other digital Item. I wanted to sleep, but still get all my fallout projects done. It uses a **AC to DC converter** to turn on a **Raspberry Pi pico** when electricity flows from the plug. The pico drives 2 **Buzzers** and displays through **oled** time when you woke up--or more accurately ~current time--from queries to an **RTC**. Let's sleep! Well, me, at very least.

## Wire

![wd](Assets/wird.png)

## 3d

![Mockup](/Assets/Mockup.jpg)
`Mockup`

![Box + Lid](/Assets/boxlid.png)
`Box & Lid`

![Opened](/Assets/Open.png)
`Open View`


[onshape](https://cad.onshape.com/documents/0ff01360ea1e6058d91f01e5/w/d01b925eefa85f8894e07011/e/78fdfa6156e56ede7d53773d?renderMode=0&uiState=6a405803cbb0f7be3ab0e881)

## Assembly
1. Solder or join all electronic parts (see Wire for connections)
2. Adhese ac-dc to edge of box
3. Screw in rtc and pico
4. Clip in oled to lid
8. Slot and optionally adhese each buzzer

## Program
1. Turn on buzz tone when power is supplied to vsys
2. Get time from RTC
3. Turn off buzzes after 5 minutes

## Bill Of Materials
| Name                 | Qty |          | Price/One | Price/Total | Notes                                                 |
| -------------------- | --- | -------- | --------- | ----------- | ----------------------------------------------------- |
| Pi pico              | 1   | Pcs      | $2.02     | $2.02       | https://www.aliexpress.com/item/1005007104120926.html |
| rtc module           | 1   | Pcs      | $2.07     | $2.07       | https://www.aliexpress.com/item/1005010675331392.html |
| ac - dc converter    | 1   | Pcs      | $0.86     | $0.86       | https://www.aliexpress.com/item/1005009215532545.html |
| Oled Module .96 inch | 1   | Pcs      | $1.15     | $1.15       | https://www.aliexpress.com/item/1005009993690787.html |
| buzzer               | 1   | Lot@5Pcs | $0.77     | $0.77       | https://www.aliexpress.com/item/32856257256.html      |
| box                  | 1   | Pcs      | $3.95     | $3.95       | https://jlc3dp.com/3d-printing-quote                  |
| lid                  | 1   | Pcs      | $1.55     | $1.55       | https://jlc3dp.com/3d-printing-quote                  |
| Cable + plug         | 1   | Set      | $0.96     | $0.96       | https://www.aliexpress.com/item/1005007805525495.html |
| Total                |     |          |           | $13.33      |                                                       |                                         

[General](/bom.csv)

## Credits
RPi
    Pi pico 3D File
