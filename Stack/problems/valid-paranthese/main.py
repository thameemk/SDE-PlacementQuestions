
class ValidParanthese:

    @staticmethod
    def is_valid_paranthese(paranthese:str)->bool:
        _paranthese = {
            '{':'}',
            '[':']',
            '(':')'
        }

        if paranthese.count('(')!=paranthese.count(')') or paranthese.count('[')!=paranthese.count(']') or paranthese.count('{')!=paranthese.count('}'):
            return False

        stack = []

        for each_chara in paranthese:
            if each_chara in _paranthese:
                stack.append(_paranthese[each_chara])
            else:
                if len(stack)==0 or each_chara!=stack.pop():
                    return False

        return True

if __name__=='__main__':
    paranthese = "()[]{}"
    response = ValidParanthese.is_valid_paranthese(paranthese=paranthese)
    print(response)