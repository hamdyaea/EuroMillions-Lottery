# EuroMillions Lottery — Random Ticket Generator

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

Generate five distinct numbers from 1–50 and two distinct stars from 1–12. Uses Python's `random.SystemRandom`. The desktop interface is built with Tkinter; a CLI is available.

```sh
python3 euroMillions.py
python3 euroMillions.py --text
python3 -m unittest discover -s tests -v
```

This is an entertainment-only random picker; it does not improve lottery odds. The historical EasyGUI implementation is preserved on the [old branch](https://github.com/hamdyaea/EuroMillions-Lottery/tree/old).
