class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @classmethod
    def with_engraving(cls, text):
        if LuxuryWatch.check_text(text):
            _watch = cls()
            _watch.text = text
            return _watch
        else:
            raise Exception(text + ' - it does not follow the "alpha" rule')

    @staticmethod
    def check_text(text):
        if len(text) > 40:
            return False
        if not text.isalpha():
            return False
        return True


print('Watches created so far:', LuxuryWatch.get_number_of_watches_created())
w1 = LuxuryWatch()
print('Number of watches created:', LuxuryWatch.get_number_of_watches_created())
w2 = LuxuryWatch.with_engraving('Alabama')
print('Alabama was created, so overall # is:', LuxuryWatch.get_number_of_watches_created())

try:
    w3 = LuxuryWatch.with_engraving('foo@foo.com')
except Exception as e:
    print('The problem is:', e)

print('Watches created so far:', LuxuryWatch.get_number_of_watches_created())