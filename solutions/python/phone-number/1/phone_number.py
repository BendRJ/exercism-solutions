class PhoneNumber:
    def __init__(self, input_no: str):
        print("1. In __init__, about to set self.number")
        self.number = input_no # triggers number setter if specified
        print("4. Back in __init__, setter finished")

    @property
    def number(self):
        print("   Getting number")
        return self._number #getter
    
    @number.setter
    def number(self, value):
        print(f"2. Setter called with value: {value}")
        if len(value) < 10: 
            raise ValueError("must not be fewer than 10 digits")
        if any(letter for letter in value if letter in ("@",":","!")):
            raise ValueError("punctuations not permitted")
        
        cleaned = value.strip().strip("+").replace(" ","").replace("-","").replace(".","").replace(")","").replace("(","")

        if len(cleaned) == 11 and cleaned[:1] not in ("1"):
            raise  ValueError("11 digits must start with 1")
        if len(cleaned) == 11 and cleaned[1:2] in ("0"):
            raise ValueError(f"area code cannot start with zero")
        if len(cleaned) == 11 and cleaned[1:2] in ("1"):
            raise ValueError(f"area code cannot start with one")
        if len(cleaned) == 10 and cleaned[0:1] in ("0"):
            raise ValueError(f"area code cannot start with zero")
        if len(cleaned) == 10 and cleaned[0:1] in ("1"):
            raise ValueError(f"area code cannot start with one")
        if len(cleaned) == 11 and cleaned[4:5] in ("0"):
            raise ValueError(f"exchange code cannot start with zero")
        if len(cleaned) == 11 and cleaned[4:5] in ("1"):
            raise ValueError(f"exchange code cannot start with one")
        if len(cleaned) == 10 and cleaned[3:4] in ("0"):
            raise ValueError(f"exchange code cannot start with zero")
        if len(cleaned) == 10 and cleaned[3:4] in ("1"):
            raise ValueError(f"exchange code cannot start with one")
        if len(cleaned) == 11 and cleaned[:1] == "1":
            cleaned = cleaned.strip("1")
        elif len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")

        try:
            cleaned = int(cleaned)
        except:
            raise ValueError("letters not permitted")
        cleaned = str(cleaned)

        print(f"3. Validation passed, storing in _number")
        self._number = cleaned  # if the setter tried to set `self.number` it would call itself indefinitely
        # Result: 'number' is NOT in __dict__ only '_number' is
    
    def pretty(self):
        print("Formatting input number...")
        if self._number[:1] == "1":
            self._number = self._number[1:]

        area_code = self._number[:3]
        exchange_code = self._number[3:6]
        residual = self._number[6:]

        return f"({area_code})-{exchange_code}-{residual}"
        
    @property
    def area_code(self):
        print(f"Returning area code.")
        #print(self)
        return str(self._number)[:3]

if __name__ == "__main__":
    test1 = PhoneNumber("12234567890")
    print(test1.__dict__)
    print(test1.number)
    print(test1.area_code)
    print(test1.pretty())