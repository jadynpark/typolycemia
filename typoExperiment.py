#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Mon May 10 18:20:26 2021
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
expName = 'typoExperiment'  # from the Builder filename that created this script
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
    originPath='/Users/Jadyn/Desktop/typo/typoExperiment.py',
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
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
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

# Initialize components for Routine "wordInst"
wordInstClock = core.Clock()
wordIntro = visual.TextStim(win=win, name='wordIntro',
    text='In this task, you will see a series of words with jumbled letters presented on the screen, one at a time. However, you will probably be able to guess what most of these words mean. \n\nAs the words appear, you will hear a sound. After the sound, your job is to read the words out loud as if they were unjumbled. Try to read them as accurately as you can. Please respond only after you hear the sound. \n\nPress space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
resp1 = keyboard.Keyboard()

# Initialize components for Routine "pracInst_word"
pracInst_wordClock = core.Clock()
pracInstWord = visual.TextStim(win=win, name='pracInstWord',
    text='Let’s start with some practice. Please read the words out loud as if they were unjumbled. Try to read them as accurately as you can. Please respond only after you hear the sound. \n\nPress space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "wordPrac"
wordPracClock = core.Clock()
pracWord = visual.TextStim(win=win, name='pracWord',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
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

# Initialize components for Routine "great"
greatClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Great! Do you have any questions?\n\nWhen you’re ready, press space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

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
proceed1 = visual.TextStim(win=win, name='proceed1',
    text='Press space to proceed',
    font='Arial',
    pos=(0, -0.25), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
beep1 = sound.Sound('A', secs=0.2, stereo=True, hamming=True,
    name='beep1')
beep1.setVolume(0.5)

# Initialize components for Routine "senInst"
senInstClock = core.Clock()
senIntro = visual.TextStim(win=win, name='senIntro',
    text='Now, you will read sentences instead of words. Again, some of the words in the sentences may have jumbled letters. However, you will probably be able to guess what the sentence means. Please concentrate on understanding the sentences to the best of your ability. \n\nAs the sentences appear, you will hear a sound. After the sound, your job is to read the sentences out loud as if they were unjumbled. Try to read them as accurately as you can. Please remember to respond only after you hear the sound.\n\nPress space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
resp2 = keyboard.Keyboard()

# Initialize components for Routine "pracInstSent"
pracInstSentClock = core.Clock()
senPracInst = visual.TextStim(win=win, name='senPracInst',
    text='Let’s start with some practice. Read the sentences out loud as if they were unjumbled. Try to read them as accurately as you can. Please remember to respond only after you hear the sound.\n\nPlease concentrate on understanding the sentences to the best of your ability. \n\nPress space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "senPrac"
senPracClock = core.Clock()
sentPrac = visual.TextStim(win=win, name='sentPrac',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()
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

# Initialize components for Routine "great_2"
great_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Great! Do you have any questions?\n\nWhen you’re ready, press space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "sentences"
sentencesClock = core.Clock()
senStim = visual.TextStim(win=win, name='senStim',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
senResp = keyboard.Keyboard()
proceed2 = visual.TextStim(win=win, name='proceed2',
    text='Press space to proceed',
    font='Arial',
    pos=(0, -0.25), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
beep2 = sound.Sound('A', secs=0.2, stereo=True, hamming=True,
    name='beep2')
beep2.setVolume(0.5)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wordInst"-------
continueRoutine = True
# update component parameters for each repeat
resp1.keys = []
resp1.rt = []
_resp1_allKeys = []
# keep track of which components have finished
wordInstComponents = [wordIntro, resp1]
for thisComponent in wordInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wordInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wordInst"-------
while continueRoutine:
    # get current time
    t = wordInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wordInstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wordIntro* updates
    if wordIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wordIntro.frameNStart = frameN  # exact frame index
        wordIntro.tStart = t  # local t and not account for scr refresh
        wordIntro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wordIntro, 'tStartRefresh')  # time at next scr refresh
        wordIntro.setAutoDraw(True)
    
    # *resp1* updates
    waitOnFlip = False
    if resp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp1.frameNStart = frameN  # exact frame index
        resp1.tStart = t  # local t and not account for scr refresh
        resp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp1, 'tStartRefresh')  # time at next scr refresh
        resp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp1.status == STARTED and not waitOnFlip:
        theseKeys = resp1.getKeys(keyList=['space'], waitRelease=False)
        _resp1_allKeys.extend(theseKeys)
        if len(_resp1_allKeys):
            resp1.keys = _resp1_allKeys[-1].name  # just the last key pressed
            resp1.rt = _resp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wordInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wordInst"-------
for thisComponent in wordInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wordIntro.started', wordIntro.tStartRefresh)
thisExp.addData('wordIntro.stopped', wordIntro.tStopRefresh)
# the Routine "wordInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pracInst_word"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
pracInst_wordComponents = [pracInstWord, key_resp]
for thisComponent in pracInst_wordComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pracInst_wordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pracInst_word"-------
while continueRoutine:
    # get current time
    t = pracInst_wordClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pracInst_wordClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pracInstWord* updates
    if pracInstWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracInstWord.frameNStart = frameN  # exact frame index
        pracInstWord.tStart = t  # local t and not account for scr refresh
        pracInstWord.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracInstWord, 'tStartRefresh')  # time at next scr refresh
        pracInstWord.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracInst_wordComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pracInst_word"-------
for thisComponent in pracInst_wordComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('pracInstWord.started', pracInstWord.tStartRefresh)
thisExp.addData('pracInstWord.stopped', pracInstWord.tStopRefresh)
# the Routine "pracInst_word" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracLoopWord = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('wordprac.xlsx', selection='1:6'),
    seed=None, name='pracLoopWord')
thisExp.addLoop(pracLoopWord)  # add the loop to the experiment
thisPracLoopWord = pracLoopWord.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracLoopWord.rgb)
if thisPracLoopWord != None:
    for paramName in thisPracLoopWord:
        exec('{} = thisPracLoopWord[paramName]'.format(paramName))

for thisPracLoopWord in pracLoopWord:
    currentLoop = pracLoopWord
    # abbreviate parameter names if possible (e.g. rgb = thisPracLoopWord.rgb)
    if thisPracLoopWord != None:
        for paramName in thisPracLoopWord:
            exec('{} = thisPracLoopWord[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "wordPrac"-------
    continueRoutine = True
    # update component parameters for each repeat
    pracWord.setText(word)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    beepPrac.setSound(beep, secs=0.2, hamming=True)
    beepPrac.setVolume(0.5, log=False)
    # keep track of which components have finished
    wordPracComponents = [pracWord, key_resp_2, beepPrac, proceedPrac]
    for thisComponent in wordPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    wordPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wordPrac"-------
    while continueRoutine:
        # get current time
        t = wordPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=wordPracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracWord* updates
        if pracWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracWord.frameNStart = frameN  # exact frame index
            pracWord.tStart = t  # local t and not account for scr refresh
            pracWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracWord, 'tStartRefresh')  # time at next scr refresh
            pracWord.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop beepPrac
        if beepPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wordPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wordPrac"-------
    for thisComponent in wordPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pracLoopWord.addData('pracWord.started', pracWord.tStartRefresh)
    pracLoopWord.addData('pracWord.stopped', pracWord.tStopRefresh)
    beepPrac.stop()  # ensure sound has stopped at end of routine
    pracLoopWord.addData('beepPrac.started', beepPrac.tStartRefresh)
    pracLoopWord.addData('beepPrac.stopped', beepPrac.tStopRefresh)
    pracLoopWord.addData('proceedPrac.started', proceedPrac.tStartRefresh)
    pracLoopWord.addData('proceedPrac.stopped', proceedPrac.tStopRefresh)
    # the Routine "wordPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'pracLoopWord'


# ------Prepare to start Routine "great"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
greatComponents = [text, key_resp_4]
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
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_4* updates
    if key_resp_4.status == NOT_STARTED and t >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clock.reset()  # now t=0
        key_resp_4.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "great" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
wordLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('word_cond.xlsx', selection='1:21'),
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
    beep1.setSound(beep, secs=0.2, hamming=True)
    beep1.setVolume(0.5, log=False)
    # keep track of which components have finished
    wordsComponents = [wordStim, wordResp, proceed1, beep1]
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
        if wordStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # *proceed1* updates
        if proceed1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proceed1.frameNStart = frameN  # exact frame index
            proceed1.tStart = t  # local t and not account for scr refresh
            proceed1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proceed1, 'tStartRefresh')  # time at next scr refresh
            proceed1.setAutoDraw(True)
        # start/stop beep1
        if beep1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            beep1.frameNStart = frameN  # exact frame index
            beep1.tStart = t  # local t and not account for scr refresh
            beep1.tStartRefresh = tThisFlipGlobal  # on global time
            beep1.play()  # start the sound (it finishes automatically)
        if beep1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > beep1.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                beep1.tStop = t  # not accounting for scr refresh
                beep1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(beep1, 'tStopRefresh')  # time at next scr refresh
                beep1.stop()
        
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
    wordLoop.addData('proceed1.started', proceed1.tStartRefresh)
    wordLoop.addData('proceed1.stopped', proceed1.tStopRefresh)
    beep1.stop()  # ensure sound has stopped at end of routine
    wordLoop.addData('beep1.started', beep1.tStart)
    wordLoop.addData('beep1.stopped', beep1.tStop)
    # the Routine "words" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'wordLoop'


# ------Prepare to start Routine "senInst"-------
continueRoutine = True
# update component parameters for each repeat
resp2.keys = []
resp2.rt = []
_resp2_allKeys = []
# keep track of which components have finished
senInstComponents = [senIntro, resp2]
for thisComponent in senInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
senInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "senInst"-------
while continueRoutine:
    # get current time
    t = senInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=senInstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *senIntro* updates
    if senIntro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        senIntro.frameNStart = frameN  # exact frame index
        senIntro.tStart = t  # local t and not account for scr refresh
        senIntro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(senIntro, 'tStartRefresh')  # time at next scr refresh
        senIntro.setAutoDraw(True)
    
    # *resp2* updates
    waitOnFlip = False
    if resp2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
        # keep track of start time/frame for later
        resp2.frameNStart = frameN  # exact frame index
        resp2.tStart = t  # local t and not account for scr refresh
        resp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp2, 'tStartRefresh')  # time at next scr refresh
        resp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp2.status == STARTED and not waitOnFlip:
        theseKeys = resp2.getKeys(keyList=None, waitRelease=False)
        _resp2_allKeys.extend(theseKeys)
        if len(_resp2_allKeys):
            resp2.keys = _resp2_allKeys[-1].name  # just the last key pressed
            resp2.rt = _resp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in senInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "senInst"-------
for thisComponent in senInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('senIntro.started', senIntro.tStartRefresh)
thisExp.addData('senIntro.stopped', senIntro.tStopRefresh)
# check responses
if resp2.keys in ['', [], None]:  # No response was made
    resp2.keys = None
thisExp.addData('resp2.keys',resp2.keys)
if resp2.keys != None:  # we had a response
    thisExp.addData('resp2.rt', resp2.rt)
thisExp.addData('resp2.started', resp2.tStartRefresh)
thisExp.addData('resp2.stopped', resp2.tStopRefresh)
thisExp.nextEntry()
# the Routine "senInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pracInstSent"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
pracInstSentComponents = [senPracInst, key_resp_6]
for thisComponent in pracInstSentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pracInstSentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pracInstSent"-------
while continueRoutine:
    # get current time
    t = pracInstSentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pracInstSentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *senPracInst* updates
    if senPracInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        senPracInst.frameNStart = frameN  # exact frame index
        senPracInst.tStart = t  # local t and not account for scr refresh
        senPracInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(senPracInst, 'tStartRefresh')  # time at next scr refresh
        senPracInst.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracInstSentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pracInstSent"-------
for thisComponent in pracInstSentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('senPracInst.started', senPracInst.tStartRefresh)
thisExp.addData('senPracInst.stopped', senPracInst.tStopRefresh)
# the Routine "pracInstSent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
sentLoopPrac = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sentprac.xlsx', selection='1:6'),
    seed=None, name='sentLoopPrac')
thisExp.addLoop(sentLoopPrac)  # add the loop to the experiment
thisSentLoopPrac = sentLoopPrac.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSentLoopPrac.rgb)
if thisSentLoopPrac != None:
    for paramName in thisSentLoopPrac:
        exec('{} = thisSentLoopPrac[paramName]'.format(paramName))

