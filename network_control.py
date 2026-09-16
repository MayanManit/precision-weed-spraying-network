
def calculate_checksum(sequence_id, zone_id, spray_class, duration):
    data = f"{sequence_id}|{zone_id}|{spray_class}|{duration}"
    checksum = 0

    for character in data:
        checksum += ord(character)

    return checksum % 256


def create_packet(sequence_id, zone_id, spray_class, duration):
    checksum = calculate_checksum(
        sequence_id,
        zone_id,
        spray_class,
        duration
    )

    packet = {
        "sequence_id": sequence_id,
        "zone_id": zone_id,
        "spray_class": spray_class,
        "duration": duration,
        "checksum": checksum
    }

    return packet


def validate_packet(packet):
    required_fields = [
        "sequence_id",
        "zone_id",
        "spray_class",
        "duration",
        "checksum"
    ]

    for field in required_fields:
        if field not in packet:
            return False

    expected_checksum = calculate_checksum(
        packet["sequence_id"],
        packet["zone_id"],
        packet["spray_class"],
        packet["duration"]
    )

    return packet["checksum"] == expected_checksum


def generate_ack(packet):
    if validate_packet(packet):
        return f"ACK-{packet['sequence_id']}"
    else:
        return "NACK"


def process_packet(sequence_id, zone_id, spray_class, duration):
    packet = create_packet(
        sequence_id,
        zone_id,
        spray_class,
        duration
    )

    valid = validate_packet(packet)
    acknowledgement = generate_ack(packet)

    return packet, valid, acknowledgement
