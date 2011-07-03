# Electromagnetic Spectrum


EMSpectrum is a little script to handle frequencies and wavelengths values of
the electromagnetic spectrum. It is basically classes providing a few
convenient methods to 


* determine in which part of the spectrum a given value is

* convert:
    * wavelengths to frequencies
    * frequencies to wavelengths
    * units of magnitude


# EXAMPLE

* Instantiate an EMSpectrum object:


        ems = EMSpectrum()


* Determine the frequency range of the infrared spectrum

    
        >>> ems.infrared_rad.freq
        >>> [300000000000.0, 100000000000000.0]
        >>> ems.infrared_rad.freq_unit
        >>> 'Hz'


* Convert the frequency range of the infrared spectrum in wavelength

    
        >>> ems.infrared_rad.freq.to_wave()
        >>> [3e-06, 0.001]
        >>> ems.infrared_rad.wave_unit
        >>> 'm'


# TODO

* Sort the ranges properly
* Write some tests
* Add dynamic methods
* Improve the documentation
