# -- coding: utf-8 --
msfs_mode = 1
icao = "wssl"

theShed = CustomizedName("SYFC Shed | Bay #§", 5)
alpha = CustomizedName("A | Bay #§", 1)
bravo = CustomizedName("B | Bay #§", 2)
charlie = CustomizedName("C | Bay #§", 3)
delta = CustomizedName("D | Bay #§", 4)
fuel = CustomizedName("Refueling | Bay #§", 6)


@AlternativeStopPositions
def offset(aircraftData):
    offset = {
        42: 8.2,
        170: 8.2,
        175: 8.2,
        190: 8.3,
        195: 8.3,
        318: 8.1,
        319: 8.1,
        320: 8.3,
        321: 8.2,
        737: 8.2,
    }

    try:
        return Distance.fromMeters(offset.get(aircraftData.idMajor, 0))
    except:
        return Distance.fromMeters(0)


parkings = {
    PARKING : {
        None : (theShed, offset),
    },
    GATE_A: {
        None : (alpha, offset),
    },
    GATE_B: {
        None: (bravo, offset),
    },
    GATE_C: {
        None : (charlie, offset),
    },
    GATE_D: {
        None : (delta, offset),
    },
    GATE_R: {
        None : (fuel, offset),
    }
}
