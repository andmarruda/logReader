from src.filter import filter

class pgsqlAuthFailed:
    @staticmethod
    def getFilter():
        regex = r"invalid length of startup packet|password authentication failed|password does not match|no postgresql user name specified in startup packet"
        return filter(regex)