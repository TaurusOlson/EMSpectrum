#!/usr/bin/python

# CONSTANTS
C = 3E8     # m.s-1
RADIO_FREQ_MIN  , RADIO_FREQ_MAX   = 1     , 300E9
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

    def __str__(self):
        """docstring for __str__"""
        return "Name: %s\nFrequency (Hz): %s\nWavelength (m): %s" % (self.name,
                                                                self.freq,
                                                                self.wave)


class Range(list):
    """A conveneient class to convert frequencies and wavelengths"""


    # def set_unit(cls, unit):
    #     cls.unit = unit
        
    #     def _unit(self):
    #         factors = {'MHz' : 1E6,
    #                    'GHz' : 1E9,
    #                    'mum' : 1E6,
    #                    'nm'  : 1E9}
    #         return Range(self.lower/factors[cls.unit],
    #                      self.upper/factors[cls.unit],
    #                      'wave')

    #     _unit.__name__ = "to_%s" % unit
    #     setattr(cls, _unit.__name__, _unit)


    def __init__(self, upper, lower, magnitude):
        list.__init__(self, [upper, lower])
        self.upper = upper
        self.lower = lower
        self.magnitude = magnitude



    def __str__(self):
        return "[%.1e; %.1e]" % (self.lower, self.upper)


    def to_wave(self):
        """docstring for freq_to_wavelength"""
        if self.magnitude == 'freq':
            return Range(C / self.lower, C / self.upper, 'wave')
        else:
            raise MagnitudeError("Magnitude is already frequency!")


    def to_nm(self):
        """docstring for to_nm"""
        if self.magnitude == 'wave':
            return Range(self.lower / 1E9, self.upper / 1E9, 'wave')
        else:
            raise MagnitudeError("Magnitude is not wavelength!")


    def to_mum(self):
        """docstring for to_mum"""
        if self.magnitude == 'wave':
            return Range(self.lower / 1E6, self.upper / 1E6, 'wave')
        else:
            raise MagnitudeError("Magnitude is not wavelength!")


    def to_freq(self):
        """docstring for freq_to_wavelength"""
        if self.magnitude == 'wave':
            return Range(C / self.lower, C / self.upper, 'freq')
        else:
            raise MagnitudeError("Magnitude is already wavelength!")


    def to_GHz(self):
        """docstring for to_GHz"""
        if self.magnitude == 'freq':
            return Range(self.lower / 1E9, self.upper / 1E9, 'freq')
        else:
            raise MagnitudeError("Magnitude is not frequency!")


    def to_MHz(self):
        """docstring for to_MHz"""
        if self.magnitude == 'freq':
            return Range(self.lower / 1E6, self.upper / 1E6, 'freq')
        else:
            raise MagnitudeError("Magnitude is not frequency!")



class EMSpectrum(object):
    """docstring for EMSpectrum"""

    def __init__(self):
        self.radio_rad       = Radiation('Radio',
                                         Range(RADIO_FREQ_MIN,   RADIO_FREQ_MAX,   'freq'),
                                         Range(C/RADIO_FREQ_MAX, C/RADIO_FREQ_MIN, 'wave'))
        self.infrared_rad    = Radiation('Infra red',
                                         Range(IR_FREQ_MIN,   IR_FREQ_MAX,   'freq'),
                                         Range(C/IR_FREQ_MAX, C/IR_FREQ_MIN, 'wave'))
        self.visible_rad     = Radiation('Visible',
                                         Range(VISIBLE_FREQ_MIN,   VISIBLE_FREQ_MAX,   'freq'),
                                         Range(C/VISIBLE_FREQ_MAX, C/VISIBLE_FREQ_MIN, 'wave'))
        self.ultraviolet_rad = Radiation('Ultraviolet',
                                         Range(UV_FREQ_MIN,   UV_FREQ_MAX,   'freq'),
                                         Range(C/UV_FREQ_MAX, C/UV_FREQ_MIN, 'wave'))
        self.x_rad           = Radiation('X-Ray',
                                         Range(X_FREQ_MIN,   X_FREQ_MAX,   'freq'),
                                         Range(C/X_FREQ_MAX, C/X_FREQ_MIN, 'wave'))
        self.gamma_rad       = Radiation('Gamma',
                                         Range(GAMMA_FREQ_MIN,   GAMMA_FREQ_MAX,   'freq'),
                                         Range(C/GAMMA_FREQ_MAX, C/GAMMA_FREQ_MIN, 'wave'))


    def at_freq(self, freq):
        """docstring for at_freq"""
        if RADIO_FREQ_MIN < freq < RADIO_FREQ_MAX:
            print "%f is in the Radio spectrum." % freq
        elif IR_FREQ_MIN < freq < IR_FREQ_MAX:
            print "%f is in the Infrared spectrum."
        elif VISIBLE_FREQ_MIN < freq < VISIBLE_FREQ_MAX:
            print "%f is in the Visible spectrum." % freq
        elif UV_FREQ_MIN < freq < UV_FREQ_MAX:
            print "%f is in the Ultraviolet spectrum." % freq
        elif X_FREQ_MIN < freq < X_FREQ_MAX:
            print "%f is in the X spectrum." % freq
        elif GAMMA_FREQ_MIN < freq < GAMMA_FREQ_MAX:
            print "%f is in the Gamma spectrum." % freq
        else:
            print "Wrong input."


    def at_wave(self, wave):
        """docstring for at_wave"""
        if C/RADIO_FREQ_MAX < wave < C/RADIO_FREQ_MIN:
            print "%f is in the Radio spectrum." % wave
        elif C/IR_FREQ_MAX < wave < C/IR_FREQ_MIN:
            print "%f is in the Infrared spectrum."
        elif C/VISIBLE_FREQ_MAX < wave < C/VISIBLE_FREQ_MIN:
            print "%f is in the Visible spectrum." % wave
        elif C/UV_FREQ_MAX < wave < C/UV_FREQ_MIN:
            print "%f is in the Ultraviolet spectrum." % wave
        elif C/X_FREQ_MAX < wave < C/X_FREQ_MIN:
            print "%f is in the X spectrum." % wave
        elif C/GAMMA_FREQ_MAX < wave < C/GAMMA_FREQ_MIN:
            print "%f is in the Gamma spectrum." % wave
        else:
            print "Wrong input."

