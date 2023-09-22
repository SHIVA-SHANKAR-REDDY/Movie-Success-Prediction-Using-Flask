# pip3 install nltk scikit-learn==1.0.2 mlxtend numpy pandas joblib

from flask import Flask,render_template,request,json,jsonify
from movie_success_predictor import predictor


app=Flask(__name__)
app.secret_key="secure"
data =0


directors = ['James Gunn', 'Ridley Scott', 'M. Night Shyamalan',
       'Christophe Lourdelet', 'David Ayer', 'Yimou Zhang',
       'Damien Chazelle', 'James Gray', 'Morten Tyldum', 'David Yates',
       'Theodore Melfi', 'Gareth Edwards', 'Ron Clements',
       'Nacho Vigalondo', 'Chris Renaud', 'Mel Gibson', 'Paul Greengrass',
       'Garth Davis', 'Denis Villeneuve', 'Stephen Gaghan',
       'Kenneth Lonergan', 'Walt Dohrn', 'Roland Emmerich', 'Jon Lucas',
       'Justin Kurzel', 'John Hamburg', 'Tom Ford', 'Bryan Singer',
       'Tim Miller', 'Paul W.S. Anderson', 'Anthony Russo',
       'Christopher Nolan', 'Scott Derrickson', 'Antoine Fuqua',
       'Greg Tiernan', 'Barry Jenkins', 'John Lee Hancock',
       'Ricardo de Montreuil', 'Rob Marshall', 'John Madden',
       'Justin Lin', 'J.J. Abrams', 'Anna Foerster', 'Garry Marshall',
       'Chad Stahelski', 'Martin Scorsese', 'Fede Alvarez',
       'Thea Sharrock', 'Lone Scherfig', 'Clint Eastwood', 'Zack Snyder',
       'Tate Taylor', 'Sam Taylor-Johnson', 'Matthew Vaughn',
       'Peter Berg', 'George Miller', 'Robin Swicord', 'Robert Zemeckis',
       'J.A. Bayona', 'David Frankel', 'Byron Howard', 'Gore Verbinski',
       'Joss Whedon', 'Quentin Tarantino', 'Paul Feig', 'Matt Ross',
       'David Fincher', 'James Wan', 'Colin Trevorrow', 'Ben Affleck',
       'James Cameron', "Gavin O'Connor", 'Duncan Jones', 'Todd Phillips',
       'Shane Black', 'Makoto Shinkai', 'Jeremy Gillespie',
       'Olivier Assayas', 'Brian Helgeland', 'Kenneth Branagh',
       'Guy Ritchie', 'David Mackenzie', 'Taylor Hackford',
       'Alex Garland', 'Greg McLean', 'Steve McQueen', 'Josh Gordon',
       'Nicolas Winding Refn', 'Dan Trachtenberg', 'Andrew Stanton',
       'Tim Burton', 'Neil Burger', 'Jake Szymanski', 'Jon Favreau',
       'Michael Bay', 'Henry Joost', 'Phyllida Lloyd',
       'Alejandro González Iñárritu', 'Denzel Washington',
       'Jaume Collet-Serra', 'Derek Cianfrance', 'Ethan Coen',
       'Baz Luhrmann', 'Thor Freudenthal', 'Adam McKay',
       'Lenny Abrahamson', 'Chan-wook Park', 'Kelly Fremon Craig',
       'Greg Mottola', 'Ron Howard', 'Steven Spielberg', 'Gary Ross',
       'Elizabeth Wood', 'Colin Strause', 'Guillermo del Toro',
       'Glenn Ficarra', 'Edgar Wright', 'Ben Wheatley', 'Edward Zwick',
       'Martin Campbell', 'Catherine Hardwicke', 'Jon M. Chu',
       'Simon Curtis', 'Sam Mendes', 'Dan Gilroy', 'Travis Knight',
       'Spike Jonze', 'Chris Buck', 'Brad Bird', 'Matt Reeves',
       'Ben Stiller', 'Peyton Reed', 'Sharon Maguire', 'Robert Eggers',
       'Asghar Farhadi', 'Ang Lee', 'Judd Apatow', 'Tom McCarthy',
       'Luke Scott', 'Joe Johnston', 'Sean Penn',
       'Rawson Marshall Thurber', 'Doug Liman', 'Oliver Stone',
       'Robert Schwentke', 'Julia Ducournau', 'Jim Jarmusch',
       'Brad Peyton', 'Harmony Korine', 'Alan Taylor', 'Alex Proyas',
       'Chris Wedge', 'Ilya Naishuller', 'John Lasseter',
       'David Robert Mitchell', 'Andrea Arnold', 'Yorgos Lanthimos',
       'Nimród Antal', 'Robert Stromberg', 'Andy Goddard',
       'Christopher McQuarrie', 'Cedric Nicolas-Troyan',
       'Stephen Chbosky', 'Pablo Larraín', 'D.J. Caruso', 'Wes Anderson',
       'Andrew Niccol', 'Pete Docter', 'Ash Brannon', 'Chris Columbus',
       'Tom Hooper', 'Alfonso Cuarón', 'Mike Mills', 'Olivier Nakache',
       'Eleanor Coppola', 'F. Gary Gray', 'Marc Webb', 'Rupert Wyatt',
       'David F. Sandberg', 'Joseph Cedar', 'Darren Aronofsky',
       'Justin Simien', 'Lars von Trier', 'Dave Green', 'Eli Roth',
       'Dan Mazer', 'Tom Tykwer', 'Gavin Hood', 'Peter Jackson',
       'Phil Lord', 'John Carney', 'Joseph Kosinski', 'Richard Linklater',
       'Louis Leterrier', 'Brett Ratner', 'Lana Wachowski', 'Jared Hess',
       'Sang-ho Yeon', 'Jason Moore', 'Nicholas Stoller', 'Ross Katz',
       'Mike Thurmeier', 'Brad Furman', 'Paul Thomas Anderson',
       'Drew Goddard', 'Fred Wolf', 'Jim Field Smith', 'James Bobin',
       'Christian Ditter', 'Abdellatif Kechiche', 'Jennifer Kent',
       'Bong Joon Ho', 'J Blakeson', 'Anne Fletcher', 'So Yong Kim',
       'Breck Eisner', 'Paul McGuigan', 'Roger Spottiswoode',
       'Jeremy Saulnier', 'Michael Mann', 'Jean-Marc Vallée',
       'David O. Russell', 'Josh Boone', 'Frank Coraci', 'Rian Johnson',
       'David Lowery', 'Sam Raimi', 'Karyn Kusama', 'Woody Allen',
       'Jocelyn Moorhouse', 'Sergei Bodrov', 'James Marsh',
       'Evan Goldberg', 'Richard Curtis', 'Jon Watts', 'Ruben Fleischer',
       'Danny Boyle', 'Bill Condon', 'Timur Bekmambetov', 'J.D. Dillard',
       'Wes Ball', 'Ariel Vromen', 'Stephen Frears', 'Eran Creevy',
       'Scott Cooper', 'Ryan Coogler', 'Dan Kwan', 'Patrick Hughes',
       'Jemaine Clement', 'Baltasar Kormákur', 'James Mangold',
       'Peter Atencio', 'Pierre Morel', 'Dennis Dugan',
       'Lee Toland Krieger', 'Peter Billingsley', 'Steven Soderbergh',
       'Kyle Balda', 'Pierre Coffin', 'Michael Hoffman',
       'Kathryn Bigelow', 'Nathan Greno', 'Francis Lawrence',
       'John Francis Daley', 'Elizabeth Banks', 'Dan Scanlon',
       'Dennis Gansel', 'Kevin Smith', 'Joe Wright', 'David Ross',
       'Burr Steers', 'Noam Murro', 'Babak Najafi', 'Frank Miller',
       'Rajkumar Hirani', 'Marc Forster', 'George Tillman Jr.',
       'Jeff Wadlow', 'John Crowley', 'Henry Selick', 'Pete Travis',
       'Taika Waititi', 'Don Hall', 'Kimberly Peirce', 'Christian Alvart',
       'Thomas Vinterberg', 'Etan Cohen', 'William Brent Bell',
       'Mick Jackson', 'Rob Letterman', 'Phillip Noyce', 'Neill Blomkamp',
       'Sofia Coppola', 'Dexter Fletcher',
       'Florian Henckel von Donnersmarck', 'John Hillcoat',
       'Adam Shankman', 'Lasse Hallström', 'Jim Mickle', 'Albert Hughes',
       'Ericson Core', 'Jonathan Glazer', 'Barry Sonnenfeld',
       'Todd Haynes', 'Paolo Sorrentino', 'Mark Herman',
       'S. Craig Zahler', 'Will Gluck', 'Biyi Bandele', 'Sean Ellis',
       'Andrey Kravchuk', 'David Schwimmer', 'George Nolfi',
       'Tony Gilroy', 'Simon Verhoeven', 'Luc Besson', 'Terence Davies',
       'Scott Waugh', 'Steven Brill', 'Roman Polanski', 'Jeff Nichols',
       'Mike Birbiglia', 'Philippe Falardeau', 'Josh Trank', 'Rob Cohen',
       'Joel Edgerton', 'Gary Shore', 'Mike Judge', 'Sylvester Stallone',
       'Rich Moore', 'Rupert Sanders', 'Jason Reitman', 'Jodie Foster',
       'Nick Cassavetes', 'Kevin Lima', 'Nancy Meyers', 'Jonathan Dayton',
       'Ben Younger', 'Craig Gillespie', 'Andrew Jarecki',
       'John Stockwell', 'Jake Kasdan', 'Kirk Jones', 'Bennett Miller',
       'Mark Steven Johnson', 'Angelina Jolie', 'Tarsem Singh',
       'Mark Andrews', 'Niels Arden Oplev', 'Anne Fontaine',
       'Michaël R. Roskam', 'Andy Fickman', 'Sean Anders', 'Tom McGrath',
       'Jean-François Richet', 'Alessandro Carloni', 'Zackary Adler',
       'Seth Gordon', 'Xavier Dolan', 'Richard LaGravenese', 'Maren Ade',
       'Andrew Dominik', 'Joseph Gordon-Levitt', 'James Watkins',
       'Joey Curtis', 'Paco Cabezas', 'Rick Famuyiwa', 'Måns Mårlind',
       'Marcus Nispel', 'Olivier Megaton', 'Len Wiseman', 'Shawn Levy',
       'Levan Gabriadze', 'Jon Hurwitz', 'Gabriele Muccino',
       'Damián Szifron', 'François Ozon', 'John Wells', 'Mark Waters',
       'Akiva Schaffer', 'Jonathan Liebesman', 'David Cronenberg',
       'Simon Stone', 'David Gordon Green', 'Jon Kasdan',
       'Mia Hansen-Løve', 'Alejandro Amenábar', 'Seth MacFarlane',
       'Daniel Espinosa', 'Frank Darabont', 'Mikael Håfström',
       'Ari Sandel', 'Jee-woon Kim', 'Lynne Ramsay', 'Whit Stillman',
       'Harald Zwart', 'Lee Unkrich', 'Tomas Alfredson', 'Gauri Shinde',
       'Mike Cahill', 'John Krasinski', 'David Dobkin',
       'Michael Dudok de Wit', 'Jorge R. Gutiérrez', 'Bobby Farrelly',
       'Doug Ellin', 'Bryan Bertino', 'Adam Wingard', 'Joe Carnahan',
       'Bruce Beresford', 'Oz Perkins', 'Terrence Malick', 'Ben Falcone',
       'Jonathan Jakubowicz', 'Juan José Campanella', 'Max Joseph',
       'Mike Flanagan', 'Gregory Hoblit', 'Martin McDonagh', 'McG',
       'Kirsten Sheridan', 'James DeMonaco', 'Jake Schreier',
       'Dean DeBlois', 'Rob Zombie', 'Bruce A. Evans', 'Chris Evans',
       'Stewart Hendler', 'Genndy Tartakovsky', 'Claude Barras',
       'Asger Leth', 'Ivan Reitman', 'Werner Herzog', 'Scott Frank',
       'Mike Newell', 'James Ponsoldt', 'Amma Asante', 'François Simard',
       'Andrés Muschietti', 'Spike Lee', 'John R. Leonetti',
       'Terry Gilliam', 'Stephen Sommers', 'Antonio Campos',
       'Jason Friedberg', 'David Bowers', 'Cary Joji Fukunaga',
       'Andy Tennant', 'Larry Charles', 'Erik Van Looy',
       'Cristian Mungiu', 'Luca Guadagnino', 'Tony Scott', 'Tim Johnson',
       'Giuseppe Tornatore', 'Robert Luketic', 'Mark Osborne',
       'Malcolm D. Lee', 'Alexandre Aja', 'Allen Coulter',
       'Miguel Arteta', 'Steven Knight', 'James Schamus',
       'Kyle Patrick Alvarez', 'Hannes Holm', 'James Wong', 'Dan Bradley',
       'Greg Berlanti', 'Juan Carlos Fresnadillo', 'Jonathan Levine',
       'Hideaki Anno', 'Wally Pfister', 'Carlos Saldanha',
       'Drake Doremus', 'Scott Hicks', 'Michael Patrick King',
       'Gary Winick', 'Leslye Headland', 'David R. Ellis',
       'Michael Dowse', 'José Padilha', 'Michael Showalter',
       'Matteo Garrone', 'Gabor Csupo', 'James Ward Byrkit',
       'Hong-jin Na', 'Simon West', 'Chris Weitz', 'Neil Marshall',
       'Christopher Landon', 'John Erick Dowdle', 'Lee Daniels',
       'Gus Van Sant', 'Craig Brewer', 'R.J. Cutler', 'Anna Biller',
       'Tom Six', 'Ryûhei Kitamura', 'David Slade', 'Mark Mylod',
       'David Twohy', 'Justin Kelly', 'Justin Tipping',
       'Alfonso Gomez-Rejon', 'Alexander Payne', 'Jordan Vogt-Roberts',
       'Tom Gormican', 'Scott Stewart', 'Patricia Rozema',
       'Justin Chadwick', 'Steven R. Monroe', 'John Luessenhop',
       'Wes Craven', 'Mira Nair', 'Pedro Almodóvar', 'Patricia Riggen',
       'Julie Taymor', 'Luke Greenfield', 'Boaz Yakin', 'Steven Quale',
       'Shana Feste', 'Patrick Tatopoulos', 'Aamir Khan',
       'Nima Nourizadeh']

genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
       'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical',
       'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']

print(len(genres))

@app.route('/',methods=["post","get"])
def first_page():
    if request.method=="POST":
        global data
        data=json.loads(request.data)
        print('Form Dataaaa:', data)
        return jsonify(dict(msg="success"))
    else:
        return render_template("form_page.html" , directors = sorted(directors), genres = sorted(genres))
    


@app.route("/data_page/",methods=["post", "get"])
def data_page():
    if request.method=="POST":
        director = request.form['director']
        genre_list = []
        for i in range(len(genres)):
            try:
                genre_list.append(request.form['genre'+str(i+1)])
            except:
                pass
        year = request.form['year']
        runtime = request.form['runtime']
        metascore = request.form['metascore']
        description = request.form['description']

        print('Form Dataxxxxx:', genre_list)
        res = predictor(director,genre_list,int(year), int(runtime), float(metascore) , description)
        print("ML", res)
        return render_template("data_page.html",message= [director,genre_list,int(year), int(runtime), float(metascore) , description], result = res)
    else:
        return "GOT GET"
    
app.run(debug=True)
