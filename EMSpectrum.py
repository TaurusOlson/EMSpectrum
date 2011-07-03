#!/usr/bin/python

# CONSTANTS
C = 3E8     # m.s-1
RADIO_FREQ_MIN  , RADIO_FREQ_MAX   = 0     , 300E9
IR_FREQ_MIN     , IR_FREQ_MAX      = 300E9 , 100E12
VISIBLE_FREQ_MIN, VISIBLE_FREQ_MAX = 400E12, 800E12
UV_FREQ_MIN     , UV_FREQ_MAX      = 750E12, 300E15
X_FREQ_MIN      , X_FREQ_MAX       = 300E15, 30E18
GAMMA_FREQ_MIN  , GAMMA_FREQ_MAX   = 30E18 , 300E18



class MagnitudeError(Exception):
    """Exception raised when the magnitude is not correct"""
    pass


class Radiation(object):
    def __init__(self, name, freq, wave):
        self.name = name
        self.freq = freq
        self.wave = wave
        self.freq_unit = "Hz"
        self.wave_unit = "m"

    # def __repr__(self):
    #     """docstring for __repr__"""
    #     return "%s" % self.name

class Range(list):
    """A conveneient class to convert frequencies and wavelengths"""
    def __init__(self, upper, lower, magnitude):
        list.__init__(self, [upper, lower])
        self.upper = upper
        self.lower = lower
        self.magnitude = magnitude


    def __str__(self):
        return "%s - %s" % (self.lower, self.upper)


    def freq_to_wave(self):
        """docstring for freq_to_wavelength"""
        if self.magnitude == 'freq':
            return [C / self.upper, C / self.lower]
        else:
            raise MagnitudeError("Magnitude is already frequency!")


    def wave_to_freq(self):
        """docstring for freq_to_wavelength"""
        if self.magnitude == 'wave':
            return [C / self.upper, C / self.lower]
        else:
            raise MagnitudeError("Magnitude is already wavelength!")


class EMSpectrum(object):
    """docstring for EMSpectrum"""

    def __init__(self):
        self.radio_ray       = Radiation('Radio',
                                         # [RADIO_FREQ_MIN, RADIO_FREQ_MAX],
                                         # [C/RADIO_FREQ_MAX, 'INF'])
                                         Range(RADIO_FREQ_MIN, RADIO_FREQ_MAX, 'freq'),
                                         Range(C/RADIO_FREQ_MAX, 'INF', 'wave'))
        self.infrared_ray    = Radiation('Infra red',
                                         # [IR_FREQ_MIN, IR_FREQ_MAX],
                                         # [C/IR_FREQ_MAX, C/IR_FREQ_MIN])
                                         Range(IR_FREQ_MIN, IR_FREQ_MAX, 'freq'),
                                         Range(C/IR_FREQ_MAX, C/IR_FREQ_MIN, 'wave'))
        self.visible_ray     = Radiation('Visible',
                                         # [VISIBLE_FREQ_MIN, VISIBLE_FREQ_MAX],
                                         # [C/VISIBLE_FREQ_MAX, C/VISIBLE_FREQ_MIN])
                                         Range(VISIBLE_FREQ_MIN, VISIBLE_FREQ_MAX, 'freq'),
                                         Range(C/VISIBLE_FREQ_MAX, C/VISIBLE_FREQ_MIN, 'wave'))
        self.ultraviolet_ray = Radiation('Ultraviolet',
                                         # [UV_FREQ_MIN, UV_FREQ_MAX],
                                         # [C/UV_FREQ_MAX, C/UV_FREQ_MIN])
                                         Range(UV_FREQ_MIN, UV_FREQ_MAX, 'freq'),
                                         Range(C/UV_FREQ_MAX, C/UV_FREQ_MIN, 'wave'))
        self.X_ray           = Radiation('X-Ray',
                                         # [X_FREQ_MIN, X_FREQ_MAX],
                                         # [C/X_FREQ_MAX, C/X_FREQ_MIN])
                                         Range(X_FREQ_MIN, X_FREQ_MAX, 'freq'),
                                         Range(C/X_FREQ_MAX, C/X_FREQ_MIN, 'wave'))
        self.gamma_ray       = Radiation('Gamma',
                                         # [GAMMA_FREQ_MIN, GAMMA_FREQ_MAX],
                                         # [C/GAMMA_FREQ_MAX, C/GAMMA_FREQ_MIN])
                                         Range(GAMMA_FREQ_MIN, GAMMA_FREQ_MAX, 'freq'),
                                         Range(C/GAMMA_FREQ_MAX, C/GAMMA_FREQ_MIN, 'wave'))


