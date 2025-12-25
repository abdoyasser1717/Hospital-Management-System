def input_valid(name: str) -> str|None:
    """
    Check name validity:
    - letters only
    - spaces allowed
    - prints error if invalid
    """
    if not name or not name.strip():
        print("Name cannot be empty")
        return None

    name = name.strip()

    for part in name.split():
        if not part.isalpha():
            print("Name must contain letters only")
            return None

    return name
SPECIALIZATIONS = {
    "general medicine": "General Medicine",
    "emergency": "Emergency",
    "cardiology": "Cardiology",
    "orthopedics": "Orthopedics",
    "neurology": "Neurology",
    "surgery": "Surgery",
    "pediatrics": "Pediatrics",
    "ent": "ENT",
    "dermatology": "Dermatology",
    "gynecology & obstetrics": "Gynecology & Obstetrics",
    "icu": "ICU",
    "radiology": "Radiology",
    "laboratory": "Laboratory"
}

def check_input_specialization(specialization: str) -> str | None:
    specialization = specialization.strip().lower()

    result = SPECIALIZATIONS.get(specialization)
    if not result:
        print("Please enter a valid specialization.")
    return result
if __name__ == '__main__':
    input_valid("Enter a number")
    print(check_input_specialization("General medicine"))
    if not check_input_specialization("General aedicine"):
        print("Specializations not found")






