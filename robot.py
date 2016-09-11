from rrb3 import *
import pygame
import sys
import time
from pygame import mixer
from pygame.locals import *
import RPi.GPIO as GPIO

# TTS
import subprocess
from gtts import gTTS

audio_file = "hello.mp3"

# put it a different thread
# import os
# commandString = "raspivid -o - -t 0 -n | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264"
# os.system(commandString)


# setup rrb3 with 6 * 1.5 V
rr = RRB3(9, 6)

sound_left = '/home/pi/Desktop/TammyBot/sounds/R2D2_1.mp3'
sound_right = '/home/pi/Desktop/TammyBot/sounds/R2D2_1.mp3'
sound_up = '/home/pi/Desktop/TammyBot/sounds/R2D2_2.mp3'
sound_down = '/home/pi/Desktop/TammyBot/sounds/R2D2_2.mp3'
sound_stop = '/home/pi/Desktop/TammyBot/sounds/robot_talk.mp3'
sound_shutdown = '/home/pi/Desktop/TammyBot/sounds/robot_shutdown.mp3'
sound_wakeup = '/home/pi/Desktop/TammyBot/sounds/robot_powerup.mp3'
sound_laugh = '/home/pi/Desktop/TammyBot/sounds/robot_laugh.mp3'

# setup pins
left_eye = 17
right_eye = 27
antenna = 22

# setup vocal chords
# set up mixer (freq, audio sample size, channels used 2 for stereo, buffer size)
mixer.pre_init(44100, -16, 2, 1024)
mixer.init()

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('TammyBot v2')
pygame.mouse.set_visible(0)

# init "Head" lights
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_eye, GPIO.OUT)  # left eye
GPIO.setup(right_eye, GPIO.OUT)  # right eye
GPIO.setup(antenna, GPIO.OUT)  # antenna

GPIO.output(left_eye, GPIO.LOW)  # left eye
GPIO.output(right_eye, GPIO.LOW)  # right eye
GPIO.output(antenna, GPIO.LOW)  # antenna


# def stream:
# stream video here to VLC through rstp


def talk_real():
    tts = gTTS(text='Hello. Good morning. Blippp.', lang='en')
    tts.save(audio_file)
    return_code = subprocess.call(["omxplayer", '-o', 'local', audio_file])
    print(return_code)


def talk(voice):
    # sound/voice parameter
    mixer.music.load(voice)
    mixer.music.play(1)
    mixer.music.set_endevent(USEREVENT)  # send event when music stops


def blink_eyes(num):
    b = num

    while (b > 0):
        GPIO.output(left_eye, GPIO.HIGH)
        GPIO.output(right_eye, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(left_eye, GPIO.LOW)
        GPIO.output(right_eye, GPIO.LOW)
        b = b - 1


def r_wakeup():
    print('Blip blop blip...')
    # blink 5 times
    blinks = 5

    talk(sound_wakeup)

    while (blinks > 0):
        GPIO.output(antenna, GPIO.HIGH)
        # GPIO.output(2, GPIO.HIGH)
        # GPIO.output(3, GPIO.HIGH)

        time.sleep(1)  # sleep for 500ms

        GPIO.output(antenna, GPIO.LOW)
        # GPIO.output(2, GPIO.LOW)
        # GPIO.output(3, GPIO.LOW)

        blinks = blinks - 1
        print(blinks)


def r_shutdown():
    # sleep sound
    talk(sound_shutdown)

    pygame.time.delay(5000)

    GPIO.output(left_eye, GPIO.LOW)
    GPIO.output(right_eye, GPIO.LOW)
    GPIO.output(antenna, GPIO.LOW)
    GPIO.cleanup()

    # rest vocal chords
    mixer.music.stop()  # stop any music
    mixer.quit()  # quit mixer
    pygame.time.delay(1000)

    print('ZZZZzzzzzZZZZZZ')
    sys.exit()


# ############# PROGRAM ENTRY #################
r_wakeup()
talk_real()

# stream
# #start streaming as soon as wake up

# main program loop
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            r_shutdown()

        if event.type == KEYDOWN:
            blink_eyes(antenna)
            if event.key == K_e:
                talk(sound_up)
                rr.forward()
                rr.set_led1(True)
                rr.set_led2(True)
            elif event.key == K_d:
                talk(sound_down)
                rr.set_led1(True)
                rr.set_led2(True)
                rr.reverse()
            elif event.key == K_f:
                talk(sound_right)
                rr.set_led1(False)
                rr.set_led2(True)
                rr.right()
            elif event.key == K_s:
                talk(sound_left)
                rr.set_led1(False)
                rr.set_led2(True)
                rr.left()
            elif event.key == K_SPACE:
                talk(sound_stop)
                rr.stop()
                rr.set_led1(False)
                rr.set_led2(False)
            elif event.key == K_x:
                talk(sound_shutdown)
                rr.set_led1(False)
                rr.set_led2(False)
                r_shutdown()
            elif event.key == K_q:
                talk(sound_shutdown)
                r_shutdown()
            elif event.key == K_c:
                talk(sound_laugh)
            else:
                print('null')
