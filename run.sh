#!/bin/bash
tmux new-session \; \
  send-keys 'uvicorn main:app --reload' C-m \; \
  split-window -h \; \
  send-keys 'python3 datafetchETH.py' C-m \; \
  split-window -v \; \
  send-keys 'python3 datafetchBSC.py' C-m \;
