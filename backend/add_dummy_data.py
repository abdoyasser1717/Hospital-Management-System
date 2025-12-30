# add_english_dummy.py
"""
Add English dummy data to the hospital management system
Run: python add_english_dummy.py
"""

import json
import random
from backend.doctor import Doctor
from backend.patient import Patient
from backend.storage import save_data, serialize_specializations, load_data


def add_english_dummy_data():
    """
    Add English-only dummy data to the system
    """
    print("⚡ Starting English dummy data generation...")

    # English names
    ENGLISH_FIRST_NAMES = [
        "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph",
        "Thomas", "Charles", "Christopher", "Daniel", "Matthew", "Anthony", "Donald",
        "Mark", "Paul", "Steven", "Andrew", "Kenneth", "Joshua", "Kevin", "Brian",
        "George", "Edward", "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth",
        "Barbara", "Susan", "Jessica", "Sarah", "Karen", "Nancy", "Lisa", "Margaret",
        "Betty", "Sandra", "Ashley", "Dorothy", "Kimberly", "Emily", "Donna",
        "Michelle", "Carol", "Amanda", "Melissa", "Deborah"
    ]

    ENGLISH_LAST_NAMES = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
        "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
        "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
        "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King",
        "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
        "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
        "Carter", "Roberts"
    ]

    # Load current data
    current_data = load_data()

    if not current_data:
        print("📝 No existing data found, creating new structure...")
        # Create default structure
        current_data = {}
        specializations = [
            "General Medicine", "Emergency", "Cardiology", "Orthopedics",
            "Neurology", "Surgery", "Pediatrics", "ENT", "Dermatology",
            "Gynecology & Obstetrics", "ICU", "Radiology", "Laboratory"
        ]
        for spec in specializations:
            current_data[spec] = {
                "doctors": [],
                "status": {0: [], 1: [], 2: []}
            }

    print("👨‍⚕️ Adding English doctors...")
    # Add 2 English doctors per specialization
    for spec in list(current_data.keys())[:5]:  # Add to first 5 specializations
        for i in range(2):
            first_name = random.choice(ENGLISH_FIRST_NAMES)
            last_name = random.choice(ENGLISH_LAST_NAMES)
            doctor_name = f"Dr. {first_name} {last_name}"

            # Check if doctor already exists
            existing_names = [d.name for d in current_data[spec]["doctors"]]
            if doctor_name not in existing_names:
                doctor = Doctor(doctor_name, spec)
                current_data[spec]["doctors"].append(doctor)

    print("👤 Adding English patients...")
    # Add English patients with different statuses
    for spec in list(current_data.keys())[:5]:  # Add to first 5 specializations
        # Normal patients (status 0)
        for i in range(3):
            first_name = random.choice(ENGLISH_FIRST_NAMES)
            last_name = random.choice(ENGLISH_LAST_NAMES)
            patient_name = f"{first_name} {last_name}"
            patient = Patient(patient_name, 0)
            current_data[spec]["status"][0].append(patient)

        # Urgent patients (status 1)
        for i in range(2):
            first_name = random.choice(ENGLISH_FIRST_NAMES)
            last_name = random.choice(ENGLISH_LAST_NAMES)
            patient_name = f"{first_name} {last_name}"
            patient = Patient(patient_name, 1)
            current_data[spec]["status"][1].append(patient)

        # Super urgent patients (status 2)
        for i in range(1):
            first_name = random.choice(ENGLISH_FIRST_NAMES)
            last_name = random.choice(ENGLISH_LAST_NAMES)
            patient_name = f"{first_name} {last_name}"
            patient = Patient(patient_name, 2)
            current_data[spec]["status"][2].append(patient)

    print("💾 Saving data...")
    # Save the updated data
    serialized_data = serialize_specializations(current_data)
    save_data(serialized_data)

    # Calculate statistics
    total_doctors = sum(len(data["doctors"]) for data in current_data.values())
    total_patients = sum(
        len(patients)
        for data in current_data.values()
        for patients in data["status"].values()
    )

    print("\n" + "=" * 50)
    print("✅ English dummy data added successfully!")
    print("=" * 50)
    print(f"🏥 Specializations: {len(current_data)}")
    print(f"👨‍⚕️ Total doctors: {total_doctors}")
    print(f"👤 Total patients: {total_patients}")
    print("=" * 50)

    # Show sample of what was added
    print("\n📋 Sample of added data (General Medicine):")
    print("-" * 40)
    if "General Medicine" in current_data:
        data = current_data["General Medicine"]
        print("Doctors:")
        for doctor in data["doctors"][:2]:  # Show first 2 doctors
            print(f"  - {doctor.name}")

        print("\nPatients (Normal):")
        for patient in data["status"][0][:2]:  # Show first 2 normal patients
            print(f"  - {patient.name}")

    return current_data


def quick_english_generate():
    """
    Quick function to generate English dummy data
    """
    try:
        data = add_english_dummy_data()
        print("\n🎉 English dummy data ready!")
        print("\nYou can now:")
        print("1. Run the system: python script.py")
        print("2. View doctors: Option 8")
        print("3. View patients: Option 2")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


if __name__ == "__main__":
    print("🏥 English Dummy Data Generator")
    print("-" * 40)
    quick_english_generate()