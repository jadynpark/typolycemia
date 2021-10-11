/*********************** 
 * Typoexperiment Test *
 ***********************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'typoExperiment';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(wordInstRoutineBegin());
flowScheduler.add(wordInstRoutineEachFrame());
flowScheduler.add(wordInstRoutineEnd());
flowScheduler.add(pracInst_wordRoutineBegin());
flowScheduler.add(pracInst_wordRoutineEachFrame());
flowScheduler.add(pracInst_wordRoutineEnd());
const pracLoopWordLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pracLoopWordLoopBegin, pracLoopWordLoopScheduler);
flowScheduler.add(pracLoopWordLoopScheduler);
flowScheduler.add(pracLoopWordLoopEnd);
flowScheduler.add(greatRoutineBegin());
flowScheduler.add(greatRoutineEachFrame());
flowScheduler.add(greatRoutineEnd());
const wordLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(wordLoopLoopBegin, wordLoopLoopScheduler);
flowScheduler.add(wordLoopLoopScheduler);
flowScheduler.add(wordLoopLoopEnd);
flowScheduler.add(senInstRoutineBegin());
flowScheduler.add(senInstRoutineEachFrame());
flowScheduler.add(senInstRoutineEnd());
flowScheduler.add(pracInstSentRoutineBegin());
flowScheduler.add(pracInstSentRoutineEachFrame());
flowScheduler.add(pracInstSentRoutineEnd());
const sentLoopPracLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(sentLoopPracLoopBegin, sentLoopPracLoopScheduler);
flowScheduler.add(sentLoopPracLoopScheduler);
flowScheduler.add(sentLoopPracLoopEnd);
flowScheduler.add(great_2RoutineBegin());
flowScheduler.add(great_2RoutineEachFrame());
flowScheduler.add(great_2RoutineEnd());
const senLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(senLoopLoopBegin, senLoopLoopScheduler);
flowScheduler.add(senLoopLoopScheduler);
flowScheduler.add(senLoopLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'word_cond.xlsx', 'path': 'word_cond.xlsx'},
    {'name': 'sentprac.xlsx', 'path': 'sentprac.xlsx'},
    {'name': 'audio/beep.wav', 'path': 'audio/beep.wav'},
    {'name': 'wordprac.xlsx', 'path': 'wordprac.xlsx'},
    {'name': 'sentence_cond.xlsx', 'path': 'sentence_cond.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var wordInstClock;
var wordIntro;
var resp1;
var pracInst_wordClock;
var pracInstWord;
var key_resp;
var wordPracClock;
var pracWord;
var key_resp_2;
var beepPrac;
var proceedPrac;
var greatClock;
var text;
var key_resp_4;
var wordsClock;
var wordStim;
var wordResp;
var proceed1;
var beep1;
var senInstClock;
var senIntro;
var resp2;
var pracInstSentClock;
var senPracInst;
var key_resp_6;
var senPracClock;
var sentPrac;
var key_resp_3;
var beepSentPrac;
var proceedSent;
var great_2Clock;
var text_2;
var key_resp_5;
var sentencesClock;
var senStim;
var senResp;
var proceed2;
var beep2;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "wordInst"
  wordInstClock = new util.Clock();
  wordIntro = new visual.TextStim({
    win: psychoJS.window,
    name: 'wordIntro',
    text: 'In this task, you will see a series of words with jumbled letters presented on the screen, one at a time. However, you will probably be able to guess what most of these words mean. \n\nAs the words appear, you will hear a sound. After the sound, your job is to read the words out loud as if they were unjumbled. Try to read them as accurately as you can. Please respond only after you hear the sound. \n\nPress space bar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  resp1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracInst_word"
  pracInst_wordClock = new util.Clock();
  pracInstWord = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracInstWord',
    text: 'Let’s start with some practice. Please read the words out loud as if they were unjumbled. Try to read them as accurately as you can. Please respond only after you hear the sound. \n\nPress space bar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wordPrac"
  wordPracClock = new util.Clock();
  pracWord = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracWord',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  beepPrac = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.2,
    });
  beepPrac.setVolume(0.5);
  proceedPrac = new visual.TextStim({
    win: psychoJS.window,
    name: 'proceedPrac',
    text: 'Press space to proceed',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "great"
  greatClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Great! Do you have any questions?\n\nWhen you’re ready, press space bar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "words"
  wordsClock = new util.Clock();
  wordStim = new visual.TextStim({
    win: psychoJS.window,
    name: 'wordStim',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  wordResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  proceed1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'proceed1',
    text: 'Press space to proceed',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  beep1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.2,
    });
  beep1.setVolume(0.5);
  // Initialize components for Routine "senInst"
  senInstClock = new util.Clock();
  senIntro = new visual.TextStim({
    win: psychoJS.window,
    name: 'senIntro',
    text: 'Now, you will read sentences instead of words. Again, some of the words in the sentences may have jumbled letters. However, you will probably be able to guess what the sentence means. Please concentrate on understanding the sentences to the best of your ability. \n\nAs the sentences appear, you will hear a sound. After the sound, your job is to read the sentences out loud as if they were unjumbled. Try to read them as accurately as you can. Please remember to respond only after you hear the sound.\n\nPress space bar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  resp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracInstSent"
  pracInstSentClock = new util.Clock();
  senPracInst = new visual.TextStim({
    win: psychoJS.window,
    name: 'senPracInst',
    text: 'Let’s start with some practice. Read the sentences out loud as if they were unjumbled. Try to read them as accurately as you can. Please remember to respond only after you hear the sound.\n\nPlease concentrate on understanding the sentences to the best of your ability. \n\nPress space bar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "senPrac"
  senPracClock = new util.Clock();
  sentPrac = new visual.TextStim({
    win: psychoJS.window,
    name: 'sentPrac',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  beepSentPrac = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.2,
    });
  beepSentPrac.setVolume(0.5);
  proceedSent = new visual.TextStim({
    win: psychoJS.window,
    name: 'proceedSent',
    text: 'Press space to proceed',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "great_2"
  great_2Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Great! Do you have any questions?\n\nWhen you’re ready, press space bar to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "sentences"
  sentencesClock = new util.Clock();
  senStim = new visual.TextStim({
    win: psychoJS.window,
    name: 'senStim',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  senResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  proceed2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'proceed2',
    text: 'Press space to proceed',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  beep2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.2,
    });
  beep2.setVolume(0.5);
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _resp1_allKeys;
var wordInstComponents;
function wordInstRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'wordInst'-------
    t = 0;
    wordInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    resp1.keys = undefined;
    resp1.rt = undefined;
    _resp1_allKeys = [];
    // keep track of which components have finished
    wordInstComponents = [];
    wordInstComponents.push(wordIntro);
    wordInstComponents.push(resp1);
    
    wordInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function wordInstRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'wordInst'-------
    // get current time
    t = wordInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *wordIntro* updates
    if (t >= 0.0 && wordIntro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wordIntro.tStart = t;  // (not accounting for frame time here)
      wordIntro.frameNStart = frameN;  // exact frame index
      
      wordIntro.setAutoDraw(true);
    }

    
    // *resp1* updates
    if (t >= 0.0 && resp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp1.tStart = t;  // (not accounting for frame time here)
      resp1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp1.clearEvents(); });
    }

    if (resp1.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp1.getKeys({keyList: ['space'], waitRelease: false});
      _resp1_allKeys = _resp1_allKeys.concat(theseKeys);
      if (_resp1_allKeys.length > 0) {
        resp1.keys = _resp1_allKeys[_resp1_allKeys.length - 1].name;  // just the last key pressed
        resp1.rt = _resp1_allKeys[_resp1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    wordInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wordInstRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'wordInst'-------
    wordInstComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    resp1.stop();
    // the Routine "wordInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var pracInst_wordComponents;
function pracInst_wordRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pracInst_word'-------
    t = 0;
    pracInst_wordClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    pracInst_wordComponents = [];
    pracInst_wordComponents.push(pracInstWord);
    pracInst_wordComponents.push(key_resp);
    
    pracInst_wordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function pracInst_wordRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pracInst_word'-------
    // get current time
    t = pracInst_wordClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pracInstWord* updates
    if (t >= 0.0 && pracInstWord.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracInstWord.tStart = t;  // (not accounting for frame time here)
      pracInstWord.frameNStart = frameN;  // exact frame index
      
      pracInstWord.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pracInst_wordComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pracInst_wordRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracInst_word'-------
    pracInst_wordComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp.stop();
    // the Routine "pracInst_word" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var pracLoopWord;
var currentLoop;
function pracLoopWordLoopBegin(pracLoopWordLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  pracLoopWord = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'wordprac.xlsx', '1:6'),
    seed: undefined, name: 'pracLoopWord'
  });
  psychoJS.experiment.addLoop(pracLoopWord); // add the loop to the experiment
  currentLoop = pracLoopWord;  // we're now the current loop

  // Schedule all the trials in the trialList:
  pracLoopWord.forEach(function() {
    const snapshot = pracLoopWord.getSnapshot();

    pracLoopWordLoopScheduler.add(importConditions(snapshot));
    pracLoopWordLoopScheduler.add(wordPracRoutineBegin(snapshot));
    pracLoopWordLoopScheduler.add(wordPracRoutineEachFrame(snapshot));
    pracLoopWordLoopScheduler.add(wordPracRoutineEnd(snapshot));
    pracLoopWordLoopScheduler.add(endLoopIteration(pracLoopWordLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function pracLoopWordLoopEnd() {
  psychoJS.experiment.removeLoop(pracLoopWord);

  return Scheduler.Event.NEXT;
}


var wordLoop;
function wordLoopLoopBegin(wordLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  wordLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'word_cond.xlsx', '1:21'),
    seed: undefined, name: 'wordLoop'
  });
  psychoJS.experiment.addLoop(wordLoop); // add the loop to the experiment
  currentLoop = wordLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  wordLoop.forEach(function() {
    const snapshot = wordLoop.getSnapshot();

    wordLoopLoopScheduler.add(importConditions(snapshot));
    wordLoopLoopScheduler.add(wordsRoutineBegin(snapshot));
    wordLoopLoopScheduler.add(wordsRoutineEachFrame(snapshot));
    wordLoopLoopScheduler.add(wordsRoutineEnd(snapshot));
    wordLoopLoopScheduler.add(endLoopIteration(wordLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function wordLoopLoopEnd() {
  psychoJS.experiment.removeLoop(wordLoop);

  return Scheduler.Event.NEXT;
}


var sentLoopPrac;
function sentLoopPracLoopBegin(sentLoopPracLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  sentLoopPrac = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'sentprac.xlsx', '1:6'),
    seed: undefined, name: 'sentLoopPrac'
  });
  psychoJS.experiment.addLoop(sentLoopPrac); // add the loop to the experiment
  currentLoop = sentLoopPrac;  // we're now the current loop

  // Schedule all the trials in the trialList:
  sentLoopPrac.forEach(function() {
    const snapshot = sentLoopPrac.getSnapshot();

    sentLoopPracLoopScheduler.add(importConditions(snapshot));
    sentLoopPracLoopScheduler.add(senPracRoutineBegin(snapshot));
    sentLoopPracLoopScheduler.add(senPracRoutineEachFrame(snapshot));
    sentLoopPracLoopScheduler.add(senPracRoutineEnd(snapshot));
    sentLoopPracLoopScheduler.add(endLoopIteration(sentLoopPracLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function sentLoopPracLoopEnd() {
  psychoJS.experiment.removeLoop(sentLoopPrac);

  return Scheduler.Event.NEXT;
}


var senLoop;
function senLoopLoopBegin(senLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  senLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'sentence_cond.xlsx', '1:21'),
    seed: undefined, name: 'senLoop'
  });
  psychoJS.experiment.addLoop(senLoop); // add the loop to the experiment
  currentLoop = senLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  senLoop.forEach(function() {
    const snapshot = senLoop.getSnapshot();

    senLoopLoopScheduler.add(importConditions(snapshot));
    senLoopLoopScheduler.add(sentencesRoutineBegin(snapshot));
    senLoopLoopScheduler.add(sentencesRoutineEachFrame(snapshot));
    senLoopLoopScheduler.add(sentencesRoutineEnd(snapshot));
    senLoopLoopScheduler.add(endLoopIteration(senLoopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function senLoopLoopEnd() {
  psychoJS.experiment.removeLoop(senLoop);

  return Scheduler.Event.NEXT;
}


var _key_resp_2_allKeys;
var wordPracComponents;
function wordPracRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'wordPrac'-------
    t = 0;
    wordPracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    pracWord.setText(word);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    beepPrac = new sound.Sound({
    win: psychoJS.window,
    value: beep,
    secs: 0.2,
    });
    beepPrac.secs=0.2;
    beepPrac.setVolume(0.5);
    // keep track of which components have finished
    wordPracComponents = [];
    wordPracComponents.push(pracWord);
    wordPracComponents.push(key_resp_2);
    wordPracComponents.push(beepPrac);
    wordPracComponents.push(proceedPrac);
    
    wordPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function wordPracRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'wordPrac'-------
    // get current time
    t = wordPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pracWord* updates
    if (t >= 0.0 && pracWord.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracWord.tStart = t;  // (not accounting for frame time here)
      pracWord.frameNStart = frameN;  // exact frame index
      
      pracWord.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.2 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop beepPrac
    if (t >= 0.0 && beepPrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beepPrac.tStart = t;  // (not accounting for frame time here)
      beepPrac.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ beepPrac.play(); });  // screen flip
      beepPrac.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (beepPrac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.2 > 0.5) {  beepPrac.stop();  // stop the sound (if longer than duration)
        beepPrac.status = PsychoJS.Status.FINISHED;
      }
    }
    
    // *proceedPrac* updates
    if (t >= 0.0 && proceedPrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      proceedPrac.tStart = t;  // (not accounting for frame time here)
      proceedPrac.frameNStart = frameN;  // exact frame index
      
      proceedPrac.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    wordPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wordPracRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'wordPrac'-------
    wordPracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_2.stop();
    beepPrac.stop();  // ensure sound has stopped at end of routine
    // the Routine "wordPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var greatComponents;
function greatRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'great'-------
    t = 0;
    greatClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    greatComponents = [];
    greatComponents.push(text);
    greatComponents.push(key_resp_4);
    
    greatComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function greatRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'great'-------
    // get current time
    t = greatClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 2.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_resp_4.clock.reset();
      key_resp_4.start();
      key_resp_4.clearEvents();
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    greatComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function greatRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'great'-------
    greatComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_4.stop();
    // the Routine "great" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _wordResp_allKeys;
var wordsComponents;
function wordsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'words'-------
    t = 0;
    wordsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    wordStim.setText(word);
    wordResp.keys = undefined;
    wordResp.rt = undefined;
    _wordResp_allKeys = [];
    beep1 = new sound.Sound({
    win: psychoJS.window,
    value: beep,
    secs: 0.2,
    });
    beep1.secs=0.2;
    beep1.setVolume(0.5);
    // keep track of which components have finished
    wordsComponents = [];
    wordsComponents.push(wordStim);
    wordsComponents.push(wordResp);
    wordsComponents.push(proceed1);
    wordsComponents.push(beep1);
    
    wordsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function wordsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'words'-------
    // get current time
    t = wordsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *wordStim* updates
    if (t >= 0.0 && wordStim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wordStim.tStart = t;  // (not accounting for frame time here)
      wordStim.frameNStart = frameN;  // exact frame index
      
      wordStim.setAutoDraw(true);
    }

    
    // *wordResp* updates
    if (t >= 0.2 && wordResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wordResp.tStart = t;  // (not accounting for frame time here)
      wordResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { wordResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { wordResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { wordResp.clearEvents(); });
    }

    if (wordResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = wordResp.getKeys({keyList: ['space'], waitRelease: false});
      _wordResp_allKeys = _wordResp_allKeys.concat(theseKeys);
      if (_wordResp_allKeys.length > 0) {
        wordResp.keys = _wordResp_allKeys[_wordResp_allKeys.length - 1].name;  // just the last key pressed
        wordResp.rt = _wordResp_allKeys[_wordResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *proceed1* updates
    if (t >= 0.0 && proceed1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      proceed1.tStart = t;  // (not accounting for frame time here)
      proceed1.frameNStart = frameN;  // exact frame index
      
      proceed1.setAutoDraw(true);
    }

    // start/stop beep1
    if (t >= 0.0 && beep1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beep1.tStart = t;  // (not accounting for frame time here)
      beep1.frameNStart = frameN;  // exact frame index
      
      beep1.play();  // start the sound (it finishes automatically)
      beep1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (beep1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.2 > 0.5) {  beep1.stop();  // stop the sound (if longer than duration)
        beep1.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    wordsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wordsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'words'-------
    wordsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('wordResp.keys', wordResp.keys);
    if (typeof wordResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('wordResp.rt', wordResp.rt);
        routineTimer.reset();
        }
    
    wordResp.stop();
    beep1.stop();  // ensure sound has stopped at end of routine
    // the Routine "words" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _resp2_allKeys;
var senInstComponents;
function senInstRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'senInst'-------
    t = 0;
    senInstClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    resp2.keys = undefined;
    resp2.rt = undefined;
    _resp2_allKeys = [];
    // keep track of which components have finished
    senInstComponents = [];
    senInstComponents.push(senIntro);
    senInstComponents.push(resp2);
    
    senInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function senInstRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'senInst'-------
    // get current time
    t = senInstClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *senIntro* updates
    if (t >= 0.0 && senIntro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      senIntro.tStart = t;  // (not accounting for frame time here)
      senIntro.frameNStart = frameN;  // exact frame index
      
      senIntro.setAutoDraw(true);
    }

    
    // *resp2* updates
    if (t >= 0.2 && resp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp2.tStart = t;  // (not accounting for frame time here)
      resp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp2.clearEvents(); });
    }

    if (resp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp2.getKeys({keyList: [], waitRelease: false});
      _resp2_allKeys = _resp2_allKeys.concat(theseKeys);
      if (_resp2_allKeys.length > 0) {
        resp2.keys = _resp2_allKeys[_resp2_allKeys.length - 1].name;  // just the last key pressed
        resp2.rt = _resp2_allKeys[_resp2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    senInstComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function senInstRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'senInst'-------
    senInstComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('resp2.keys', resp2.keys);
    if (typeof resp2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp2.rt', resp2.rt);
        routineTimer.reset();
        }
    
    resp2.stop();
    // the Routine "senInst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var pracInstSentComponents;
function pracInstSentRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pracInstSent'-------
    t = 0;
    pracInstSentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    pracInstSentComponents = [];
    pracInstSentComponents.push(senPracInst);
    pracInstSentComponents.push(key_resp_6);
    
    pracInstSentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function pracInstSentRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pracInstSent'-------
    // get current time
    t = pracInstSentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *senPracInst* updates
    if (t >= 0.0 && senPracInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      senPracInst.tStart = t;  // (not accounting for frame time here)
      senPracInst.frameNStart = frameN;  // exact frame index
      
      senPracInst.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pracInstSentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pracInstSentRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracInstSent'-------
    pracInstSentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_6.stop();
    // the Routine "pracInstSent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var senPracComponents;
function senPracRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'senPrac'-------
    t = 0;
    senPracClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sentPrac.setText(sentence);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    beepSentPrac = new sound.Sound({
    win: psychoJS.window,
    value: beep,
    secs: 0.2,
    });
    beepSentPrac.secs=0.2;
    beepSentPrac.setVolume(0.5);
    // keep track of which components have finished
    senPracComponents = [];
    senPracComponents.push(sentPrac);
    senPracComponents.push(key_resp_3);
    senPracComponents.push(beepSentPrac);
    senPracComponents.push(proceedSent);
    
    senPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function senPracRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'senPrac'-------
    // get current time
    t = senPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sentPrac* updates
    if (t >= 0.0 && sentPrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sentPrac.tStart = t;  // (not accounting for frame time here)
      sentPrac.frameNStart = frameN;  // exact frame index
      
      sentPrac.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.2 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop beepSentPrac
    if (t >= 0.0 && beepSentPrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beepSentPrac.tStart = t;  // (not accounting for frame time here)
      beepSentPrac.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ beepSentPrac.play(); });  // screen flip
      beepSentPrac.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (beepSentPrac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.2 > 0.5) {  beepSentPrac.stop();  // stop the sound (if longer than duration)
        beepSentPrac.status = PsychoJS.Status.FINISHED;
      }
    }
    
    // *proceedSent* updates
    if (t >= 0.0 && proceedSent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      proceedSent.tStart = t;  // (not accounting for frame time here)
      proceedSent.frameNStart = frameN;  // exact frame index
      
      proceedSent.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    senPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function senPracRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'senPrac'-------
    senPracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_3.stop();
    beepSentPrac.stop();  // ensure sound has stopped at end of routine
    // the Routine "senPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var great_2Components;
function great_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'great_2'-------
    t = 0;
    great_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    great_2Components = [];
    great_2Components.push(text_2);
    great_2Components.push(key_resp_5);
    
    great_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function great_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'great_2'-------
    // get current time
    t = great_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 2.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    great_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function great_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'great_2'-------
    great_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "great_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _senResp_allKeys;
var sentencesComponents;
function sentencesRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'sentences'-------
    t = 0;
    sentencesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    senStim.setText(sentence);
    senResp.keys = undefined;
    senResp.rt = undefined;
    _senResp_allKeys = [];
    beep2 = new sound.Sound({
    win: psychoJS.window,
    value: beep,
    secs: 0.2,
    });
    beep2.secs=0.2;
    beep2.setVolume(0.5);
    // keep track of which components have finished
    sentencesComponents = [];
    sentencesComponents.push(senStim);
    sentencesComponents.push(senResp);
    sentencesComponents.push(proceed2);
    sentencesComponents.push(beep2);
    
    sentencesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function sentencesRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'sentences'-------
    // get current time
    t = sentencesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *senStim* updates
    if (t >= 0.0 && senStim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      senStim.tStart = t;  // (not accounting for frame time here)
      senStim.frameNStart = frameN;  // exact frame index
      
      senStim.setAutoDraw(true);
    }

    
    // *senResp* updates
    if (t >= 0.2 && senResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      senResp.tStart = t;  // (not accounting for frame time here)
      senResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { senResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { senResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { senResp.clearEvents(); });
    }

    if (senResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = senResp.getKeys({keyList: ['space'], waitRelease: false});
      _senResp_allKeys = _senResp_allKeys.concat(theseKeys);
      if (_senResp_allKeys.length > 0) {
        senResp.keys = _senResp_allKeys[_senResp_allKeys.length - 1].name;  // just the last key pressed
        senResp.rt = _senResp_allKeys[_senResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *proceed2* updates
    if (t >= 0.0 && proceed2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      proceed2.tStart = t;  // (not accounting for frame time here)
      proceed2.frameNStart = frameN;  // exact frame index
      
      proceed2.setAutoDraw(true);
    }

    // start/stop beep2
    if (t >= 0.0 && beep2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      beep2.tStart = t;  // (not accounting for frame time here)
      beep2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ beep2.play(); });  // screen flip
      beep2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (beep2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.2 > 0.5) {  beep2.stop();  // stop the sound (if longer than duration)
        beep2.status = PsychoJS.Status.FINISHED;
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    sentencesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function sentencesRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'sentences'-------
    sentencesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    senResp.stop();
    beep2.stop();  // ensure sound has stopped at end of routine
    // the Routine "sentences" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
