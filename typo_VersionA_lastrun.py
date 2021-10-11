#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Wed Jul 21 13:51:49 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'typo_VersionA'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/Jadyn/Desktop/typo/typo_VersionA_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "word_intro"
word_introClock = core.Clock()
wordInst = visual.TextStim(win=win, name='wordInst',
    text="In this task, you will see a series of words, presented one after another. Some of these words will be jumbled. For example, the word 'front' might appear as 'fornt'. \n\nYour job is to read the words out loud. If the word is jumbled, please read it as if it were unjumbled. For example, please say 'front' when presented with 'fornt' and 'happy' when presented with 'haypp'. \n",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
proceed0 = keyboard.Keyboard()
proceedPrac0 = visual.TextStim(win=win, name='proceedPrac0',
    text='Press space to proceed',
    font='Arial',
    pos=(0, -0.25), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "word_intro2"
word_intro2Clock = core.Clock()
wordInst2 = visual.TextStim(win=win, name='wordInst2',
    text='As the words appear, you will hear a sound. Please try to respond as fast and accurate as you can after the sound. If you cannot unjumble the word, please try your best.\n\nOnce you respond, press the spacebar to move on to the next word. Only press the spacebar when you are done responding. \n\nPress the spacebar to complete a few practice trials.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
proceed1 = keyboard.Keyboard()

# Initialize components for Routine "word_practice"
word_practiceClock = core.Clock()
wordPrac = visual.TextStim(win=win, name='wordPrac',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wordPrac_resp = keyboard.Keyboard()
beepPrac = sound.Sound('A', secs=0.2, stereo=True, hamming=True,
    name='beepPrac')
beepPrac.setVolume(0.5)
proceedPrac = visual.TextStim(win=win, name='proceedPrac',
    text='Press space to proceed',
    font='Arial',
    pos=(0, -0.25), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ITI1 = visual.TextStim(win=win, name='ITI1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "great"
greatClock = core.Clock()
word_great = visual.TextStim(win=win, name='word_great',
    text='Great! Do you have any questions?\n\nWhen you’re ready, press the space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
proceed2 = keyboard.Keyboard()

# Initialize components for Routine "words"
wordsClock = core.Clock()
wordStim = visual.TextStim(win=win, name='wordStim',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
wordResp = keyboard.Keyboard()
proceed3 = visual.TextStim(win=win, name='proceed3',
    text='Press space to proceed',
    font='Arial',
    pos=(0, -0.25), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
wordBeep = sound.Sound('A', secs=0.2, stereo=True, hamming=True,
    name='wordBeep')
wordBeep.setVolume(0.5)
ITI2 = visual.TextStim(win=win, name='ITI2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "word_diff"
word_diffClock = core.Clock()
word_difficulty = visual.TextStim(win=win, name='word_difficulty',
    text='On a scale of 1-10, how difficult was it to read the jumbled words? \nClick on the scale below.',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
diffRating = visual.Slider(win=win, name='diffRating',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6, 7,  8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7,  8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "fatigue"
fatigueClock = core.Clock()
tired = visual.TextStim(win=win, name='tired',
    text='On a scale of 1-10, how tired are you? \nClick on the scale below.',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fatigueRating = visual.Slider(win=win, name='fatigueRating',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6, 7,  8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "sen_intro"
sen_introClock = core.Clock()
senInst = visual.TextStim(win=win, name='senInst',
    text='Now, you will see a series of sentences instead of words, one after another.  \n\nYour job is to read the sentences out loud. If some of the sentences are jumbled, plsaee raed it as if it wree unjbmuled. \n\nAs the sentences appear, you will hear a sound. After the sound, please try to respond as fast as you can while understanding the sentences to the best of your ability. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
proceed4 = keyboard.Keyboard()

# Initialize components for Routine "sen_intro2"
sen_intro2Clock = core.Clock()
senInst2 = visual.TextStim(win=win, name='senInst2',
    text='Once you respond, press the spacebar to move on to the next sentence. Only press the spacebar when you are done responding. \n\nPress the spacebar to complete a few practice trials.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
proceed4_2 = keyboard.Keyboard()

# Initialize components for Routine "sen_practice"
sen_practiceClock = core.Clock()
sentPrac = visual.TextStim(win=win, name='sentPrac',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sentPrac_resp = keyboard.Keyboard()
beepSentPrac = sound.Sound('A', secs=0.2, stereo=True, hamming=True,
    name='beepSentPrac')
beepSentPrac.setVolume(0.5)
proceedSent = visual.TextStim(win=win, name='proceedSent',
    text='Press space to proceed',
    font='Arial',
    pos=(0, -0.25), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ITI3 = visual.TextStim(win=win, name='ITI3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "block2_intro"
block2_introClock = core.Clock()
block2Intro = visual.TextStim(win=win, name='block2Intro',
    text='You will now begin the actual task. \n\nPlease do not worry about the meaning and focus on reading the sentences as fast and accurate as you can.\n\nWhen you’re ready, press space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
proceed5 = keyboard.Keyboard()

# Initialize components for Routine "meaningful"
meaningfulClock = core.Clock()
sentStim = visual.TextStim(win=win, name='sentStim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sentResp = keyboard.Keyboard()
proceed6 = visual.TextStim(win=win, name='proceed6',
    text='Press space to proceed',
    font='Arial',
    pos=(0, -0.25), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
sentBeep = sound.Sound('audio/beep.wav', secs=0.2, stereo=True, hamming=True,
    name='sentBeep')
sentBeep.setVolume(1.0)
ITI4 = visual.TextStim(win=win, name='ITI4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "sent_diff"
sent_diffClock = core.Clock()
sent_difficulty = visual.TextStim(win=win, name='sent_difficulty',
    text='On a scale of 1-10, how difficult was it to read the jumbled sentences? \nClick on the scale below.',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sentRating = visual.Slider(win=win, name='sentRating',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "fatigue"
fatigueClock = core.Clock()
tired = visual.TextStim(win=win, name='tired',
    text='On a scale of 1-10, how tired are you? \nClick on the scale below.',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fatigueRating = visual.Slider(win=win, name='fatigueRating',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6, 7,  8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "block3_intro"
block3_introClock = core.Clock()
block3Intro = visual.TextStim(win=win, name='block3Intro',
    text='Great!\n\nYou will continue reading sentences out loud. This time, the sentences may not make sense. For example, you will see sentences like “The loud grape was grateful to sing a tower”.\n\nPlease do not worry about the meaning and focus on reading the sentences as fast and accurate as you can.\n\nPress the spacebar to proceed.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
proceed7 = keyboard.Keyboard()

# Initialize components for Routine "meaningless"
meaninglessClock = core.Clock()
nonsenseStim = visual.TextStim(win=win, name='nonsenseStim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
nonsenseResp = keyboard.Keyboard()
proceed8 = visual.TextStim(win=win, name='proceed8',
    text='Press space to proceed',
    font='Arial',
    pos=(0, -0.25), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
nonsenseBeep = sound.Sound('audio/beep.wav', secs=0.2, stereo=True, hamming=True,
    name='nonsenseBeep')
nonsenseBeep.setVolume(1.0)
ITI5 = visual.TextStim(win=win, name='ITI5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "sent_diff"
sent_diffClock = core.Clock()
sent_difficulty = visual.TextStim(win=win, name='sent_difficulty',
    text='On a scale of 1-10, how difficult was it to read the jumbled sentences? \nClick on the scale below.',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sentRating = visual.Slider(win=win, name='sentRating',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "fatigue"
fatigueClock = core.Clock()
tired = visual.TextStim(win=win, name='tired',
    text='On a scale of 1-10, how tired are you? \nClick on the scale below.',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fatigueRating = visual.Slider(win=win, name='fatigueRating',
    size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=[1, 2, 3, 4, 5, 6, 7,  8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, depth=-1, readOnly=False)

# Initialize components for Routine "strategy"
strategyClock = core.Clock()
strategyUse = visual.TextStim(win=win, name='strategyUse',
    text='Did you use any strategies to unjumble the words/sentences?\nIf so, what strategies did you use? Please answer the question out loud.\n\nWhen you’re done, press the space bar to end the experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "thankyou"
thankyouClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='Thank you for participating in our experiment! ',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
escape = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "word_intro"-------
continueRoutine = True
# update component parameters for each repeat
proceed0.keys = []
proceed0.rt = []
_proceed0_allKeys = []
# keep track of which components have finished
word_introComponents = [wordInst, proceed0, proceedPrac0]
for thisComponent in word_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
word_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "word_intro"-------
while continueRoutine:
    # get current time
    t = word_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=word_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wordInst* updates
    if wordInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wordInst.frameNStart = frameN  # exact frame index
        wordInst.tStart = t  # local t and not account for scr refresh
        wordInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wordInst, 'tStartRefresh')  # time at next scr refresh
        wordInst.setAutoDraw(True)
    
    # *proceed0* updates
    waitOnFlip = False
    if proceed0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceed0.frameNStart = frameN  # exact frame index
        proceed0.tStart = t  # local t and not account for scr refresh
        proceed0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed0, 'tStartRefresh')  # time at next scr refresh
        proceed0.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed0.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed0.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed0.status == STARTED and not waitOnFlip:
        theseKeys = proceed0.getKeys(keyList=['space'], waitRelease=False)
        _proceed0_allKeys.extend(theseKeys)
        if len(_proceed0_allKeys):
            proceed0.keys = _proceed0_allKeys[-1].name  # just the last key pressed
            proceed0.rt = _proceed0_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *proceedPrac0* updates
    if proceedPrac0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceedPrac0.frameNStart = frameN  # exact frame index
        proceedPrac0.tStart = t  # local t and not account for scr refresh
        proceedPrac0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceedPrac0, 'tStartRefresh')  # time at next scr refresh
        proceedPrac0.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in word_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "word_intro"-------
for thisComponent in word_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wordInst.started', wordInst.tStartRefresh)
thisExp.addData('wordInst.stopped', wordInst.tStopRefresh)
thisExp.addData('proceedPrac0.started', proceedPrac0.tStartRefresh)
thisExp.addData('proceedPrac0.stopped', proceedPrac0.tStopRefresh)
# the Routine "word_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "word_intro2"-------
continueRoutine = True
# update component parameters for each repeat
proceed1.keys = []
proceed1.rt = []
_proceed1_allKeys = []
# keep track of which components have finished
word_intro2Components = [wordInst2, proceed1]
for thisComponent in word_intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
word_intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "word_intro2"-------
while continueRoutine:
    # get current time
    t = word_intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=word_intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wordInst2* updates
    if wordInst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wordInst2.frameNStart = frameN  # exact frame index
        wordInst2.tStart = t  # local t and not account for scr refresh
        wordInst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wordInst2, 'tStartRefresh')  # time at next scr refresh
        wordInst2.setAutoDraw(True)
    
    # *proceed1* updates
    waitOnFlip = False
    if proceed1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        proceed1.frameNStart = frameN  # exact frame index
        proceed1.tStart = t  # local t and not account for scr refresh
        proceed1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed1, 'tStartRefresh')  # time at next scr refresh
        proceed1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed1.status == STARTED and not waitOnFlip:
        theseKeys = proceed1.getKeys(keyList=['space'], waitRelease=False)
        _proceed1_allKeys.extend(theseKeys)
        if len(_proceed1_allKeys):
            proceed1.keys = _proceed1_allKeys[-1].name  # just the last key pressed
            proceed1.rt = _proceed1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in word_intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "word_intro2"-------
for thisComponent in word_intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wordInst2.started', wordInst2.tStartRefresh)
thisExp.addData('wordInst2.stopped', wordInst2.tStopRefresh)
# check responses
if proceed1.keys in ['', [], None]:  # No response was made
    proceed1.keys = None
thisExp.addData('proceed1.keys',proceed1.keys)
if proceed1.keys != None:  # we had a response
    thisExp.addData('proceed1.rt', proceed1.rt)
thisExp.addData('proceed1.started', proceed1.tStartRefresh)
thisExp.addData('proceed1.stopped', proceed1.tStopRefresh)
thisExp.nextEntry()
# the Routine "word_intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
wordPracLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('wordprac.xlsx'),
    seed=None, name='wordPracLoop')
thisExp.addLoop(wordPracLoop)  # add the loop to the experiment
thisWordPracLoop = wordPracLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWordPracLoop.rgb)
if thisWordPracLoop != None:
    for paramName in thisWordPracLoop:
        exec('{} = thisWordPracLoop[paramName]'.format(paramName))

for thisWordPracLoop in wordPracLoop:
    currentLoop = wordPracLoop
    # abbreviate parameter names if possible (e.g. rgb = thisWordPracLoop.rgb)
    if thisWordPracLoop != None:
        for paramName in thisWordPracLoop:
            exec('{} = thisWordPracLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "word_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    wordPrac.setText(word)
    wordPrac_resp.keys = []
    wordPrac_resp.rt = []
    _wordPrac_resp_allKeys = []
    beepPrac.setSound('audio/beep.wav', secs=0.2, hamming=True)
    beepPrac.setVolume(0.5, log=False)
    ITI1.setText('+')
    iti = random() * (1.5 - 1.0) + 1.0
    iti = round(iti, 2)
    thisExp.addData('iti', iti)
    
    # keep track of which components have finished
    word_practiceComponents = [wordPrac, wordPrac_resp, beepPrac, proceedPrac, ITI1]
    for thisComponent in word_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    word_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "word_practice"-------
    while continueRoutine:
        # get current time
        t = word_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=word_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wordPrac* updates
        if wordPrac.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            wordPrac.frameNStart = frameN  # exact frame index
            wordPrac.tStart = t  # local t and not account for scr refresh
            wordPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wordPrac, 'tStartRefresh')  # time at next scr refresh
            wordPrac.setAutoDraw(True)
        
        # *wordPrac_resp* updates
        waitOnFlip = False
        if wordPrac_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            wordPrac_resp.frameNStart = frameN  # exact frame index
            wordPrac_resp.tStart = t  # local t and not account for scr refresh
            wordPrac_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wordPrac_resp, 'tStartRefresh')  # time at next scr refresh
            wordPrac_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wordPrac_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wordPrac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wordPrac_resp.status == STARTED and not waitOnFlip:
            theseKeys = wordPrac_resp.getKeys(keyList=['space'], waitRelease=False)
            _wordPrac_resp_allKeys.extend(theseKeys)
            if len(_wordPrac_resp_allKeys):
                wordPrac_resp.keys = _wordPrac_resp_allKeys[-1].name  # just the last key pressed
                wordPrac_resp.rt = _wordPrac_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop beepPrac
        if beepPrac.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            beepPrac.frameNStart = frameN  # exact frame index
            beepPrac.tStart = t  # local t and not account for scr refresh
            beepPrac.tStartRefresh = tThisFlipGlobal  # on global time
            beepPrac.play(when=win)  # sync with win flip
        if beepPrac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > beepPrac.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                beepPrac.tStop = t  # not accounting for scr refresh
                beepPrac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(beepPrac, 'tStopRefresh')  # time at next scr refresh
                beepPrac.stop()
        
        # *proceedPrac* updates
        if proceedPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proceedPrac.frameNStart = frameN  # exact frame index
            proceedPrac.tStart = t  # local t and not account for scr refresh
            proceedPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proceedPrac, 'tStartRefresh')  # time at next scr refresh
            proceedPrac.setAutoDraw(True)
        
        # *ITI1* updates
        if ITI1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI1.frameNStart = frameN  # exact frame index
            ITI1.tStart = t  # local t and not account for scr refresh
            ITI1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI1, 'tStartRefresh')  # time at next scr refresh
            ITI1.setAutoDraw(True)
        if ITI1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI1.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                ITI1.tStop = t  # not accounting for scr refresh
                ITI1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI1, 'tStopRefresh')  # time at next scr refresh
                ITI1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in word_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "word_practice"-------
    for thisComponent in word_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wordPracLoop.addData('wordPrac.started', wordPrac.tStartRefresh)
    wordPracLoop.addData('wordPrac.stopped', wordPrac.tStopRefresh)
    beepPrac.stop()  # ensure sound has stopped at end of routine
    wordPracLoop.addData('beepPrac.started', beepPrac.tStartRefresh)
    wordPracLoop.addData('beepPrac.stopped', beepPrac.tStopRefresh)
    wordPracLoop.addData('proceedPrac.started', proceedPrac.tStartRefresh)
    wordPracLoop.addData('proceedPrac.stopped', proceedPrac.tStopRefresh)
    wordPracLoop.addData('ITI1.started', ITI1.tStartRefresh)
    wordPracLoop.addData('ITI1.stopped', ITI1.tStopRefresh)
    # the Routine "word_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'wordPracLoop'


# ------Prepare to start Routine "great"-------
continueRoutine = True
# update component parameters for each repeat
proceed2.keys = []
proceed2.rt = []
_proceed2_allKeys = []
# keep track of which components have finished
greatComponents = [word_great, proceed2]
for thisComponent in greatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
greatClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "great"-------
while continueRoutine:
    # get current time
    t = greatClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=greatClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *word_great* updates
    if word_great.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        word_great.frameNStart = frameN  # exact frame index
        word_great.tStart = t  # local t and not account for scr refresh
        word_great.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(word_great, 'tStartRefresh')  # time at next scr refresh
        word_great.setAutoDraw(True)
    
    # *proceed2* updates
    if proceed2.status == NOT_STARTED and t >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        proceed2.frameNStart = frameN  # exact frame index
        proceed2.tStart = t  # local t and not account for scr refresh
        proceed2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed2, 'tStartRefresh')  # time at next scr refresh
        proceed2.status = STARTED
        # keyboard checking is just starting
        proceed2.clock.reset()  # now t=0
        proceed2.clearEvents(eventType='keyboard')
    if proceed2.status == STARTED:
        theseKeys = proceed2.getKeys(keyList=['space'], waitRelease=False)
        _proceed2_allKeys.extend(theseKeys)
        if len(_proceed2_allKeys):
            proceed2.keys = _proceed2_allKeys[-1].name  # just the last key pressed
            proceed2.rt = _proceed2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in greatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "great"-------
for thisComponent in greatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('word_great.started', word_great.tStartRefresh)
thisExp.addData('word_great.stopped', word_great.tStopRefresh)
# the Routine "great" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
wordLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('word_cond.xlsx', selection='1:5'),
    seed=None, name='wordLoop')
thisExp.addLoop(wordLoop)  # add the loop to the experiment
thisWordLoop = wordLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisWordLoop.rgb)
if thisWordLoop != None:
    for paramName in thisWordLoop:
        exec('{} = thisWordLoop[paramName]'.format(paramName))

for thisWordLoop in wordLoop:
    currentLoop = wordLoop
    # abbreviate parameter names if possible (e.g. rgb = thisWordLoop.rgb)
    if thisWordLoop != None:
        for paramName in thisWordLoop:
            exec('{} = thisWordLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "words"-------
    continueRoutine = True
    # update component parameters for each repeat
    wordStim.setText(word)
    wordResp.keys = []
    wordResp.rt = []
    _wordResp_allKeys = []
    wordBeep.setSound('audio/beep.wav', secs=0.2, hamming=True)
    wordBeep.setVolume(0.5, log=False)
    ITI2.setText('+')
    iti = random() * (1.5 - 1.0) + 1.0
    iti = round(iti, 2)
    thisExp.addData('iti', iti)
    
    # keep track of which components have finished
    wordsComponents = [wordStim, wordResp, proceed3, wordBeep, ITI2]
    for thisComponent in wordsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wordsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "words"-------
    while continueRoutine:
        # get current time
        t = wordsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wordsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *wordStim* updates
        if wordStim.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            wordStim.frameNStart = frameN  # exact frame index
            wordStim.tStart = t  # local t and not account for scr refresh
            wordStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wordStim, 'tStartRefresh')  # time at next scr refresh
            wordStim.setAutoDraw(True)
        
        # *wordResp* updates
        waitOnFlip = False
        if wordResp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            wordResp.frameNStart = frameN  # exact frame index
            wordResp.tStart = t  # local t and not account for scr refresh
            wordResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(wordResp, 'tStartRefresh')  # time at next scr refresh
            wordResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(wordResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(wordResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if wordResp.status == STARTED and not waitOnFlip:
            theseKeys = wordResp.getKeys(keyList=['space'], waitRelease=False)
            _wordResp_allKeys.extend(theseKeys)
            if len(_wordResp_allKeys):
                wordResp.keys = _wordResp_allKeys[-1].name  # just the last key pressed
                wordResp.rt = _wordResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *proceed3* updates
        if proceed3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proceed3.frameNStart = frameN  # exact frame index
            proceed3.tStart = t  # local t and not account for scr refresh
            proceed3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proceed3, 'tStartRefresh')  # time at next scr refresh
            proceed3.setAutoDraw(True)
        # start/stop wordBeep
        if wordBeep.status == NOT_STARTED and t >= iti-frameTolerance:
            # keep track of start time/frame for later
            wordBeep.frameNStart = frameN  # exact frame index
            wordBeep.tStart = t  # local t and not account for scr refresh
            wordBeep.tStartRefresh = tThisFlipGlobal  # on global time
            wordBeep.play()  # start the sound (it finishes automatically)
        if wordBeep.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > wordBeep.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                wordBeep.tStop = t  # not accounting for scr refresh
                wordBeep.frameNStop = frameN  # exact frame index
                win.timeOnFlip(wordBeep, 'tStopRefresh')  # time at next scr refresh
                wordBeep.stop()
        
        # *ITI2* updates
        if ITI2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI2.frameNStart = frameN  # exact frame index
            ITI2.tStart = t  # local t and not account for scr refresh
            ITI2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI2, 'tStartRefresh')  # time at next scr refresh
            ITI2.setAutoDraw(True)
        if ITI2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI2.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                ITI2.tStop = t  # not accounting for scr refresh
                ITI2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI2, 'tStopRefresh')  # time at next scr refresh
                ITI2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wordsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "words"-------
    for thisComponent in wordsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    wordLoop.addData('wordStim.started', wordStim.tStartRefresh)
    wordLoop.addData('wordStim.stopped', wordStim.tStopRefresh)
    # check responses
    if wordResp.keys in ['', [], None]:  # No response was made
        wordResp.keys = None
    wordLoop.addData('wordResp.keys',wordResp.keys)
    if wordResp.keys != None:  # we had a response
        wordLoop.addData('wordResp.rt', wordResp.rt)
    wordLoop.addData('wordResp.started', wordResp.tStartRefresh)
    wordLoop.addData('wordResp.stopped', wordResp.tStopRefresh)
    wordLoop.addData('proceed3.started', proceed3.tStartRefresh)
    wordLoop.addData('proceed3.stopped', proceed3.tStopRefresh)
    wordBeep.stop()  # ensure sound has stopped at end of routine
    wordLoop.addData('wordBeep.started', wordBeep.tStart)
    wordLoop.addData('wordBeep.stopped', wordBeep.tStop)
    wordLoop.addData('ITI2.started', ITI2.tStartRefresh)
    wordLoop.addData('ITI2.stopped', ITI2.tStopRefresh)
    # the Routine "words" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'wordLoop'


# ------Prepare to start Routine "word_diff"-------
continueRoutine = True
# update component parameters for each repeat
diffRating.reset()
# keep track of which components have finished
word_diffComponents = [word_difficulty, diffRating]
for thisComponent in word_diffComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
word_diffClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "word_diff"-------
while continueRoutine:
    # get current time
    t = word_diffClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=word_diffClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *word_difficulty* updates
    if word_difficulty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        word_difficulty.frameNStart = frameN  # exact frame index
        word_difficulty.tStart = t  # local t and not account for scr refresh
        word_difficulty.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(word_difficulty, 'tStartRefresh')  # time at next scr refresh
        word_difficulty.setAutoDraw(True)
    
    # *diffRating* updates
    if diffRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        diffRating.frameNStart = frameN  # exact frame index
        diffRating.tStart = t  # local t and not account for scr refresh
        diffRating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(diffRating, 'tStartRefresh')  # time at next scr refresh
        diffRating.setAutoDraw(True)
    
    # Check diffRating for response to end routine
    if diffRating.getRating() is not None and diffRating.status == STARTED:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in word_diffComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "word_diff"-------
for thisComponent in word_diffComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('word_difficulty.started', word_difficulty.tStartRefresh)
thisExp.addData('word_difficulty.stopped', word_difficulty.tStopRefresh)
thisExp.addData('diffRating.response', diffRating.getRating())
thisExp.addData('diffRating.rt', diffRating.getRT())
thisExp.addData('diffRating.started', diffRating.tStartRefresh)
thisExp.addData('diffRating.stopped', diffRating.tStopRefresh)
# the Routine "word_diff" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fatigue"-------
continueRoutine = True
# update component parameters for each repeat
fatigueRating.reset()
# keep track of which components have finished
fatigueComponents = [tired, fatigueRating]
for thisComponent in fatigueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fatigueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fatigue"-------
while continueRoutine:
    # get current time
    t = fatigueClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fatigueClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tired* updates
    if tired.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tired.frameNStart = frameN  # exact frame index
        tired.tStart = t  # local t and not account for scr refresh
        tired.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tired, 'tStartRefresh')  # time at next scr refresh
        tired.setAutoDraw(True)
    
    # *fatigueRating* updates
    if fatigueRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fatigueRating.frameNStart = frameN  # exact frame index
        fatigueRating.tStart = t  # local t and not account for scr refresh
        fatigueRating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fatigueRating, 'tStartRefresh')  # time at next scr refresh
        fatigueRating.setAutoDraw(True)
    
    # Check fatigueRating for response to end routine
    if fatigueRating.getRating() is not None and fatigueRating.status == STARTED:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fatigueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fatigue"-------
for thisComponent in fatigueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tired.started', tired.tStartRefresh)
thisExp.addData('tired.stopped', tired.tStopRefresh)
thisExp.addData('fatigueRating.response', fatigueRating.getRating())
thisExp.addData('fatigueRating.rt', fatigueRating.getRT())
thisExp.addData('fatigueRating.started', fatigueRating.tStartRefresh)
thisExp.addData('fatigueRating.stopped', fatigueRating.tStopRefresh)
# the Routine "fatigue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sen_intro"-------
continueRoutine = True
# update component parameters for each repeat
proceed4.keys = []
proceed4.rt = []
_proceed4_allKeys = []
# keep track of which components have finished
sen_introComponents = [senInst, proceed4]
for thisComponent in sen_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sen_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sen_intro"-------
while continueRoutine:
    # get current time
    t = sen_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sen_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *senInst* updates
    if senInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        senInst.frameNStart = frameN  # exact frame index
        senInst.tStart = t  # local t and not account for scr refresh
        senInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(senInst, 'tStartRefresh')  # time at next scr refresh
        senInst.setAutoDraw(True)
    
    # *proceed4* updates
    waitOnFlip = False
    if proceed4.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        proceed4.frameNStart = frameN  # exact frame index
        proceed4.tStart = t  # local t and not account for scr refresh
        proceed4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed4, 'tStartRefresh')  # time at next scr refresh
        proceed4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed4.status == STARTED and not waitOnFlip:
        theseKeys = proceed4.getKeys(keyList=None, waitRelease=False)
        _proceed4_allKeys.extend(theseKeys)
        if len(_proceed4_allKeys):
            proceed4.keys = _proceed4_allKeys[-1].name  # just the last key pressed
            proceed4.rt = _proceed4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sen_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sen_intro"-------
for thisComponent in sen_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('senInst.started', senInst.tStartRefresh)
thisExp.addData('senInst.stopped', senInst.tStopRefresh)
# check responses
if proceed4.keys in ['', [], None]:  # No response was made
    proceed4.keys = None
thisExp.addData('proceed4.keys',proceed4.keys)
if proceed4.keys != None:  # we had a response
    thisExp.addData('proceed4.rt', proceed4.rt)
thisExp.addData('proceed4.started', proceed4.tStartRefresh)
thisExp.addData('proceed4.stopped', proceed4.tStopRefresh)
thisExp.nextEntry()
# the Routine "sen_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sen_intro2"-------
continueRoutine = True
# update component parameters for each repeat
proceed4_2.keys = []
proceed4_2.rt = []
_proceed4_2_allKeys = []
# keep track of which components have finished
sen_intro2Components = [senInst2, proceed4_2]
for thisComponent in sen_intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sen_intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sen_intro2"-------
while continueRoutine:
    # get current time
    t = sen_intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sen_intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *senInst2* updates
    if senInst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        senInst2.frameNStart = frameN  # exact frame index
        senInst2.tStart = t  # local t and not account for scr refresh
        senInst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(senInst2, 'tStartRefresh')  # time at next scr refresh
        senInst2.setAutoDraw(True)
    
    # *proceed4_2* updates
    waitOnFlip = False
    if proceed4_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        proceed4_2.frameNStart = frameN  # exact frame index
        proceed4_2.tStart = t  # local t and not account for scr refresh
        proceed4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed4_2, 'tStartRefresh')  # time at next scr refresh
        proceed4_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed4_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed4_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed4_2.status == STARTED and not waitOnFlip:
        theseKeys = proceed4_2.getKeys(keyList=None, waitRelease=False)
        _proceed4_2_allKeys.extend(theseKeys)
        if len(_proceed4_2_allKeys):
            proceed4_2.keys = _proceed4_2_allKeys[-1].name  # just the last key pressed
            proceed4_2.rt = _proceed4_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sen_intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sen_intro2"-------
for thisComponent in sen_intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('senInst2.started', senInst2.tStartRefresh)
thisExp.addData('senInst2.stopped', senInst2.tStopRefresh)
# check responses
if proceed4_2.keys in ['', [], None]:  # No response was made
    proceed4_2.keys = None
thisExp.addData('proceed4_2.keys',proceed4_2.keys)
if proceed4_2.keys != None:  # we had a response
    thisExp.addData('proceed4_2.rt', proceed4_2.rt)
thisExp.addData('proceed4_2.started', proceed4_2.tStartRefresh)
thisExp.addData('proceed4_2.stopped', proceed4_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "sen_intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
sentPracLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sentprac.xlsx', selection='1:5'),
    seed=None, name='sentPracLoop')
thisExp.addLoop(sentPracLoop)  # add the loop to the experiment
thisSentPracLoop = sentPracLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSentPracLoop.rgb)
if thisSentPracLoop != None:
    for paramName in thisSentPracLoop:
        exec('{} = thisSentPracLoop[paramName]'.format(paramName))

for thisSentPracLoop in sentPracLoop:
    currentLoop = sentPracLoop
    # abbreviate parameter names if possible (e.g. rgb = thisSentPracLoop.rgb)
    if thisSentPracLoop != None:
        for paramName in thisSentPracLoop:
            exec('{} = thisSentPracLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sen_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    sentPrac.setText(sentence)
    sentPrac_resp.keys = []
    sentPrac_resp.rt = []
    _sentPrac_resp_allKeys = []
    beepSentPrac.setSound('audio/beep.wav', secs=0.2, hamming=True)
    beepSentPrac.setVolume(0.5, log=False)
    ITI3.setText('+')
    iti = random() * (1.5 - 1.0) + 1.0
    iti = round(iti, 2)
    thisExp.addData('iti', iti)
    
    # keep track of which components have finished
    sen_practiceComponents = [sentPrac, sentPrac_resp, beepSentPrac, proceedSent, ITI3]
    for thisComponent in sen_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sen_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sen_practice"-------
    while continueRoutine:
        # get current time
        t = sen_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sen_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentPrac* updates
        if sentPrac.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            sentPrac.frameNStart = frameN  # exact frame index
            sentPrac.tStart = t  # local t and not account for scr refresh
            sentPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentPrac, 'tStartRefresh')  # time at next scr refresh
            sentPrac.setAutoDraw(True)
        
        # *sentPrac_resp* updates
        waitOnFlip = False
        if sentPrac_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            sentPrac_resp.frameNStart = frameN  # exact frame index
            sentPrac_resp.tStart = t  # local t and not account for scr refresh
            sentPrac_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentPrac_resp, 'tStartRefresh')  # time at next scr refresh
            sentPrac_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sentPrac_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sentPrac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sentPrac_resp.status == STARTED and not waitOnFlip:
            theseKeys = sentPrac_resp.getKeys(keyList=['space'], waitRelease=False)
            _sentPrac_resp_allKeys.extend(theseKeys)
            if len(_sentPrac_resp_allKeys):
                sentPrac_resp.keys = _sentPrac_resp_allKeys[-1].name  # just the last key pressed
                sentPrac_resp.rt = _sentPrac_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop beepSentPrac
        if beepSentPrac.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            beepSentPrac.frameNStart = frameN  # exact frame index
            beepSentPrac.tStart = t  # local t and not account for scr refresh
            beepSentPrac.tStartRefresh = tThisFlipGlobal  # on global time
            beepSentPrac.play(when=win)  # sync with win flip
        if beepSentPrac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > beepSentPrac.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                beepSentPrac.tStop = t  # not accounting for scr refresh
                beepSentPrac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(beepSentPrac, 'tStopRefresh')  # time at next scr refresh
                beepSentPrac.stop()
        
        # *proceedSent* updates
        if proceedSent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proceedSent.frameNStart = frameN  # exact frame index
            proceedSent.tStart = t  # local t and not account for scr refresh
            proceedSent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proceedSent, 'tStartRefresh')  # time at next scr refresh
            proceedSent.setAutoDraw(True)
        
        # *ITI3* updates
        if ITI3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI3.frameNStart = frameN  # exact frame index
            ITI3.tStart = t  # local t and not account for scr refresh
            ITI3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI3, 'tStartRefresh')  # time at next scr refresh
            ITI3.setAutoDraw(True)
        if ITI3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI3.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                ITI3.tStop = t  # not accounting for scr refresh
                ITI3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI3, 'tStopRefresh')  # time at next scr refresh
                ITI3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sen_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sen_practice"-------
    for thisComponent in sen_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sentPracLoop.addData('sentPrac.started', sentPrac.tStartRefresh)
    sentPracLoop.addData('sentPrac.stopped', sentPrac.tStopRefresh)
    beepSentPrac.stop()  # ensure sound has stopped at end of routine
    sentPracLoop.addData('beepSentPrac.started', beepSentPrac.tStartRefresh)
    sentPracLoop.addData('beepSentPrac.stopped', beepSentPrac.tStopRefresh)
    sentPracLoop.addData('proceedSent.started', proceedSent.tStartRefresh)
    sentPracLoop.addData('proceedSent.stopped', proceedSent.tStopRefresh)
    sentPracLoop.addData('ITI3.started', ITI3.tStartRefresh)
    sentPracLoop.addData('ITI3.stopped', ITI3.tStopRefresh)
    # the Routine "sen_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'sentPracLoop'


# ------Prepare to start Routine "block2_intro"-------
continueRoutine = True
# update component parameters for each repeat
proceed5.keys = []
proceed5.rt = []
_proceed5_allKeys = []
# keep track of which components have finished
block2_introComponents = [block2Intro, proceed5]
for thisComponent in block2_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
block2_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "block2_intro"-------
while continueRoutine:
    # get current time
    t = block2_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=block2_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block2Intro* updates
    if block2Intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block2Intro.frameNStart = frameN  # exact frame index
        block2Intro.tStart = t  # local t and not account for scr refresh
        block2Intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block2Intro, 'tStartRefresh')  # time at next scr refresh
        block2Intro.setAutoDraw(True)
    
    # *proceed5* updates
    waitOnFlip = False
    if proceed5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        proceed5.frameNStart = frameN  # exact frame index
        proceed5.tStart = t  # local t and not account for scr refresh
        proceed5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed5, 'tStartRefresh')  # time at next scr refresh
        proceed5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed5.status == STARTED and not waitOnFlip:
        theseKeys = proceed5.getKeys(keyList=['space'], waitRelease=False)
        _proceed5_allKeys.extend(theseKeys)
        if len(_proceed5_allKeys):
            proceed5.keys = _proceed5_allKeys[-1].name  # just the last key pressed
            proceed5.rt = _proceed5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block2_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block2_intro"-------
for thisComponent in block2_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('block2Intro.started', block2Intro.tStartRefresh)
thisExp.addData('block2Intro.stopped', block2Intro.tStopRefresh)
# check responses
if proceed5.keys in ['', [], None]:  # No response was made
    proceed5.keys = None
thisExp.addData('proceed5.keys',proceed5.keys)
if proceed5.keys != None:  # we had a response
    thisExp.addData('proceed5.rt', proceed5.rt)
thisExp.addData('proceed5.started', proceed5.tStartRefresh)
thisExp.addData('proceed5.stopped', proceed5.tStopRefresh)
thisExp.nextEntry()
# the Routine "block2_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
meaningLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('meaningful.xlsx', selection='1:5'),
    seed=None, name='meaningLoop')
thisExp.addLoop(meaningLoop)  # add the loop to the experiment
thisMeaningLoop = meaningLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMeaningLoop.rgb)
if thisMeaningLoop != None:
    for paramName in thisMeaningLoop:
        exec('{} = thisMeaningLoop[paramName]'.format(paramName))

for thisMeaningLoop in meaningLoop:
    currentLoop = meaningLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMeaningLoop.rgb)
    if thisMeaningLoop != None:
        for paramName in thisMeaningLoop:
            exec('{} = thisMeaningLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "meaningful"-------
    continueRoutine = True
    # update component parameters for each repeat
    sentStim.setText(sentence)
    sentResp.keys = []
    sentResp.rt = []
    _sentResp_allKeys = []
    sentBeep.setSound('audio/beep.wav', secs=0.2, hamming=True)
    sentBeep.setVolume(1.0, log=False)
    ITI4.setText('+')
    iti = random() * (1.5 - 1.0) + 1.0
    iti = round(iti, 2)
    thisExp.addData('iti', iti)
    
    # keep track of which components have finished
    meaningfulComponents = [sentStim, sentResp, proceed6, sentBeep, ITI4]
    for thisComponent in meaningfulComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    meaningfulClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "meaningful"-------
    while continueRoutine:
        # get current time
        t = meaningfulClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=meaningfulClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentStim* updates
        if sentStim.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            sentStim.frameNStart = frameN  # exact frame index
            sentStim.tStart = t  # local t and not account for scr refresh
            sentStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentStim, 'tStartRefresh')  # time at next scr refresh
            sentStim.setAutoDraw(True)
        
        # *sentResp* updates
        waitOnFlip = False
        if sentResp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            sentResp.frameNStart = frameN  # exact frame index
            sentResp.tStart = t  # local t and not account for scr refresh
            sentResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentResp, 'tStartRefresh')  # time at next scr refresh
            sentResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sentResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sentResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sentResp.status == STARTED and not waitOnFlip:
            theseKeys = sentResp.getKeys(keyList=['space'], waitRelease=False)
            _sentResp_allKeys.extend(theseKeys)
            if len(_sentResp_allKeys):
                sentResp.keys = _sentResp_allKeys[-1].name  # just the last key pressed
                sentResp.rt = _sentResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *proceed6* updates
        if proceed6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proceed6.frameNStart = frameN  # exact frame index
            proceed6.tStart = t  # local t and not account for scr refresh
            proceed6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proceed6, 'tStartRefresh')  # time at next scr refresh
            proceed6.setAutoDraw(True)
        # start/stop sentBeep
        if sentBeep.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            sentBeep.frameNStart = frameN  # exact frame index
            sentBeep.tStart = t  # local t and not account for scr refresh
            sentBeep.tStartRefresh = tThisFlipGlobal  # on global time
            sentBeep.play(when=win)  # sync with win flip
        if sentBeep.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sentBeep.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                sentBeep.tStop = t  # not accounting for scr refresh
                sentBeep.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sentBeep, 'tStopRefresh')  # time at next scr refresh
                sentBeep.stop()
        
        # *ITI4* updates
        if ITI4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI4.frameNStart = frameN  # exact frame index
            ITI4.tStart = t  # local t and not account for scr refresh
            ITI4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI4, 'tStartRefresh')  # time at next scr refresh
            ITI4.setAutoDraw(True)
        if ITI4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI4.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                ITI4.tStop = t  # not accounting for scr refresh
                ITI4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI4, 'tStopRefresh')  # time at next scr refresh
                ITI4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in meaningfulComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "meaningful"-------
    for thisComponent in meaningfulComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    meaningLoop.addData('sentStim.started', sentStim.tStartRefresh)
    meaningLoop.addData('sentStim.stopped', sentStim.tStopRefresh)
    # check responses
    if sentResp.keys in ['', [], None]:  # No response was made
        sentResp.keys = None
    meaningLoop.addData('sentResp.keys',sentResp.keys)
    if sentResp.keys != None:  # we had a response
        meaningLoop.addData('sentResp.rt', sentResp.rt)
    meaningLoop.addData('sentResp.started', sentResp.tStartRefresh)
    meaningLoop.addData('sentResp.stopped', sentResp.tStopRefresh)
    meaningLoop.addData('proceed6.started', proceed6.tStartRefresh)
    meaningLoop.addData('proceed6.stopped', proceed6.tStopRefresh)
    sentBeep.stop()  # ensure sound has stopped at end of routine
    meaningLoop.addData('sentBeep.started', sentBeep.tStartRefresh)
    meaningLoop.addData('sentBeep.stopped', sentBeep.tStopRefresh)
    meaningLoop.addData('ITI4.started', ITI4.tStartRefresh)
    meaningLoop.addData('ITI4.stopped', ITI4.tStopRefresh)
    # the Routine "meaningful" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'meaningLoop'


# ------Prepare to start Routine "sent_diff"-------
continueRoutine = True
# update component parameters for each repeat
sentRating.reset()
# keep track of which components have finished
sent_diffComponents = [sent_difficulty, sentRating]
for thisComponent in sent_diffComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sent_diffClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sent_diff"-------
while continueRoutine:
    # get current time
    t = sent_diffClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sent_diffClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sent_difficulty* updates
    if sent_difficulty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sent_difficulty.frameNStart = frameN  # exact frame index
        sent_difficulty.tStart = t  # local t and not account for scr refresh
        sent_difficulty.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sent_difficulty, 'tStartRefresh')  # time at next scr refresh
        sent_difficulty.setAutoDraw(True)
    
    # *sentRating* updates
    if sentRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sentRating.frameNStart = frameN  # exact frame index
        sentRating.tStart = t  # local t and not account for scr refresh
        sentRating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sentRating, 'tStartRefresh')  # time at next scr refresh
        sentRating.setAutoDraw(True)
    
    # Check sentRating for response to end routine
    if sentRating.getRating() is not None and sentRating.status == STARTED:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sent_diffComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sent_diff"-------
