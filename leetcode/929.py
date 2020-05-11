from typing import *
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def simplifyEmails(email):
            # find the @
            at_loc = email.find('@')
            # find the + in the first part
            plus_loc = email.find('+')
            # find the useful parts
            if plus_loc > at_loc or plus_loc == -1:
                end_loc = at_loc
            else:
                end_loc = plus_loc
            useful = email[:end_loc]
            # go through useful to eliminate '.'
            simplified = ''
            for char in useful:
                if char == ".":
                    continue
                simplified += (char)
            print('u:', useful)
            print('s:', simplified)
            print('at: ', email[at_loc:])
            return simplified + email[at_loc:]
        
        unique_addrs = {}
        for email in emails:
            simplified_email = simplifyEmails(email)
            print(email, '-->', simplified_email)
            if simplified_email not in unique_addrs:
                unique_addrs[simplified_email] = 1
        return len(unique_addrs)
        
