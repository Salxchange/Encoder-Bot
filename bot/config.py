#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 5467555331
    OWNER = config("OWNER")
    ffmpegcode = ["-preset faster -c:v libx265 -s 1280x720 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1 -metadata title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata author=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:0 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:0 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:v:0 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:1 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:1 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:2 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:2 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:3 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:3 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:4 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:4 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:5 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:5 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:6 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:6 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:7 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:7 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:8 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:8 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:9 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:9 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:10 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:10 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:11 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:11 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:12 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:12 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:13 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:13 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:14 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:14 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:15 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:15 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:16 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:16 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:17 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:17 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:18 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:18 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:19 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:19 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:20 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:20 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:21 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:21 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:22 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:22 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:23 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:23 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:24 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:24 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:25 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:25 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:26 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:26 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:27 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:27 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:28 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:28 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:29 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:29 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:30 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:30 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:30 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:31 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:31 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:32 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:32 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:33 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:33 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:34 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:34 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:35 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:35 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:36 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:36 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:37 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:37 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:38 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:38 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:39 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:a:39 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾 -metadata:s:s:40 title=𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆:@𝖫𝗈𝗐_𝖬𝖻_𝖹𝗈𝗇𝖾"]
    THUMB = config("THUMBNAIL")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit(1)