for thisComponent in sent_diffComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sent_difficulty.started', sent_difficulty.tStartRefresh)
thisExp.addData('sent_difficulty.stopped', sent_difficulty.tStopRefresh)
thisExp.addData('sentRating.response', sentRating.getRating())
thisExp.addData('sentRating.rt', sentRating.getRT())
thisExp.addData('sentRating.started', sentRating.tStartRefresh)
thisExp.addData('sentRating.stopped', sentRating.tStopRefresh)
# the Routine "sent_diff" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fatigue"-------
continueRoutine = True
# update component parameters for each repeat
fatigueRating.reset()
# keep track of which components have finished
fatigueComponents = [tired, fatigueRating]
for thisComponent in fatigueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fatigueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fatigue"-------
while continueRoutine:
    # get current time
    t = fatigueClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fatigueClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tired* updates
    if tired.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tired.frameNStart = frameN  # exact frame index
        tired.tStart = t  # local t and not account for scr refresh
        tired.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tired, 'tStartRefresh')  # time at next scr refresh
        tired.setAutoDraw(True)
    
    # *fatigueRating* updates
    if fatigueRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fatigueRating.frameNStart = frameN  # exact frame index
        fatigueRating.tStart = t  # local t and not account for scr refresh
        fatigueRating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fatigueRating, 'tStartRefresh')  # time at next scr refresh
        fatigueRating.setAutoDraw(True)
    
    # Check fatigueRating for response to end routine
    if fatigueRating.getRating() is not None and fatigueRating.status == STARTED:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fatigueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fatigue"-------
