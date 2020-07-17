from src import twitterMethods, ApiGenerator, Texts

def main(filterText):
    apiGenerator = ApiGenerator()
    api = apiGenerator.createApi()
    twitterMethods.streamStatus(api, filterText)
    #uppdateStatus(api)

if __name__ == "__main__":
    texts = Texts()
    main(texts.getWords())
    #"quero emagrecer", "preciso emagrecer", "ajuda a emagrecer", "to gorda", "odeio meu corpo"

    