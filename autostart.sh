#!/bin/sh

## Qtile config directory
QTILE="$HOME/.config/qtile"

## Export qtile/scripts dir to PATH
export PATH="${PATH}:$HOME/.config/qtile/scripts"

# Kill if already running
killall -9 xsettingsd dunst xfce4-power-manager

# Lauch xsettingsd daemon
xsettingsd --config="$QTILE"/xsettingsd &

# polkit agent
if [[ ! $(pidof xfce-polkit) ]]; then
	/usr/lib/xfce-polkit/xfce-polkit &
fi

# Enable power management
xfce4-power-manager &

# Start mpd
exec mpd &

# Start qtile scripts
qtilecomp
qtiledunst
