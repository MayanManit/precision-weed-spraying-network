
from weed_density import analyze_zone
from network_control import process_packet
from actuator_control import control_actuator


def main():
    zones = [
        ("Z1", 0, 100),
        ("Z2", 6, 100),
        ("Z3", 18, 100),
        ("Z4", 34, 100)
    ]

    sequence_id = 1

    print("Precision Weed Spraying Network")
    print("--------------------------------")

    for zone_id, weed_area, total_area in zones:
        density_result = analyze_zone(weed_area, total_area)

        coverage = density_result["coverage"]
        spray_class = density_result["density"]

        actuator = control_actuator(zone_id, spray_class)

        packet, valid, ack = process_packet(
            sequence_id,
            zone_id,
            spray_class,
            actuator["duration"]
        )

        print(
            f"{zone_id}  {coverage:5.2f}%  "
            f"{spray_class:9}  "
            f"{actuator['nozzle']}  "
            f"{actuator['state']:3}  "
            f"{actuator['duration']:3} ms  "
            f"{ack}"
        )

        if not valid:
            print("Packet validation failed")

        sequence_id += 1


if __name__ == "__main__":
    main()


