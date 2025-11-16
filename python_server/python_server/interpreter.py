# interpreter.py

class DreamInterpreter:
    def __init__(self):
        pass
    
    def interpret(self, eeg_signals):
        valence = eeg_signals["alpha"] - eeg_signals["beta"]
        arousal = eeg_signals["theta"]
        
        if valence > 0.2 and arousal < 0.5:
            return "peaceful"
        elif valence < -0.2 and arousal > 0.7:
            return "anxious"
        else:
            return "curious"