for thisComponent in fatigueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tired.started', tired.tStartRefresh)
thisExp.addData('tired.stopped', tired.tStopRefresh)
thisExp.addData('fatigueRating.response', fatigueRating.getRating())
thisExp.addData('fatigueRating.rt', fatigueRating.getRT())
thisExp.addData('fatigueRating.started', fatigueRating.tStartRefresh)
thisExp.addData('fatigueRating.stopped', fatigueRating.tStopRefresh)
# the Routine "fatigue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "block3_intro"-------
continueRoutine = True
# update component parameters for each repeat
proceed7.keys = []
proceed7.rt = []
_proceed7_allKeys = []
# keep track of which components have finished
block3_introComponents = [block3Intro, proceed7]
for thisComponent in block3_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
block3_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "block3_intro"-------
while continueRoutine:
    # get current time
    t = block3_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=block3_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block3Intro* updates
    if block3Intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block3Intro.frameNStart = frameN  # exact frame index
        block3Intro.tStart = t  # local t and not account for scr refresh
        block3Intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block3Intro, 'tStartRefresh')  # time at next scr refresh
        block3Intro.setAutoDraw(True)
    
    # *proceed7* updates
    waitOnFlip = False
    if proceed7.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        proceed7.frameNStart = frameN  # exact frame index
        proceed7.tStart = t  # local t and not account for scr refresh
        proceed7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(proceed7, 'tStartRefresh')  # time at next scr refresh
        proceed7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(proceed7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(proceed7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if proceed7.status == STARTED and not waitOnFlip:
        theseKeys = proceed7.getKeys(keyList=['space'], waitRelease=False)
        _proceed7_allKeys.extend(theseKeys)
        if len(_proceed7_allKeys):
            proceed7.keys = _proceed7_allKeys[-1].name  # just the last key pressed
            proceed7.rt = _proceed7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block3_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block3_intro"-------
for thisComponent in block3_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('block3Intro.started', block3Intro.tStartRefresh)
thisExp.addData('block3Intro.stopped', block3Intro.tStopRefresh)
# check responses
if proceed7.keys in ['', [], None]:  # No response was made
    proceed7.keys = None
thisExp.addData('proceed7.keys',proceed7.keys)
if proceed7.keys != None:  # we had a response
    thisExp.addData('proceed7.rt', proceed7.rt)
thisExp.addData('proceed7.started', proceed7.tStartRefresh)
thisExp.addData('proceed7.stopped', proceed7.tStopRefresh)
thisExp.nextEntry()
# the Routine "block3_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
nonsenseLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('meaningless.xlsx', selection='1:5'),
    seed=None, name='nonsenseLoop')
thisExp.addLoop(nonsenseLoop)  # add the loop to the experiment
thisNonsenseLoop = nonsenseLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNonsenseLoop.rgb)
if thisNonsenseLoop != None:
    for paramName in thisNonsenseLoop:
        exec('{} = thisNonsenseLoop[paramName]'.format(paramName))

