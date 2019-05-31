# -*- coding: utf-8 -*-

from skidl import *


def _home_rcl_arduino_uno_r3_from_scratch_Arduino_Uno_R3_From_Scratch_sch():

    #===============================================================================
    # Component templates.
    #===============================================================================

    Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__ = Part('Arduino_Uno_R3_From_Scratch', 'CERAMIC_RESONATOR', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'Characteristics', 'CER RESONATOR 16.0MHZ SMD')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'Critical', 'Y')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'Description', 'ATMEGA328P Oscillator')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'MFN', 'Murata')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'MFP', 'CSTCE16M0V53-R0')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'Package ID', 'SMD')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__, 'Subsystem', '328P_Sub')

    Arduino_Uno_R3_From_Scratch_RESET_SWITCH = Part('Arduino_Uno_R3_From_Scratch', 'RESET_SWITCH', dest=TEMPLATE)
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'Characteristics', 'SWITCH TACTILE SPST-NO 0.02A 15V')
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'Description', 'Reset Pushbutton')
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'MFN', 'Panasonic')
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'MFP', 'EVQ-Q2U02W')
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'Notes', 'Prefer below 3mm in accuator height off PCB')
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'Package ID', 'SMD')
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_RESET_SWITCH, 'Subsystem', '328P_Sub')

    Arduino_Uno_R3_From_Scratch_USB_TYPE_B__ = Part('Arduino_Uno_R3_From_Scratch', 'USB_TYPE_B', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'Characteristics', '4 CONTACT(S), FEMALE, RIGHT ANGLE USB TYPE-B CONNECTOR')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'Critical', 'Y')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'Description', 'USB Type-B Connector')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'MFN', 'TE Connectivity')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'MFP', '292304-1')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'Notes', 'Must match footprint')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'Package ID', 'PTH')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_USB_TYPE_B__, 'Subsystem', 'USB_Cnxn')

    Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'BARREL_JACK', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'Characteristics', 'CONN PWR JACK DC RA SMD  ')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'Description', '9V Barrel Jack')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'MFN', 'Wurth Electronics')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'MFP', '694106106102')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'Notes', 'Any sub must match footprint')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'Package ID', 'Custom SMD')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__, 'Subsystem', 'Voltage_Reg')

    Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'CONN_01X06', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'Characteristics', 'Connector Header 6 Position 0.100\" (2.54mm) Gold Surface Mount')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'Description', 'Shield Header 6POS - ANLG')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'MFN', 'Sullins Connector')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'MFP', 'NPPC061KFXC-RC')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'Package ID', 'SMD')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__, 'Subsystem', 'Shield_Headers')

    Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'CONN_01X08', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'Characteristics', 'Connector Header 8 Position 0.100\" (2.54mm) Gold Surface Mount')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'Description', 'Shield Header 8POS - DIG01')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'MFN', 'Sullins Connector')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'MFP', 'NPPC081KFXC-RC')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'Package ID', 'SMD')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__, 'Subsystem', 'Shield_Headers')

    Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'CONN_01X10', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'Characteristics', 'Connector Header 10 Position 0.100\" (2.54mm) Gold Surface Mount')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'Description', 'Shield Header 10POS - DIG02')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'MFN', 'Sullins Connector')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'MFP', 'NPPC101KFXC-RC')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'Package ID', 'SMD')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__, 'Subsystem', 'Shield_Headers')

    Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'CONN_02X02', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'Characteristics', 'FOOTPRINT ONLY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'Critical', 'FOOTPRINT ONLY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'Description', 'FOOTPRINT ONLY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'MFN', 'FOOTPRINT ONLY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'MFP', 'FOOTPRINT ONLY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'Package ID', 'PTH')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'Source', 'FOOTPRINT ONLY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__, 'Subsystem', '16U2_Sub')

    Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'CONN_02X03', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'Characteristics', '6 CONTACT(S), MALE, STRAIGHT TWO PART BOARD CONNECTOR')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'Description', 'ATMEGA328P ICSP Header')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'MFN', 'Harwin')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'MFP', 'M20-9980346')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'Package ID', 'PTH')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__, 'Subsystem', '328P_Sub')

    Arduino_Uno_R3_From_Scratch_rescue_CP__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'CP', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'Characteristics', 'CAPACITOR, ALUMINUM ELECTROLYTIC, NON SOLID, POLARIZED, 50 V, 47 uF, SURFACE MOUNT, 3131, CHIP, ROHS COMPLIANT')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'Description', '47uF Low ESR LDO Output Cap')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'MFN', 'Vishay')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'MFP', 'MAL215371479E3')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'Notes', 'ESR must fall between 0.33Î© and 22Î©')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'Package ID', 'SMD 5.0 x 5.0 x 5.3')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_CP__, 'Subsystem', 'Voltage_Reg')

    Arduino_Uno_R3_From_Scratch_rescue_C__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'C', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'Characteristics', 'CAPACITOR, CERAMIC, MULTILAYER, 100 V, X7R, 0.1 uF, SURFACE MOUNT, 0805, CHIP, ROHS COMPLIANT')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'Description', 'ATMEGA328P Reset Cap')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'MFN', 'Kemet')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'MFP', 'C0805C104K1RACAUTO')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'Package ID', 'SMD_0805')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_C__, 'Subsystem', '328P_Sub')

    Arduino_Uno_R3_From_Scratch_rescue_Crystal__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'Crystal', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'Characteristics', '16MHz PARALLEL FUNDAMENTAL 30PPM 20PF LOAD')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'Description', 'ATMEGA16U2 16MHz Crystal Oscillator')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'MFN', 'Fox Electronics')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'MFP', 'FOXSLF/160-20')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'Notes', 'Must Match Tolerance in PPM and Load Cap Value')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'Package ID', 'PTH')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Crystal__, 'Subsystem', '16U2_Sub')

    Arduino_Uno_R3_From_Scratch_rescue_D__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'D', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'Characteristics', 'DIODE GEN PURP 100V 300MA SOD123')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'Description', 'ATMEGA328P ICSP Reset Voltage Spike Protection')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'MFN', 'Diodes Inc')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'MFP', '1N4148W-7-F')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'Package ID', 'SOD123')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_D__, 'Subsystem', '328P_Sub')

    Arduino_Uno_R3_From_Scratch_rescue_FILTER__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'FILTER', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'Characteristics', '2 A, FERRITE CHIP, EIA STD PACKAGE SIZE 0805')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'Description', 'USB Ferrite Bead')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'MFN', 'Murata')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'MFP', 'BLM21PG221SN1D')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'Notes', 'Must meet 2A tolerance rating')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'Package ID', 'SMD_0805')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_FILTER__, 'Subsystem', 'USB_Cnxn')

    Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR = Part('Arduino_Uno_R3_From_Scratch-rescue', 'LD1117S50TR', dest=TEMPLATE)
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'Characteristics', '5 V FIXED POSITIVE LDO REGULATOR, 1.2 V DROPOUT, PDSO3, ROHS COMPLIANT, SOT-223, 4 PIN')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'Description', '5V Fixed LDO')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'MFN', 'STMicroelectronics')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'MFP', 'LD1117S50TR')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'Package ID', 'SOT-223')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'Source', 'Any')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR, 'Subsystem', 'Voltage_Reg')

    Arduino_Uno_R3_From_Scratch_rescue_LED__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'LED', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'Characteristics', 'LED CHIPLED 570NM GREEN')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'Description', 'Serial Rx Green LED')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'MFN', 'OSRAM Opto')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'MFP', 'LG R971-KN-1')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'Package ID', 'SMD_0805')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LED__, 'Subsystem', '16U2_Sub')

    Arduino_Uno_R3_From_Scratch_rescue_LM358 = Part('Arduino_Uno_R3_From_Scratch-rescue', 'LM358', dest=TEMPLATE)
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'Characteristics', 'DUAL OP-AMP, 7000uV OFFSET-MAX, 1MHz BAND WIDTH')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'Description', 'Comparator Op-amp')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'MFN', 'Texas Instruments')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'MFP', 'LMV358IDGKR')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'Package ID', 'VSSOP8')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LM358, 'Subsystem', 'Voltage_Mgmt')

    Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'LP2985LV', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'Characteristics', '3.3V FIXED POSITIVE LDO REGULATOR, 0.575V DROPOUT')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'Description', '3V3 Fixed LDO Regulator')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'MFN', 'Texas Instruments')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'MFP', 'LP2985-33DBVR')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'Package ID', 'SOT-23 5')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__, 'Subsystem', 'Voltage_Mgmt')

    Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'Q_PMOS_GSD', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'Characteristics', '2000 mA, 20 V, P-CHANNEL, Si, SMALL SIGNAL, MOSFET, SUPERSOT-3')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'Description', 'USBVCC MOSFET')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'MFN', 'Fairchild Semiconductor')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'MFP', 'FDN340P')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'Package ID', 'SOT23')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__, 'Subsystem', 'Voltage_Mgmt')

    Arduino_Uno_R3_From_Scratch_rescue_R__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'R', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'Characteristics', 'RES SMD 1M OHM 1% 1/8W 0805')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'Description', 'ATMEGA328P Xtal 1M Feedback Resistor')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'MFN', 'Vishay')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'MFP', 'CRCW08051M00FKEA')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'Package ID', 'SMD_0805')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_R__, 'Subsystem', '328P_Sub')

    Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'THERMISTOR', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'Characteristics', '500mA EMPERATURE DEPENDENT, PTC RESETTABLE FUSE')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'Description', 'PTC Resettable Fuse on USBVCC')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'MFN', 'Bourns')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'MFP', 'MF-MSMF050-2')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'Package ID', 'SMD')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__, 'Subsystem', 'USB_Cnxn')

    Arduino_Uno_R3_From_Scratch_rescue_VR__ = Part('Arduino_Uno_R3_From_Scratch-rescue', 'VR', dest=TEMPLATE, footprint='~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'Characteristics', 'VOLTAGE DEPENDENT RESISTOR, 5V, SURFACE MOUNT, CHIP, 0603,')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'Critical', 'N')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'Description', 'ESD Protection Varistor')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'MFN', 'Bourns')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'MFP', 'CG0603MLC-05E')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'Notes', '~')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'Package ID', '0603')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'Source', 'ANY')
    setattr(Arduino_Uno_R3_From_Scratch_rescue_VR__, 'Subsystem', 'USB_Cnxn')

    MFN_Atmel_ATMEGA16U2_MU = Part('MFN_Atmel', 'ATMEGA16U2-MU', dest=TEMPLATE)
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'Characteristics', 'ATMEGA16U2 Microcontroller')
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'Critical', 'Y')
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'Description', 'ATMEGA16U2 Microcontroller')
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'MFN', 'Atmel')
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'MFP', 'ATMEGA16U2-MU')
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'Notes', '~')
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'Package ID', 'QFN32')
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'Source', 'ANY')
    setattr(MFN_Atmel_ATMEGA16U2_MU, 'Subsystem', '16U2_Sub')

    MFN_Atmel_ATMEGA328P_PU__ = Part('MFN_Atmel', 'ATMEGA328P-PU', dest=TEMPLATE, footprint='~')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'Characteristics', 'IC MCU 8BIT 32KB FLASH 28DIP')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'Critical', 'Y')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'Description', 'ATMEGA328P')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'MFN', 'Atmel')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'MFP', 'ATMEGA328P-PU')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'Notes', '~')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'Package ID', 'PTH')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'Source', 'ANY')
    setattr(MFN_Atmel_ATMEGA328P_PU__, 'Subsystem', '328P_Sub')


    #===============================================================================
    # Component instantiations.
    #===============================================================================

    C1 = Arduino_Uno_R3_From_Scratch_rescue_CP__(ref='C1', value='47uF')
    setattr(C1, 'Description', '47uF Low ESR LDO Input Cap')

    C10 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C10', value='1uF')
    setattr(C10, 'Characteristics', 'CAPACITOR, CERAMIC, MULTILAYER, 10 V, X7R, 1 uF, SURFACE MOUNT, 0805')
    setattr(C10, 'Description', 'ATMEGA16U2 1uF UCAP ')
    setattr(C10, 'MFP', 'C0805C105K8RACAUTO ')
    setattr(C10, 'Subsystem', '16U2_Sub')

    C11 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C11', value='0.1 uF')

    C14 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C14', value='0.1 uF')
    setattr(C14, 'Description', 'ATMEGA328P AREF Bypass Cap')

    C15 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C15', value='0.1 uF')
    setattr(C15, 'Description', 'ATMEGA328P VCC and AVCC Bypass Cap')

    C2 = Arduino_Uno_R3_From_Scratch_rescue_CP__(ref='C2', value='47uF')

    C3 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C3', value='0.1 uF')
    setattr(C3, 'Description', 'LDO Bypass Cap')
    setattr(C3, 'Subsystem', 'Voltage_Reg')

    C4 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C4', value='0.1 uF')
    setattr(C4, 'Description', 'LDO Bypass Cap')
    setattr(C4, 'Subsystem', 'Voltage_Mgmt')

    C5 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C5', value='1uF')
    setattr(C5, 'Characteristics', 'CAPACITOR, CERAMIC, MULTILAYER, 10 V, X7R, 1 uF, SURFACE MOUNT, 0805')
    setattr(C5, 'Description', '3V3 LDO Input Cap')
    setattr(C5, 'MFP', 'C0805C105K8RACAUTO ')
    setattr(C5, 'Subsystem', 'Voltage_Mgmt')

    C6 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C6', value='2.2uF')
    setattr(C6, 'Characteristics', 'CAP CER 2.2UF 16V X7R 0805')
    setattr(C6, 'Critical', 'Y')
    setattr(C6, 'Description', '2.2uF 3V3 LDO Output Cap')
    setattr(C6, 'MFN', 'TDK Corporation')
    setattr(C6, 'MFP', 'C2012X7R1C225K125AB')
    setattr(C6, 'Notes', 'Must be between 0.001 and 1Î© ESR')
    setattr(C6, 'Subsystem', 'Voltage_Mgmt')

    C7 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C7', value='20pF')
    setattr(C7, 'Characteristics', 'CAP CER 20PF 50V 2% NP0 0805')
    setattr(C7, 'Critical', 'Y')
    setattr(C7, 'Description', '20pF ATMEGA16U2 XTAL Load Cap')
    setattr(C7, 'MFP', 'C0805C200G5GACTU')
    setattr(C7, 'Notes', 'Must match tolerance')
    setattr(C7, 'Source', 'Any')
    setattr(C7, 'Subsystem', '16U2_Sub')

    C8 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C8', value='20pF')
    setattr(C8, 'Characteristics', 'CAP CER 20PF 50V 2% NP0 0805')
    setattr(C8, 'Critical', 'Y')
    setattr(C8, 'Description', '20pF ATMEGA16U2 XTAL Load Cap')
    setattr(C8, 'MFP', 'C0805C200G5GACTU')
    setattr(C8, 'Notes', 'Must match tolerance')
    setattr(C8, 'Source', 'Any')
    setattr(C8, 'Subsystem', '16U2_Sub')

    C9 = Arduino_Uno_R3_From_Scratch_rescue_C__(ref='C9', value='0.1 uF')
    setattr(C9, 'Description', 'ATMEGA16U2 VCC Bypass Cap')
    setattr(C9, 'Subsystem', '16U2_Sub')

    CON1 = Arduino_Uno_R3_From_Scratch_rescue_BARREL_JACK__(ref='CON1', value='BARREL_JACK')

    D1 = Arduino_Uno_R3_From_Scratch_rescue_D__(ref='D1', value='DIODE')
    setattr(D1, 'Characteristics', '1A, 1000V, SILICON, SIGNAL DIODE, ROHS COMPLIANT, COMPACT, PLASTIC, CASE 403D-02, SMA, 2 PIN')
    setattr(D1, 'Description', 'Reverse Voltage Protection Diode')
    setattr(D1, 'MFN', 'ON Semi')
    setattr(D1, 'MFP', 'MRA4007T3G')
    setattr(D1, 'Package ID', 'R-PDSO-J2')
    setattr(D1, 'Subsystem', 'Voltage_Reg')

    D2 = Arduino_Uno_R3_From_Scratch_rescue_LED__(ref='D2', value='LED')
    setattr(D2, 'Description', 'Power On Green LED')
    setattr(D2, 'Subsystem', 'Voltage_Reg')

    D3 = Arduino_Uno_R3_From_Scratch_rescue_LED__(ref='D3', value='LED')
    setattr(D3, 'Description', 'Power On Green LED')
    setattr(D3, 'Subsystem', 'Pin13_LED')

    D4 = Arduino_Uno_R3_From_Scratch_rescue_D__(ref='D4', value='1N4148W-7-F')
    setattr(D4, 'Description', 'ATMEGA16U2 ICSP Reset Voltage Spike Protection')
    setattr(D4, 'Subsystem', '16U2_Sub')

    D5 = Arduino_Uno_R3_From_Scratch_rescue_LED__(ref='D5', value='LED')
    setattr(D5, 'Description', 'Serial Tx Green LED')

    D6 = Arduino_Uno_R3_From_Scratch_rescue_LED__(ref='D6', value='LED')

    D7 = Arduino_Uno_R3_From_Scratch_rescue_D__(ref='D7', value='1N4148W-7-F')

    FB1 = Arduino_Uno_R3_From_Scratch_rescue_FILTER__(ref='FB1', value='BLM21PG221SN1D')

    ICSP1 = Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__(ref='ICSP1', value='M20-9980346')
    setattr(ICSP1, 'Description', 'ATMEGA16U2 ICSP Header')
    setattr(ICSP1, 'Subsystem', '16U2_Sub')

    ICSP2 = Arduino_Uno_R3_From_Scratch_rescue_CONN_02X03__(ref='ICSP2', value='M20-9980346')

    J1 = Arduino_Uno_R3_From_Scratch_USB_TYPE_B__(ref='J1', value='USB_TYPE_B')

    JP2 = Arduino_Uno_R3_From_Scratch_rescue_CONN_02X02__(ref='JP2', value='NO_POP')

    MF_MSMF050_2 = Arduino_Uno_R3_From_Scratch_rescue_THERMISTOR__(ref='MF-MSMF050-2', value='500mA')

    P1 = Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__(ref='P1', value='Power Header')
    setattr(P1, 'Description', 'Shield Header 8POS - PWR')

    P2 = Arduino_Uno_R3_From_Scratch_rescue_CONN_01X06__(ref='P2', value='Analog Header')

    P3 = Arduino_Uno_R3_From_Scratch_rescue_CONN_01X10__(ref='P3', value='Digital Header 02')

    P4 = Arduino_Uno_R3_From_Scratch_rescue_CONN_01X08__(ref='P4', value='Digital Header 01')

    Q1 = Arduino_Uno_R3_From_Scratch_rescue_Q_PMOS_GSD__(ref='Q1', value='FDN340P')

    R1 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R1', value='510')
    setattr(R1, 'Characteristics', 'RESISTOR, METAL GLAZE/THICK FILM, 0.125W, 1%, 100ppm, 510ohm, SURFACE MOUNT, 0805')
    setattr(R1, 'Description', 'Power On LED Resistor')
    setattr(R1, 'MFN', 'Yageo')
    setattr(R1, 'MFP', 'RC0805FR-07510RL')
    setattr(R1, 'Subsystem', 'Voltage_Reg')

    R10 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R10', value='510')
    setattr(R10, 'Characteristics', 'RESISTOR, METAL GLAZE/THICK FILM, 0.125W, 1%, 100ppm, 510ohm, SURFACE MOUNT, 0805')
    setattr(R10, 'Description', 'Serial Tx LED Resistor')
    setattr(R10, 'MFN', 'Yageo')
    setattr(R10, 'MFP', 'RC0805FR-07510RL')
    setattr(R10, 'Subsystem', '16U2_Sub')

    R11 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R11', value='510')
    setattr(R11, 'Characteristics', 'RESISTOR, METAL GLAZE/THICK FILM, 0.125W, 1%, 100ppm, 510ohm, SURFACE MOUNT, 0805')
    setattr(R11, 'Description', 'Serial Rx LED Resistor')
    setattr(R11, 'MFN', 'Yageo')
    setattr(R11, 'MFP', 'RC0805FR-07510RL')
    setattr(R11, 'Subsystem', '16U2_Sub')

    R12 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R12', value='1K')
    setattr(R12, 'Characteristics', 'METAL GLAZE/THICK FILM, 0.125W, 5%, 200ppm, 1000ohm, SURFACE MOUNT, 0805,')
    setattr(R12, 'Description', 'ATMEGA328P DTR Pull Down Resistor')
    setattr(R12, 'MFP', 'CRCW08051K00JNEA')

    R13 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R13', value='0')
    setattr(R13, 'Characteristics', 'RES SMD 0.0 OHM JUMPER 1/8W 0805')
    setattr(R13, 'Description', 'ATMEGA328P DTR 0R Link')
    setattr(R13, 'MFN', 'Panasonic')
    setattr(R13, 'MFP', 'ERJ-6GEY0R00V')

    R14 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R14', value='1K')
    setattr(R14, 'Characteristics', 'METAL GLAZE/THICK FILM, 0.125W, 5%, 200ppm, 1000ohm, SURFACE MOUNT, 0805,')
    setattr(R14, 'Description', 'ATMEGA328P Serial Tx Terminator')
    setattr(R14, 'MFP', 'CRCW08051K00JNEA')

    R15 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R15', value='1K')
    setattr(R15, 'Characteristics', 'METAL GLAZE/THICK FILM, 0.125W, 5%, 200ppm, 1000ohm, SURFACE MOUNT, 0805,')
    setattr(R15, 'Description', 'ATMEGA328P Serial Rx Terminator')
    setattr(R15, 'MFP', 'CRCW08051K00JNEA')

    R16 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R16', value='10K')
    setattr(R16, 'Characteristics', 'RESISTOR, METAL GLAZE/THICK FILM, 0.125W, 5%, 200ppm, 10000ohm, SURFACE MOUNT, 0805')
    setattr(R16, 'Description', 'ATMEGA328P 10K ICSP Pull Up')
    setattr(R16, 'MFP', 'CRCW080510K0JNEA')

    R17 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R17', value='1M')

    R2 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R2', value='10K')
    setattr(R2, 'Characteristics', 'RESISTOR, METAL GLAZE/THICK FILM, 0.125W, 5%, 200ppm, 10000ohm, SURFACE MOUNT, 0805')
    setattr(R2, 'Description', '10K Comparator Voltage Divider Resistor')
    setattr(R2, 'MFP', 'CRCW080510K0JNEA')
    setattr(R2, 'Subsystem', 'Voltage_Mgmt')

    R3 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R3', value='10K')
    setattr(R3, 'Characteristics', 'RESISTOR, METAL GLAZE/THICK FILM, 0.125W, 5%, 200ppm, 10000ohm, SURFACE MOUNT, 0805')
    setattr(R3, 'Description', '10K Comparator Voltage Divider Resistor')
    setattr(R3, 'MFP', 'CRCW080510K0JNEA')
    setattr(R3, 'Subsystem', 'Voltage_Mgmt')

    R4 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R4', value='510')
    setattr(R4, 'Characteristics', 'RESISTOR, METAL GLAZE/THICK FILM, 0.125W, 1%, 100ppm, 510ohm, SURFACE MOUNT, 0805')
    setattr(R4, 'Description', 'Power On LED Resistor')
    setattr(R4, 'MFN', 'Yageo')
    setattr(R4, 'MFP', 'RC0805FR-07510RL')
    setattr(R4, 'Subsystem', 'Pin13_LED')

    R5 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R5', value='22R')
    setattr(R5, 'Characteristics', 'RES SMD 22 OHM 5% 1/8W 0805')
    setattr(R5, 'Critical', 'Y')
    setattr(R5, 'Description', '22R USB Termination Resistor')
    setattr(R5, 'MFN', 'Yageo')
    setattr(R5, 'MFP', 'RC0805JR-0722RL')
    setattr(R5, 'Notes', 'Must match 5% tolerance')
    setattr(R5, 'Subsystem', 'USB_Cnxn')

    R6 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R6', value='22R')
    setattr(R6, 'Characteristics', 'RES SMD 22 OHM 5% 1/8W 0805')
    setattr(R6, 'Critical', 'Y')
    setattr(R6, 'Description', '22R USB Termination Resistor')
    setattr(R6, 'MFN', 'Yageo')
    setattr(R6, 'MFP', 'RC0805JR-0722RL')
    setattr(R6, 'Notes', 'Must match 5% tolerance')
    setattr(R6, 'Subsystem', 'USB_Cnxn')

    R7 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R7', value='10K')
    setattr(R7, 'Characteristics', 'RESISTOR, METAL GLAZE/THICK FILM, 0.125W, 5%, 200ppm, 10000ohm, SURFACE MOUNT, 0805')
    setattr(R7, 'Description', 'ATMEGA16U2 10K ICSP Pull Up')
    setattr(R7, 'MFP', 'CRCW080510K0JNEA')
    setattr(R7, 'Subsystem', '16U2_Sub')

    R8 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R8', value='0')
    setattr(R8, 'Characteristics', 'RES SMD 0.0 OHM JUMPER 1/8W 0805')
    setattr(R8, 'Description', 'ATMEGA16U2 UGND to GND Link')
    setattr(R8, 'MFN', 'Panasonic')
    setattr(R8, 'MFP', 'ERJ-6GEY0R00V')
    setattr(R8, 'Subsystem', '16U2_Sub')

    R9 = Arduino_Uno_R3_From_Scratch_rescue_R__(ref='R9', value='1M')
    setattr(R9, 'Description', 'ATMEGA16U2 Xtal 1M Feedback Resistor')
    setattr(R9, 'Subsystem', '16U2_Sub')

    SW1 = Arduino_Uno_R3_From_Scratch_RESET_SWITCH(ref='SW1', value='RESET_SWITCH')

    U1 = Arduino_Uno_R3_From_Scratch_rescue_LD1117S50TR(ref='U1', value='LD1117S50TR')

    U2 = Arduino_Uno_R3_From_Scratch_rescue_LM358(ref='U2', value='LMV358IDGKR')

    U3 = Arduino_Uno_R3_From_Scratch_rescue_LP2985LV__(ref='U3', value='LP2985-33DBVR')

    U4 = MFN_Atmel_ATMEGA16U2_MU(ref='U4', value='ATMEGA16U2-MU')

    U5 = MFN_Atmel_ATMEGA328P_PU__(ref='U5', value='ATMEGA328P')

    VR1 = Arduino_Uno_R3_From_Scratch_rescue_VR__(ref='VR1', value='CG0603MLC-05E')

    VR2 = Arduino_Uno_R3_From_Scratch_rescue_VR__(ref='VR2', value='CG0603MLC-05E')

    X1 = Arduino_Uno_R3_From_Scratch_rescue_Crystal__(ref='X1', value='FOXSLF/160-20')

    X2 = Arduino_Uno_R3_From_Scratch_CERAMIC_RESONATOR__(ref='X2', value='CSTCE16MOV53-R0')


    #===============================================================================
    # Net interconnections between instantiated components.
    #===============================================================================

    Net('/ATMEGA16U2/DTR').connect(R12['1'], U4['13'], C11['1'])

    Net('/ATMEGA16U2/SERIAL_Rx').connect(U4['9'], R14['1'])

    Net('/ATMEGA16U2/SERIAL_Tx').connect(R15['1'], U4['8'])

    Net('/ATMEGA16U2/USB_GND').connect(U4['28'], FB1['1'], R8['1'], J1['4'], C10['1'])

    Net('/ATMEGA16U2/USB_RD+').connect(R5['2'], U4['29'])

    Net('/ATMEGA16U2/USB_RD-').connect(R6['2'], U4['30'])

    Net('/ATMEGA328P/328P_RESET').connect(P1['3'], D7['1'], ICSP2['5'], R13['2'], R16['1'], SW1['4'], SW1['3'], U5['1'])

    Net('/ATMEGA328P/ARD_AN0').connect(U5['23'], P2['1'])

    Net('/ATMEGA328P/ARD_AN1').connect(U5['24'], P2['2'])

    Net('/ATMEGA328P/ARD_AN2').connect(U5['25'], P2['3'])

    Net('/ATMEGA328P/ARD_AN3').connect(P2['4'], U5['26'])

    Net('/ATMEGA328P/ARD_AN4/SDA').connect(P3['9'], P2['5'], U5['27'])

    Net('/ATMEGA328P/ARD_AN5/SCL').connect(P2['6'], P3['10'], U5['28'])

    Net('/ATMEGA328P/ARD_DIG0').connect(R14['2'], P4['8'], U5['2'])

    Net('/ATMEGA328P/ARD_DIG1').connect(R15['2'], P4['7'], U5['3'])

    Net('/ATMEGA328P/ARD_DIG10/SPI_SS').connect(P3['3'], U5['16'])

    Net('/ATMEGA328P/ARD_DIG2').connect(P4['6'], U5['4'])

    Net('/ATMEGA328P/ARD_DIG3').connect(U5['5'], P4['5'])

    Net('/ATMEGA328P/ARD_DIG4').connect(U5['6'], P4['4'])

    Net('/ATMEGA328P/ARD_DIG5').connect(U5['11'], P4['3'])

    Net('/ATMEGA328P/ARD_DIG6').connect(P4['2'], U5['12'])

    Net('/ATMEGA328P/ARD_DIG7').connect(P4['1'], U5['13'])

    Net('/ATMEGA328P/ARD_DIG8').connect(P3['1'], U5['14'])

    Net('/ATMEGA328P/ARD_DIG9').connect(P3['2'], U5['15'])

    Net('/ATMEGA328P/AREF').connect(P3['8'], U5['21'], C14['1'])

    Net('328P_ICSP_MISO').connect(P3['5'], U5['18'], ICSP2['1'])

    Net('328P_ICSP_MOSI').connect(ICSP2['4'], P3['4'], U5['17'])

    Net('328P_ICSP_SCK').connect(U2['5'], ICSP2['3'], P3['6'], U5['19'])

    Net('3V3_LDO').connect(U2['2'], U3['5'], C6['1'], P1['4'])

    Net('5V_LDO').connect(Q1['2'], ICSP2['2'], C2['1'], U5['7'], U4['4'], C9['1'], U5['20'], R1['2'], ICSP1['2'], U2['8'], C4['2'], R16['2'], C15['1'], C5['1'], U3['1'], U3['3'], U2['8'], D7['2'], U4['32'], R11['2'], R10['2'], D4['2'], R7['2'], P1['2'], U1['2'], P1['5'], C3['1'])

    Net('GND').connect(C14['2'], C15['2'], U1['1'], U2['4'], P1['6'], P3['7'], P1['7'], C3['2'], C6['2'], C5['2'], R3['1'], C4['1'], SW1['2'], SW1['1'], C1['2'], D2['1'], U5['22'], C2['2'], U5['8'], CON1['1'], X2['2'], ICSP1['6'], U4['3'], U4['33'], D3['1'], C8['1'], R8['2'], C9['2'], C7['1'], R12['2'], U2['4'], ICSP2['6'], U3['2'])

    Net('ICSP_MISO').connect(ICSP1['1'], U4['17'])

    Net('ICSP_MOSI').connect(ICSP1['4'], U4['16'])

    Net('ICSP_SCK').connect(U4['15'], ICSP1['3'])

    Net('Net-(C10-Pad2)').connect(U4['27'], C10['2'])

    Net('Net-(C11-Pad2)').connect(R13['1'], C11['2'])

    Net('Net-(C7-Pad2)').connect(X1['2'], R9['1'], C7['2'], U4['2'])

    Net('Net-(C8-Pad2)').connect(R9['2'], C8['2'], X1['1'], U4['1'])

    Net('Net-(CON1-Pad2)').connect(D1['2'], CON1['2'], CON1['3'])

    Net('Net-(D2-Pad2)').connect(R1['1'], D2['2'])

    Net('Net-(D3-Pad2)').connect(D3['2'], R4['2'])

    Net('Net-(D4-Pad1)').connect(U4['24'], R7['1'], ICSP1['5'], D4['1'])

    Net('Net-(D5-Pad1)').connect(D5['1'], U4['11'])

    Net('Net-(D5-Pad2)').connect(D5['2'], R10['1'])

    Net('Net-(D6-Pad1)').connect(D6['1'], U4['10'])

    Net('Net-(D6-Pad2)').connect(D6['2'], R11['1'])

    Net('Net-(FB1-Pad2)').connect(J1['6'], J1['5'], VR2['2'], VR1['2'], FB1['2'])

    Net('Net-(J1-Pad1)').connect(J1['1'], MF_MSMF050_2['1'])

    Net('Net-(J1-Pad2)').connect(R5['1'], VR2['1'], J1['2'])

    Net('Net-(J1-Pad3)').connect(VR1['1'], R6['1'], J1['3'])

    Net('Net-(JP2-Pad1)').connect(JP2['1'], U4['18'])

    Net('Net-(JP2-Pad2)').connect(JP2['2'], U4['21'])

    Net('Net-(JP2-Pad3)').connect(JP2['3'], U4['19'])

    Net('Net-(JP2-Pad4)').connect(U4['20'], JP2['4'])

    Net('Net-(P1-Pad1)').connect(P1['1'])

    Net('Net-(Q1-Pad1)').connect(Q1['1'], U2['1'])

    Net('Net-(R17-Pad1)').connect(U5['10'], X2['1'], R17['1'])

    Net('Net-(R17-Pad2)').connect(X2['3'], R17['2'], U5['9'])

    Net('Net-(R2-Pad1)').connect(U2['3'], R2['1'], R3['2'])

    Net('Net-(R4-Pad1)').connect(R4['1'], U2['6'], U2['7'])

    Net('Net-(U3-Pad4)').connect(U3['4'])

    Net('Net-(U4-Pad12)').connect(U4['12'])

    Net('Net-(U4-Pad14)').connect(U4['14'])

    Net('Net-(U4-Pad22)').connect(U4['22'])

    Net('Net-(U4-Pad23)').connect(U4['23'])

    Net('Net-(U4-Pad25)').connect(U4['25'])

    Net('Net-(U4-Pad26)').connect(U4['26'])

    Net('Net-(U4-Pad5)').connect(U4['5'])

    Net('Net-(U4-Pad6)').connect(U4['6'])

    Net('Net-(U4-Pad7)').connect(U4['7'])

    Net('USBVCC').connect(Q1['3'], U4['UVCC'], MF_MSMF050_2['2'])

    Net('Vin').connect(D1['1'], P1['8'], U1['3'], C1['1'], R2['2'])


#===============================================================================
# Instantiate the circuit and generate the netlist.
#===============================================================================

if __name__ == "__main__":
    _home_rcl_arduino_uno_r3_from_scratch_Arduino_Uno_R3_From_Scratch_sch()
    generate_netlist()
