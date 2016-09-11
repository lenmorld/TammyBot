#raspivid -o - -t 0 -n -w 128 -h 96 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264