for thisSentLoopPrac in sentLoopPrac:
    currentLoop = sentLoopPrac
    # abbreviate parameter names if possible (e.g. rgb = thisSentLoopPrac.rgb)
    if thisSentLoopPrac != None:
        for paramName in thisSentLoopPrac:
            exec('{} = thisSentLoopPrac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "senPrac"-------
    continueRoutine = True
    # update component parameters for each repeat
    sentPrac.setText(sentence)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    beepSentPrac.setSound(beep, secs=0.2, hamming=True)
    beepSentPrac.setVolume(0.5, log=False)
    # keep track of which components have finished
    senPracComponents = [sentPrac, key_resp_3, beepSentPrac, proceedSent]
    for thisComponent in senPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    senPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "senPrac"-------
    while continueRoutine:
        # get current time
        t = senPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=senPracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentPrac* updates
        if sentPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sentPrac.frameNStart = frameN  # exact frame index
            sentPrac.tStart = t  # local t and not account for scr refresh
            sentPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sentPrac, 'tStartRefresh')  # time at next scr refresh
            sentPrac.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop beepSentPrac
        if beepSentPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in senPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "senPrac"-------
    for thisComponent in senPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sentLoopPrac.addData('sentPrac.started', sentPrac.tStartRefresh)
    sentLoopPrac.addData('sentPrac.stopped', sentPrac.tStopRefresh)
    beepSentPrac.stop()  # ensure sound has stopped at end of routine
    sentLoopPrac.addData('beepSentPrac.started', beepSentPrac.tStartRefresh)
    sentLoopPrac.addData('beepSentPrac.stopped', beepSentPrac.tStopRefresh)
    sentLoopPrac.addData('proceedSent.started', proceedSent.tStartRefresh)
    sentLoopPrac.addData('proceedSent.stopped', proceedSent.tStopRefresh)
    # the Routine "senPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'sentLoopPrac'


