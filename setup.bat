@echo off

winget install python
python3 -m pip install --upgrade pip
python3 -m pip install opencv-python-headless
python3 -m pip install auto-py-to-exe