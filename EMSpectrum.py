#!/usr/bin/python

# CONSTANTS

# Speed of light (m.s-1)
C = 3E8

# Frequencies (Hz)
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
    """A convenient class to convert frequencies and wavelengths"""


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
        """Convert a frequency into a wavelength"""
        if self.magnitude == 'freq':
            return Range(C / self.lower, C / self.upper, 'wave')
        else:
            raise MagnitudeError("Magnitude is already frequency!")


    def to_nm(self):
        """Convert a wavelength from meter to nanometer"""
        if self.magnitude == 'wave':
            return Range(self.lower / 1E9, self.upper / 1E9, 'wave')
        else:
            raise MagnitudeError("Magnitude is not wavelength!")


    def to_mum(self):
        """Convert a wavelength from meter to micrometer"""
        if self.magnitude == 'wave':
            return Range(self.lower / 1E6, self.upper / 1E6, 'wave')
        else:
            raise MagnitudeError("Magnitude is not wavelength!")


    def to_freq(self):
        """Convert a wavelength into frequency"""
        if self.magnitude == 'wave':
            return Range(C / self.lower, C / self.upper, 'freq')
        else:
            raise MagnitudeError("Magnitude is already wavelength!")


    def to_GHz(self):
        """Convert a frequency from Hz to GHz"""
        if self.magnitude == 'freq':
            return Range(self.lower / 1E9, self.upper / 1E9, 'freq')
        else:
            raise MagnitudeError("Magnitude is not frequency!")


    def to_MHz(self):
        """Convert a frequency in MHz"""
        if self.magnitude == 'freq':
            return Range(self.lower / 1E6, self.upper / 1E6, 'freq')
        else:
            raise MagnitudeError("Magnitude is not frequency!")



class EMSpectrum(object):
    """A class to handle Electromagnetic Spectrum wavelengths and frequencies
    
    Instanciation:

    >>> e = EMSpectrum()

    Determine in what part of the EM spectrum a given input frequency is

    >>> e.at_freq(400E9)
    400E9 Hz is in the Infrared spectrum.

    Determine in what part of the EM spectrum a given input frequency is
    
    >>> e.at_wave(700E-9)
    7.000000e-7 m is in the Visible spectrum.

    """

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
        """Determine in which part of the EM spectrum the input frequency is.

            Inputs:
                :freq: The input frequency 

        """
        if RADIO_FREQ_MIN < freq < RADIO_FREQ_MAX:
            print "%e Hz is in the Radio spectrum." % freq
        elif IR_FREQ_MIN < freq < IR_FREQ_MAX:
            print "%e Hz is in the Infrared spectrum." % freq
        elif VISIBLE_FREQ_MIN < freq < VISIBLE_FREQ_MAX:
            print "%e Hz is in the Visible spectrum." % freq
        elif UV_FREQ_MIN < freq < UV_FREQ_MAX:
            print "%e Hz is in the Ultraviolet spectrum." % freq
        elif X_FREQ_MIN < freq < X_FREQ_MAX:
            print "%e Hz is in the X spectrum." % freq
        elif GAMMA_FREQ_MIN < freq < GAMMA_FREQ_MAX:
            print "%e Hz is in the Gamma spectrum." % freq
        else:
            print "Wrong input."


    def at_wave(self, wave):
        """Determine in which part of the EM spectrum the input wavelength is.

            Inputs:
                :wave: The input wavelength 
        """
        if C/RADIO_FREQ_MAX < wave < C/RADIO_FREQ_MIN:
            print "%e m is in the Radio spectrum." % wave
        elif C/IR_FREQ_MAX < wave < C/IR_FREQ_MIN:
            print "%e m is in the Infrared spectrum."
        elif C/VISIBLE_FREQ_MAX < wave < C/VISIBLE_FREQ_MIN:
            print "%e m is in the Visible spectrum." % wave
        elif C/UV_FREQ_MAX < wave < C/UV_FREQ_MIN:
            print "%e m is in the Ultraviolet spectrum." % wave
        elif C/X_FREQ_MAX < wave < C/X_FREQ_MIN:
            print "%e m is in the X spectrum." % wave
        elif C/GAMMA_FREQ_MAX < wave < C/GAMMA_FREQ_MIN:
            print "%e m is in the Gamma spectrum." % wave
        else:
            print "Wrong input."