for thisNonsenseLoop in nonsenseLoop:
    currentLoop = nonsenseLoop
    # abbreviate parameter names if possible (e.g. rgb = thisNonsenseLoop.rgb)
    if thisNonsenseLoop != None:
        for paramName in thisNonsenseLoop:
            exec('{} = thisNonsenseLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "meaningless"-------
    continueRoutine = True
    # update component parameters for each repeat
    nonsenseStim.setText(sentence)
    nonsenseResp.keys = []
    nonsenseResp.rt = []
    _nonsenseResp_allKeys = []
    nonsenseBeep.setSound('audio/beep.wav', secs=0.2, hamming=True)
    nonsenseBeep.setVolume(1.0, log=False)
    ITI5.setText('+')
    iti = random() * (1.5 - 1.0) + 1.0
    iti = round(iti, 2)
    thisExp.addData('iti', iti)
    
    # keep track of which components have finished
    meaninglessComponents = [nonsenseStim, nonsenseResp, proceed8, nonsenseBeep, ITI5]
    for thisComponent in meaninglessComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    meaninglessClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "meaningless"-------
    while continueRoutine:
        # get current time
        t = meaninglessClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=meaninglessClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *nonsenseStim* updates
        if nonsenseStim.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            nonsenseStim.frameNStart = frameN  # exact frame index
            nonsenseStim.tStart = t  # local t and not account for scr refresh
            nonsenseStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nonsenseStim, 'tStartRefresh')  # time at next scr refresh
            nonsenseStim.setAutoDraw(True)
        
        # *nonsenseResp* updates
        waitOnFlip = False
        if nonsenseResp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            nonsenseResp.frameNStart = frameN  # exact frame index
            nonsenseResp.tStart = t  # local t and not account for scr refresh
            nonsenseResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nonsenseResp, 'tStartRefresh')  # time at next scr refresh
            nonsenseResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(nonsenseResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(nonsenseResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if nonsenseResp.status == STARTED and not waitOnFlip:
            theseKeys = nonsenseResp.getKeys(keyList=['space'], waitRelease=False)
            _nonsenseResp_allKeys.extend(theseKeys)
            if len(_nonsenseResp_allKeys):
                nonsenseResp.keys = _nonsenseResp_allKeys[-1].name  # just the last key pressed
                nonsenseResp.rt = _nonsenseResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *proceed8* updates
        if proceed8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proceed8.frameNStart = frameN  # exact frame index
            proceed8.tStart = t  # local t and not account for scr refresh
            proceed8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proceed8, 'tStartRefresh')  # time at next scr refresh
            proceed8.setAutoDraw(True)
        # start/stop nonsenseBeep
        if nonsenseBeep.status == NOT_STARTED and tThisFlip >= iti-frameTolerance:
            # keep track of start time/frame for later
            nonsenseBeep.frameNStart = frameN  # exact frame index
            nonsenseBeep.tStart = t  # local t and not account for scr refresh
            nonsenseBeep.tStartRefresh = tThisFlipGlobal  # on global time
            nonsenseBeep.play(when=win)  # sync with win flip
        if nonsenseBeep.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nonsenseBeep.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                nonsenseBeep.tStop = t  # not accounting for scr refresh
                nonsenseBeep.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nonsenseBeep, 'tStopRefresh')  # time at next scr refresh
                nonsenseBeep.stop()
        
        # *ITI5* updates
        if ITI5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI5.frameNStart = frameN  # exact frame index
            ITI5.tStart = t  # local t and not account for scr refresh
            ITI5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI5, 'tStartRefresh')  # time at next scr refresh
            ITI5.setAutoDraw(True)
        if ITI5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI5.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                ITI5.tStop = t  # not accounting for scr refresh
                ITI5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI5, 'tStopRefresh')  # time at next scr refresh
                ITI5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in meaninglessComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "meaningless"-------
    for thisComponent in meaninglessComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nonsenseLoop.addData('nonsenseStim.started', nonsenseStim.tStartRefresh)
    nonsenseLoop.addData('nonsenseStim.stopped', nonsenseStim.tStopRefresh)
    # check responses
    if nonsenseResp.keys in ['', [], None]:  # No response was made
        nonsenseResp.keys = None
    nonsenseLoop.addData('nonsenseResp.keys',nonsenseResp.keys)
    if nonsenseResp.keys != None:  # we had a response
        nonsenseLoop.addData('nonsenseResp.rt', nonsenseResp.rt)
    nonsenseLoop.addData('nonsenseResp.started', nonsenseResp.tStartRefresh)
    nonsenseLoop.addData('nonsenseResp.stopped', nonsenseResp.tStopRefresh)
    nonsenseLoop.addData('proceed8.started', proceed8.tStartRefresh)
    nonsenseLoop.addData('proceed8.stopped', proceed8.tStopRefresh)
    nonsenseBeep.stop()  # ensure sound has stopped at end of routine
    nonsenseLoop.addData('nonsenseBeep.started', nonsenseBeep.tStartRefresh)
    nonsenseLoop.addData('nonsenseBeep.stopped', nonsenseBeep.tStopRefresh)
    nonsenseLoop.addData('ITI5.started', ITI5.tStartRefresh)
    nonsenseLoop.addData('ITI5.stopped', ITI5.tStopRefresh)
    # the Routine "meaningless" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'nonsenseLoop'


