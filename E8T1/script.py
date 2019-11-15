# The signatures of this class and its public methods are required for the automated
# grading to work. You must not change the names or the list of parameters. You may
# introduce private/protected utility methods though.


class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = list(template)

    def __clean(self, profanity):
        if len(profanity) > len(self.__template):
            difference = len(profanity) - len(self.__template)

            for i in range(difference):
                self.__template.append(self.__template[i])

            profanity = "".join(self.__template)
            return profanity

        else:
            profanity = "".join(self.__template[:len(profanity)])
            return profanity

    def __sort(self):
        self.__keywords = sorted(self.__keywords, key=len, reverse=True)
        return self.__keywords

    def __case_insensitive_replace(self, old, new, text):
        idx = 0
        while idx < len(text):
            index_l = text.lower().find(old.lower(), idx)
            if index_l == -1:
                return text
            text = text[:index_l] + new + text[index_l + len(old):]
            idx = index_l + len(new)
        return text

    def filter(self, msg):
        self.__keywords = self.__sort()

        for key in self.__keywords:
            if key.lower() in msg.lower():
                replacement = self.__clean(key)
                msg = self.__case_insensitive_replace(key, replacement, msg)

        return msg

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno