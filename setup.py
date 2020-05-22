import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "asyncio", "idna", "jinja2"], "excludes": ["tkinter"], }

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Cue!",
      version="2.0",
      description="Cue Quiz Deck",
      options={"build_exe": build_exe_options},
      executables=[Executable("app.py", base=base)])
