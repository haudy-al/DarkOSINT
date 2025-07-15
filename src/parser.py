import re

class LeakParser:
    def __init__(self, regex_patterns):
        self.regex_patterns = regex_patterns

    def extract_all(self, html):
        results = {}
        for key, pattern in self.regex_patterns.items():
            matches = re.findall(pattern, html, re.IGNORECASE)
            if matches:
                results[key] = list(set(matches))  
        return results