# ------Prepare to start Routine "sent_diff"-------
continueRoutine = True
# update component parameters for each repeat
sentRating.reset()
# keep track of which components have finished
sent_diffComponents = [sent_difficulty, sentRating]
for thisComponent in sent_diffComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sent_diffClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sent_diff"-------
while continueRoutine:
    # get current time
    t = sent_diffClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sent_diffClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sent_difficulty* updates
    if sent_difficulty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sent_difficulty.frameNStart = frameN  # exact frame index
        sent_difficulty.tStart = t  # local t and not account for scr refresh
        sent_difficulty.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sent_difficulty, 'tStartRefresh')  # time at next scr refresh
        sent_difficulty.setAutoDraw(True)
    
    # *sentRating* updates
    if sentRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sentRating.frameNStart = frameN  # exact frame index
        sentRating.tStart = t  # local t and not account for scr refresh
        sentRating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sentRating, 'tStartRefresh')  # time at next scr refresh
        sentRating.setAutoDraw(True)
    
    # Check sentRating for response to end routine
    if sentRating.getRating() is not None and sentRating.status == STARTED:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sent_diffComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sent_diff"-------
for thisComponent in sent_diffComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sent_difficulty.started', sent_difficulty.tStartRefresh)
thisExp.addData('sent_difficulty.stopped', sent_difficulty.tStopRefresh)
thisExp.addData('sentRating.response', sentRating.getRating())
thisExp.addData('sentRating.rt', sentRating.getRT())
thisExp.addData('sentRating.started', sentRating.tStartRefresh)
thisExp.addData('sentRating.stopped', sentRating.tStopRefresh)
# the Routine "sent_diff" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fatigue"-------
continueRoutine = True
# update component parameters for each repeat
fatigueRating.reset()
# keep track of which components have finished
fatigueComponents = [tired, fatigueRating]
for thisComponent in fatigueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fatigueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fatigue"-------
while continueRoutine:
    # get current time
    t = fatigueClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fatigueClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tired* updates
    if tired.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tired.frameNStart = frameN  # exact frame index
        tired.tStart = t  # local t and not account for scr refresh
        tired.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tired, 'tStartRefresh')  # time at next scr refresh
        tired.setAutoDraw(True)
    
    # *fatigueRating* updates
    if fatigueRating.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fatigueRating.frameNStart = frameN  # exact frame index
        fatigueRating.tStart = t  # local t and not account for scr refresh
        fatigueRating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fatigueRating, 'tStartRefresh')  # time at next scr refresh
        fatigueRating.setAutoDraw(True)
    
    # Check fatigueRating for response to end routine
    if fatigueRating.getRating() is not None and fatigueRating.status == STARTED:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fatigueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fatigue"-------
