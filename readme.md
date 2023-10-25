# Workshop: BBC micro:bit robot ovládaný cez Tkinter

Autor a lektor: Marek Mansell (Učíme s Hardvérom / SPy)

*Tkinter je populárny na slovenských stredných školách, no ako ho zmysluplne prepojiť s micro:bitmi?*
*Na workshope si naprogramujeme grafickú aplikáciu, pomocou ktorej budeme ovládať diaľkovo riadeného*
*BBC micro:bit robota. Zároveň budeme z micro:bit senzorov zaznamenávať údaje a posielať ich späť do počítača,*
*kde sa budú vykresľovať.*

# ToDo:

- [ ] Poskladať všetkých robotov + nabiť
- [x] Program pre MOVE MINI MK2
- [ ] Program pre Ring:bit Car V2
- [ ] Program pre Hummer
- [ ] Program pre Rugged
- [ ] Program pre Wonder Rugged
- [ ] Program pre Cutebot
- [ ] Program pre NEZHA
- [ ] Program pre Simple Robotics Kit Kitronik
- [ ] Prezentácia
- [ ] Readme dokumentácia
- [ ] DJI dron
- [ ] ESP cam
- [ ] Diaľkové ovládače

**Zoznam robotov:**

* MOVE MINI MK2 -- 4ks
* Ring:bit Car V2 -- 6ks
* Hummer prerobený -- 2ks
* Rugged -- 2ks
* Wonder Rugged Car ELECFREAKS -- 1ks
* Smart Cutebot -- 1ks
* NEZHA -- 1ks
  * AI kamera
* Simple Robotics Kit Kitronik -- 1ks

**Doplnky:**

* 4x diaľkový ovládač
* 1x dron s kamerou (DJI TELLO EDU)
* 2x ESP-32 CAM

**Obsah workshopu (90min):**

* Intro (predstavenie sa a ciele tohto workshopu)
* Inštalácia a predstavenie prostredí
  * Online Python Editor
  * Mu editor
    * `pip install mu-editor==1.2.0`
  * Thonny
* Užitočné zdroje
  * BBC micro:bit MicroPython dokumentácia
  * Tkinter dokumentácia?
* Otázky:
  * Funkcionálne vs objektové programovanie v Tkinter?
  * Skúsenosti s Pythonom?
  * Skúsenosti s micro:bitmi?
  * Skúsenosti s knižnicou pyserial?
  * Skúsenosti s inštalovaním cez pip?
  * Skúsenosti s micro:bit robotmi?
* Aktivita 1: Jednoduchý sériový komunikátor
  * Pozor na WebUSB!
* Aktivita 2: Posielanie príkazov robotovi
  * Najprv ovládanie robota
  * Potom aj meranie údajov na micro:bit a posielanie do počítača
* Aktivita 3: Vylepšenie robota
  * Pridajte vlastnú funkcionalitu pre `btn_func_c`
  * Pridajte druhú hodnotu, ktorú bude micro:bit merať a posielať (napr. naklonenie gyroskopu)



```
# ==== KEYS ====
# os.system('xset r off')  # Pre Linux
# def key_press(key):
#     if key.keysym == "Up":
#         print("Forward")
#         send_to_microbit(microbit_serial, "Forward")
#     elif key.keysym == "Down":
#         print("Back")
#         send_to_microbit(microbit_serial, "Back")
#     elif key.keysym == "Left":
#         print("Left")
#         send_to_microbit(microbit_serial, "Left")
#     elif key.keysym == "Right":
#         print("Right")
#         send_to_microbit(microbit_serial, "Right")
#
#
# def key_released(key):
#     print("Stop")
#     send_to_microbit(microbit_serial, "Stop")
#
#
# # Bind the Mouse button event
# root.bind_all('<KeyPress>', key_press)
# root.bind_all('<KeyRelease>', key_released)
# ==== END KEYS ====
```