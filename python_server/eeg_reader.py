# eeg_reader.py

import numpy as np

class EEGReader:
    def __init__(self, device=None):
        self.device = device
    
    def read(self):
        # Simulate reading EEG signals; replace with real device code
        return {
            "alpha": np.random.random(),
            "beta": np.random.random(),
            "theta": np.random.random(),
        }
