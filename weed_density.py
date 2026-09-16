
def calculate_coverage(weed_area, total_area):
    if total_area <= 0:
        raise ValueError("Total area must be greater than zero")
    if weed_area < 0 or weed_area > total_area:
        raise ValueError("Weed area must be between 0 and total area")

    return (weed_area / total_area) * 100


def classify_density(coverage):
    if coverage == 0:
        return "NO_SPRAY"
    elif coverage < 10:
        return "LOW"
    elif coverage < 25:
        return "MEDIUM"
    else:
        return "HIGH"


def analyze_zone(weed_area, total_area):
    coverage = calculate_coverage(weed_area, total_area)
    density = classify_density(coverage)

    return {
        "coverage": coverage,
        "density": density
    }