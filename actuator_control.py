
NOZZLE_MAP = {
    "Z1": "N1",
    "Z2": "N2",
    "Z3": "N3",
    "Z4": "N4"
}

DURATION_MAP = {
    "NO_SPRAY": 0,
    "LOW": 250,
    "MEDIUM": 500,
    "HIGH": 750
}


def get_nozzle(zone_id):
    if zone_id not in NOZZLE_MAP:
        raise ValueError("Invalid zone ID")

    return NOZZLE_MAP[zone_id]


def get_actuator_state(spray_class):
    if spray_class == "NO_SPRAY":
        return "OFF"
    elif spray_class in ["LOW", "MEDIUM", "HIGH"]:
        return "ON"
    else:
        raise ValueError("Invalid spray class")


def get_duration(spray_class):
    if spray_class not in DURATION_MAP:
        raise ValueError("Invalid spray class")

    return DURATION_MAP[spray_class]


def control_actuator(zone_id, spray_class):
    nozzle = get_nozzle(zone_id)
    state = get_actuator_state(spray_class)
    duration = get_duration(spray_class)

    return {
        "zone_id": zone_id,
        "nozzle": nozzle,
        "state": state,
        "duration": duration
    }

