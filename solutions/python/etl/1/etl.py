legacy_data = {
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"],
        }


def transform(legacy_data):
    solution = dict()
    for key, value in legacy_data.items():
        for letter in value:
            solution[letter.lower()] = key

    return solution

transform(legacy_data)