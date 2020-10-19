
class JsObject:
    def __init__(self, dictionary: dict):
        self.__dictionary = dictionary
        
        for x in dictionary:
            if type(dictionary[x]) not in [type({}), type([])]: setattr(self, x, dictionary[x])
            else:
                if type(dictionary[x]) == type({}): setattr(self, x, JsObject(dictionary[x]))
                else:
                    def loop(obj, objs):
                        for z in objs:
                            if type(z) == type({}): obj.append(JsObject(z))
                            elif type(z) == type([]): obj.append(loop([], z))
                            else: obj.append(z)
                        return obj
                    setattr(self, x, loop([], dictionary[x]))

    def items(self):
        return self.__dictionary

    def __getitem__(self, value):
        return self.__dictionary[value]

    def __setitem__(self, value, newvalue):
        print(newvalue, value)
        self.__dictionary[value] = newvalue

    def __iter__(self):
        for x in self.__dictionary:
            yield x

    def __len__(self):
        return len(self.__dictionary)

    def __str__(self):
        def loop(s, d):
            if type(d) in [type({}), type(JsObject)]:
                if len(d) == 0:s += "{}";return s
                s += "{"
                for k, v in d.items():
                    if not type(v) in [type({}), type([])]:
                        s += f"{k}: {v}, "
                    else:
                        s += f"""{k}: {loop("",v)}, """
                return s[:-2] + "}"
            else:
                if len(d) == 0:s += "[]";return s
                s += "["
                for k in d:
                    if not type(k) in [type({}), type([])]:
                        s += f"{k}, "
                    else:
                        s += f"""{loop("", k)}, """
                return s[:-2] + "]"
        return loop("", self.__dictionary)

    def __repr__(self):
        def loop(s, d):
            if type(d) in [type({}), type(JsObject)]:
                if len(d) == 0:s += "{}";return s
                s += "{"
                for k, v in d.items():
                    if not type(v) in [type({}), type([])]:
                        s += f"{k}: {v}, "
                    else:
                        s += f"""{k}: {loop("",v)}, """
                return s[:-2] + "}"
        return f"""<JsObject {loop("", self.__dictionary)}>"""


