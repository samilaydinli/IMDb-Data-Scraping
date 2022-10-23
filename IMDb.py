import requests,json,time,re,textwrap

class Film():
    def __init__(self):
        self.loop = True
    
    def program(self):
        choice = self.menu()

        if choice == "1":
            self.top250movies()
        if choice == "2":
            self.mostPopularmovies()
        if choice == "3":
            self.inTheaters()
        if choice == "4":
            self.boxOfficeAllTime()
        if choice == "5":
            self.searchMovie()
        if choice == "6":
            self.quit()

    def menu(self):
        def control(choice):
            if re.search("[^1-6]",choice):
                raise Exception("Please enter a value between 1 and 6")
        while True:
            try:
                choice = input("Welcome to xxx IMDb Platform...\n\nPlease make your choice...\n\n[1]-Top 250 Movies\n[2]-Most Popular Movies\n[3]-InTheaters\n[4]-Box Office All Time\n[5]-Search a Movie\n[6]-Log Out\n\n")
                control(choice)
            except Exception as error:
                print(error)
                time.sleep(2)
            else:
                break
        return choice

    def top250movies(self):
        print("Loading Top 250 Movies List...\n\n")
        time.sleep(2)
        url = requests.get("https://imdb-api.com/en/API/Top250Movies/k_rs97zh2v")
        list = url.json()
        for i in list["items"]:
            title = i["fullTitle"]
            rank = i["rank"]
            print("{}-{}".format(rank,title))
        self.returnToMenu()

    def mostPopularmovies(self):
        print("Loading Most Popular Movies List...\n\n")
        time.sleep(2)
        url = requests.get("https://imdb-api.com/en/API/MostPopularMovies/k_rs97zh2v")
        list = url.json()
        for i in list["items"]:
            title = i["fullTitle"]
            rank = i["rank"]
            print("{}-{}".format(rank,title))
        self.returnToMenu()

    def inTheaters(self):
        print("Loading InTheaters List...\n\n")
        time.sleep(2)
        url = requests.get("https://imdb-api.com/en/API/InTheaters/k_rs97zh2v")
        list = url.json()
        counter =1
        for i in list["items"]:
            title = i["fullTitle"]
            date = i["releaseState"]
            print(str(counter)+"-"+title+" - "+date)
            counter+=1
        self.returnToMenu()


    def boxOfficeAllTime(self):
        print("Loading Box Office All Time Movies List...\n\n")
        time.sleep(2)
        url = requests.get("https://imdb-api.com/en/API/BoxOfficeAllTime/k_rs97zh2v")
        list = url.json()
        for i in list["items"]:
            title = i["title"]
            rank = i["rank"]
            gross = i["worldwideLifetimeGross"]
            print("{}-{} - Worldwide Lifetime Gross: {}".format(rank,title,gross))
        self.returnToMenu()


    def searchMovie(self):
        print("Movie Search Menu is Loading...\n\n")
        time.sleep(2)
        film = input("Movie to be searched: ").title()

        #Search will be done within the Top 250 Movies list
        url = requests.get("https://imdb-api.com/en/API/Top250Movies/k_rs97zh2v")
        link = url.json()

        #I create an empty list called #ID and since each movie in the API link has an id, I add those ids one by one to the list I created.
        ID = list()
        for i in link["items"]:
            ID.append(i["id"])
        
        #I do the same thing for 'TITLE' as i did for 'ID'
        TITLE = list()
        for i in link["items"]:
            TITLE.append(i["title"])

        #I combined #TITLE and ID (key = TITLE , value = ID) then converted the list to dictionary with dict method.
        join = zip(TITLE,ID)
        data = dict(join)

        key = data.get(film)

        #I define a variable inside the url as each movie has an id.
        url2 = requests.get("https://imdb-api.com/en/API/Wikipedia/k_rs97zh2v/{}".format(key))
        link2 = url2.json()
        print(textwrap.fill(link2["plotShort"]["plainText"]))
        self.returnToMenu()

    def quit(self):
        print("Exiting the Platform...")
        time.sleep(2)
        self.loop = False
        exit()

    def returnToMenu(self):
        while True:
            x = input("\n\nPress '7' to return to menu, Press '6' to exit the program: ")
            if x == "7":
                print("Menu is Loading...")
                time.sleep(2)
                self.program()
                break
            elif x == "6":
                self.quit()
                break
            else:
                print("Please make a valid choice!")


System = Film()
while System.loop:
    System.program()

