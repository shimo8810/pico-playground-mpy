#!/bin/bash

function file_exists() {
    mpremote exec "import os; import sys; print('$1' in os.listdir('$2'), end='')"
    return 0
}

# download ssd1306.mpy
if [ "$(file_exists ssd1306.mpy ./lib)" == "False" ]; then
    mpremote mip install ssd1306
fi

# upload lenna.dat
if [ "$(file_exists lenna.dat ./)" == "False" ]; then
    mpremote cp lenna.dat :
fi

# upload main.py
mpremote cp main.py :

# run
mpremote run main.py
