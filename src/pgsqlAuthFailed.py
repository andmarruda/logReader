from src.filter import filter

class pgsqlAuthFailed(filter):
    def getRegEx(self):
        return "invalid length of startup packet|password authentication failed|password does not match|no postgresql user name specified in startup packet"