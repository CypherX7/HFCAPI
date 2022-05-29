#!/bin/bash
gnome-terminal --full-screen -- tmux new-session \; \
  send-keys 'uvicorn main:app --reload' C-m \; \
  split-window -v \; \
  send-keys 'ngrok http 8000' C-m \;\
  split-window -h \; \
  send-keys 'python3 datafetchETH.py' C-m \; \
  select-pane -t 0 \; \
  split-window -h \; \
  send-keys 'python3 datafetchBSC.py' C-m \;
