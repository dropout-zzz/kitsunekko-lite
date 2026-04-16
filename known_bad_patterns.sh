#!/bin/bash

exec grep --color -rnIE -- '\[(外:[0-9A-F]{32}|TEL|ｽﾋﾟｰｶ|ﾃﾚﾋﾞ)\]' "$@"