for thisComponent in fatigueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tired.started', tired.tStartRefresh)
thisExp.addData('tired.stopped', tired.tStopRefresh)
thisExp.addData('fatigueRating.response', fatigueRating.getRating())
thisExp.addData('fatigueRating.rt', fatigueRating.getRT())
thisExp.addData('fatigueRating.started', fatigueRating.tStartRefresh)
thisExp.addData('fatigueRating.stopped', fatigueRating.tStopRefresh)
# the Routine "fatigue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "strategy"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
strategyComponents = [strategyUse, key_resp_9]
for thisComponent in strategyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
strategyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "strategy"-------
while continueRoutine:
    # get current time
    t = strategyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=strategyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *strategyUse* updates
    if strategyUse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        strategyUse.frameNStart = frameN  # exact frame index
        strategyUse.tStart = t  # local t and not account for scr refresh
        strategyUse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(strategyUse, 'tStartRefresh')  # time at next scr refresh
        strategyUse.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in strategyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "strategy"-------
for thisComponent in strategyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('strategyUse.started', strategyUse.tStartRefresh)
thisExp.addData('strategyUse.stopped', strategyUse.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "strategy" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "thankyou"-------
continueRoutine = True
# update component parameters for each repeat
escape.keys = []
escape.rt = []
_escape_allKeys = []
# keep track of which components have finished
thankyouComponents = [thanks, escape]
for thisComponent in thankyouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thankyouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thankyou"-------
while continueRoutine:
    # get current time
    t = thankyouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thankyouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    
    # *escape* updates
    waitOnFlip = False
    if escape.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        escape.frameNStart = frameN  # exact frame index
        escape.tStart = t  # local t and not account for scr refresh
        escape.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(escape, 'tStartRefresh')  # time at next scr refresh
        escape.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(escape.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(escape.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if escape.status == STARTED and not waitOnFlip:
        theseKeys = escape.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _escape_allKeys.extend(theseKeys)
        if len(_escape_allKeys):
            escape.keys = _escape_allKeys[-1].name  # just the last key pressed
            escape.rt = _escape_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thankyou"-------
for thisComponent in thankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)
# check responses
if escape.keys in ['', [], None]:  # No response was made
    escape.keys = None
thisExp.addData('escape.keys',escape.keys)
if escape.keys != None:  # we had a response
    thisExp.addData('escape.rt', escape.rt)
thisExp.addData('escape.started', escape.tStartRefresh)
thisExp.addData('escape.stopped', escape.tStopRefresh)
thisExp.nextEntry()
# the Routine "thankyou" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