# ------Prepare to start Routine "great_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
great_2Components = [text_2, key_resp_5]
for thisComponent in great_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
great_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "great_2"-------
while continueRoutine:
    # get current time
    t = great_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=great_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in great_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "great_2"-------
for thisComponent in great_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "great_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
senLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sentence_cond.xlsx', selection='1:21'),
    seed=None, name='senLoop')
thisExp.addLoop(senLoop)  # add the loop to the experiment
thisSenLoop = senLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSenLoop.rgb)
if thisSenLoop != None:
    for paramName in thisSenLoop:
        exec('{} = thisSenLoop[paramName]'.format(paramName))

for thisSenLoop in senLoop:
    currentLoop = senLoop
    # abbreviate parameter names if possible (e.g. rgb = thisSenLoop.rgb)
    if thisSenLoop != None:
        for paramName in thisSenLoop:
            exec('{} = thisSenLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sentences"-------
    continueRoutine = True
    # update component parameters for each repeat
    senStim.setText(sentence)
    senResp.keys = []
    senResp.rt = []
    _senResp_allKeys = []
    beep2.setSound(beep, secs=0.2, hamming=True)
    beep2.setVolume(0.5, log=False)
    # keep track of which components have finished
    sentencesComponents = [senStim, senResp, proceed2, beep2]
    for thisComponent in sentencesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sentencesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sentences"-------
    while continueRoutine:
        # get current time
        t = sentencesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sentencesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *senStim* updates
        if senStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            senStim.frameNStart = frameN  # exact frame index
            senStim.tStart = t  # local t and not account for scr refresh
            senStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(senStim, 'tStartRefresh')  # time at next scr refresh
            senStim.setAutoDraw(True)
        
        # *senResp* updates
        waitOnFlip = False
        if senResp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            senResp.frameNStart = frameN  # exact frame index
            senResp.tStart = t  # local t and not account for scr refresh
            senResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(senResp, 'tStartRefresh')  # time at next scr refresh
            senResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(senResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(senResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if senResp.status == STARTED and not waitOnFlip:
            theseKeys = senResp.getKeys(keyList=['space'], waitRelease=False)
            _senResp_allKeys.extend(theseKeys)
            if len(_senResp_allKeys):
                senResp.keys = _senResp_allKeys[-1].name  # just the last key pressed
                senResp.rt = _senResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *proceed2* updates
        if proceed2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            proceed2.frameNStart = frameN  # exact frame index
            proceed2.tStart = t  # local t and not account for scr refresh
            proceed2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(proceed2, 'tStartRefresh')  # time at next scr refresh
            proceed2.setAutoDraw(True)
        # start/stop beep2
        if beep2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            beep2.frameNStart = frameN  # exact frame index
            beep2.tStart = t  # local t and not account for scr refresh
            beep2.tStartRefresh = tThisFlipGlobal  # on global time
            beep2.play(when=win)  # sync with win flip
        if beep2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > beep2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                beep2.tStop = t  # not accounting for scr refresh
                beep2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(beep2, 'tStopRefresh')  # time at next scr refresh
                beep2.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sentencesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sentences"-------
    for thisComponent in sentencesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    senLoop.addData('senStim.started', senStim.tStartRefresh)
    senLoop.addData('senStim.stopped', senStim.tStopRefresh)
    senLoop.addData('proceed2.started', proceed2.tStartRefresh)
    senLoop.addData('proceed2.stopped', proceed2.tStopRefresh)
    beep2.stop()  # ensure sound has stopped at end of routine
    senLoop.addData('beep2.started', beep2.tStartRefresh)
    senLoop.addData('beep2.stopped', beep2.tStopRefresh)
    # the Routine "sentences" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'senLoop'


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
