class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # localName@ domainName

        # . in localName => email will forward to localName without .
        # + in localName => email will forward to localName before the +
        mail = set()
        for email in emails:
            domain = email[email.index('@'):]

            local = email[:email.index('@')]
            if '+' in local:
                local = local[:local.index('+')]
            email = local.replace('.', '') + domain
            mail.add(email)
        return len(mail)