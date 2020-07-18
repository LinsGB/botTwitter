from src import twitterMethods,date
from src.Texts import Texts
from src.ApiGenerator import ApiGenerator

def main():
    apiGenerator = ApiGenerator()
    api = apiGenerator.createApi()
    #twitterMethods.searchTweets(api)
    twitterMethods.streamStatus(api)
    #uppdateStatus(api)

if __name__ == "__main__":
    main()
    #"quero emagrecer", "preciso emagrecer", "ajuda a emagrecer", "to gorda", "odeio meu corpo"

    