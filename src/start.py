from twitterMethods import streamStatusUpdate
from createApi import createApi

def main(filterText):
    api = createApi("jZtq1SB2W5v0z3Mq18CUMq6pq", "sLyYO4gXKRPQajhknkrOYdgTEwS4x5tG1ys84Ba24RKspxF16w",
                     "875414705388621825-IBVLxPYrMTRH9Fn2rnhpWPouku24dKR", "AqUEbNn0c9PWERPKuHDGX7gS4W5ih2YtUOB0jVsG2AUJo")
    streamStatusUpdate(api, filterText)

if __name__ == "__main__":
    main(["teste do biel"])