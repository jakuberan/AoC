class Passport:
    """
    This class represents a passport together with validator methods
    """

    # Content fields
    string = ""
    data = {"byr": 0, "iyr": 0, "eyr": 0, "hgt": "", "hcl": "", "ecl": "", "pid": 0}

    # Validation data
    valid_values = {
        "byr": [1920, 2002],
        "iyr": [2010, 2020],
        "eyr": [2020, 2030],
        "hgt": {"cm": [150, 193], "in": [59, 76]},
        "hcl": "0123456789abcdef",
        "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    }

    def __init__(
        self,
    ):
        """ Initializes empty passport """
        self.string = ""

    def display_string(self):
        """ Prints passport string data """
        print(self.string)

    def display_data(self):
        """ Prints passport parsed data """
        print(self.data)

    def add_data(self, new_data):
        """ Adds passport data """
        if self.string != "":
            self.string += " "
        self.string += new_data.strip()

    def get_string(self):
        """ Return passport string """
        return self.string

    def get_data(self):
        """ Return passport data """
        return self.data

    def update_data(self, values, fields):
        """ Updates all passport values"""
        for f in self.data.keys():
            self.data[f] = values[fields.index(f)]

    def valid_year(self, ytype):
        """ Validates passport data -- year """

        # Check lenght
        if len(self.data[ytype]) != 4:
            return False

        # Check if this is an integer
        try:
            year = int(self.data[ytype])
        except:
            return False

        # Check ranges
        return (
            self.valid_values[ytype][0] <= year and year <= self.valid_values[ytype][1]
        )

    def valid_pid(self):
        """ Validates passport data -- Passport ID """

        # Check lenght
        if len(self.data["pid"]) != 9:
            return False

        # Check if this is an integer
        try:
            int(self.data["pid"])
        except:
            return False

        # Return true
        return True

    def valid_hgt(self):
        """ Validates passport data -- Height """

        # Check lenght
        if len(self.data["hgt"]) < 4:
            return False

        # Obtain measure
        length = len(self.data["hgt"])
        heig = self.data["hgt"][0 : (length - 2)]
        unit = self.data["hgt"][(length - 2) : length]

        # Check unit
        if unit not in self.valid_values["hgt"].keys():
            return False

        # Check height validity
        try:
            heig = int(heig)
        except:
            return False

        # Check height range
        return (
            self.valid_values["hgt"][unit][0] <= heig
            and heig <= self.valid_values["hgt"][unit][1]
        )

    def valid_ecl(self):
        """ Validates passport data -- Eye Color """
        return self.data["ecl"] in self.valid_values["ecl"]

    def valid_hcl(self):
        """ Validates passport data -- Hair Color """
        # Check hair color lenght and first character
        if len(self.data["hcl"]) != 7:
            return False
        if self.data["hcl"][0] != "#":
            return False

        # Check hair color characters
        return 0 not in [c in self.valid_values["hcl"] for c in self.data["hcl"][1:]]

    def validate(self):
        """ Validates passport data """
        fields = [d.split(":")[0] for d in self.string.split()]
        values = [d.split(":")[1] for d in self.string.split()]

        # Validate fields
        if len(list(set(self.data.keys()) - set(fields))) > 0:
            return False

        # Update all values
        self.update_data(values, fields)

        # Validate values
        return (
            self.valid_year("byr")
            and self.valid_year("iyr")
            and self.valid_year("eyr")
            and self.valid_pid()
            and self.valid_ecl()
            and self.valid_hcl()
            and self.valid_hgt()
        )
