# HandBrake Python Videos Folder Convert
A simple Python script to use Handbrake to convert videos in a folder

Requirements:
- Python3
- HandBrakeCli
- HandBrake exported preset file (*.json)
  
### Python installation
https://www.python.org/downloads/

### HandBrakeCli installation
https://handbrake.fr/downloads2.php

Copy the binary to executable path:

```
$sudo cp HandBrakeCLI /usr/local/bin
```

### HandBrake exported preset file

1. Open HandBrake app
2. Select "Presets" button at toolbar
3. Select any preset
4. Select the action button in bottom toolbar
5. "Export..."
6. Done!

## Script Usage

```
$ python3 convert.py MyHandBrakePreset.json /Data/VideosToConvert`
```

Also you can mark the script as executable

```
$ chmod +x convert.py`
```

Then

```
$ convert.py MyHandBrakePreset.json /Data/VideosToConvert
```
