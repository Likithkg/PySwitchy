class switchy():
    def add_case(self, list):
        case = {}
        for index, item in enumerate(list):
            case[index] = item
        return case

    def switch(self, case,option):
        try:
            return case[option]
        except Exception as e:
            return "wrong choice enter another option"


