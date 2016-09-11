#!/bin/bash
echo "the $1 eats $2"
pico2wave -w lookdave.wav $1 && aplay lookdave.wav
