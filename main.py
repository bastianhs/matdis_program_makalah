# Adjacency matrix that represents blood type compatibility

matrix_blood_transfusion = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1],
]

# Function for converting blood types into matrix indices

def get_blood_type_index(abo, rh):
    match abo:
        case "O":
            match rh:
                case "+":
                    return 0
                case "-":
                    return 1
        case "A":
            match rh:
                case "+":
                    return 2
                case "-":
                    return 3
        case "B":
            match rh:
                case "+":
                    return 4
                case "-":
                    return 5
        case "AB":
            match rh:
                case "+":
                    return 6
                case "-":
                    return 7

# Function for checking value in the matrix

def is_compatible(donor, recipient):
    return 1 == matrix_blood_transfusion[donor][recipient]


# Main program

# Get input from user and validate the input

while True:
    abo_donor = input("Masukkan golongan darah ABO pendonor (O/A/B/AB): ")
    if abo_donor in ["O", "A", "B", "AB"]:
        break
    
    print("Masukan tidak valid !")

while True:
    rh_donor = input("Masukkan golongan darah rh pendonor (+/-): ")
    if rh_donor in ["+", "-"]:
        break
    
    print("Masukan tidak valid !")

while True:
    abo_recipient = input("Masukkan golongan darah ABO penerima (O/A/B/AB): ")
    if abo_recipient in ["O", "A", "B", "AB"]:
        break

    print("Masukan tidak valid !")

while True:
    rh_recipient = input("Masukkan golongan darah rh penerima (+/-): ")
    if rh_recipient in ["+", "-"]:
        break

    print("Masukan tidak valid !")

# Get blood type index from user input

index_donor = get_blood_type_index(abo_donor, rh_donor)
index_recipient = get_blood_type_index(abo_recipient, rh_recipient)

# Check for blood transfusion compatibility

if is_compatible(index_donor, index_recipient):
    print("Transfusi darah dapat dilakukan")
else:
    print("Transfusi darah tidak dapat dilakukan")
