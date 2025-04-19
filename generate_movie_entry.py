#write the start of the html
# to open/create a new html file in the write mode 
  # w overwrites file, a adds to existing contents
f = open('movies.html', 'w') 
  
  # the html code which will go in the file GFG.html 
html_template = """
  <!DOCTYPE html>
    <head>
    <meta charset="UTF-8"> 
    
    <Title>&#127916; Movie Collection</Title>

        <!--Bootstrap Links-->
            <!-- Latest compiled and minified CSS -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
            <!-- Optional theme -->
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
            <!-- Latest compiled and minified JavaScript -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

            
          <!--I THINK these are for the drop-down buttons-->
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.min.js" integrity="sha384-VQqxDN0EQCkWoxt/0vsQvZswzTHUVOImccYmSyhJTp7kGtPed0Qcx8rK9h9YEgx+" crossorigin="anonymous"></script>

            <!-- jQuery (required for Bootstrap's JavaScript plugins) -->
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

            <!-- Popper.js (required for Bootstrap dropdowns) -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.6/umd/popper.min.js"></script>
            
            
<style>
  body {
    background-color: #282828;
  }

  h1, h2, h3, h4, h5, b, p  {
    color: white;
  }

  button {
    background-color: gray;
    color: white;
    width: 100%;
  }
</style>
        
    </head>
    <body>
  <h1><b>Movie Collection</b></h1>
  <br>
            


  """
  
  # writing the code into the file 
f.write(html_template) 
  
  # close the file 
f.close() 


#read spreadsheet
  #pip install xlrd
  #pip install pandas
  #pip install openpyxl
  #https://pythonbasics.org/read-excel/
import pandas as pd

#load spreadsheet into a data frame
df = pd.read_excel('movie_list.xlsx')

#current row
current_row = 0
movie_select = df.loc[(current_row)]

#loop starts
while (movie_select)[0] != "zoolander":
  print(current_row)

  #movie (row) selection
  movie_select = df.loc[(current_row)]
  print(movie_select)

  #establish loop

  # Set variables
  movie_tag = (movie_select)[0] 
  movie_title = (movie_select)[1]
  movie_type = (movie_select)[2]
  movie_franchise = (movie_select)[3]
  movie_franchise_entry = str((movie_select)[4])
  movie_year = str((movie_select)[5])
  movie_rating = (movie_select)[6]
  movie_length = (movie_select)[7]
  movie_formats = (movie_select)[8]
  movie_genres = (movie_select)[9]
  movie_director = (movie_select)[10]
  movie_starring = (movie_select)[11]
  movie_description = (movie_select)[12]
  movie_poster = (movie_select)[22]
  movie_trailer_link = (movie_select)[13]
  movie_trailer_embed = (movie_select)[14]
  movie_imdb_score = (movie_select)[15]
  movie_imdb_link = (movie_select)[16]
  movie_rt_score = (movie_select)[17]
  movie_rt_link = (movie_select)[18]
  movie_review_link = (movie_select)[19]
  movie_reviewer = (movie_select)[20]
  movie_review_text = (movie_select)[21]

  print(movie_title+""" - Movie Entry""")
  #write html file
  # to open/create a new html file in the write mode 
  f = open('movies.html', 'a') 
  
  # the html code which will go in the file GFG.html 
  html_template = """

  
  <!-- """+(movie_title)+"""-->
  <div class="col-xs-12 col-sm-12 col-md-4 col-lg-3">  <!--Movie Entry-->
  <br>
  <div class="row"> <!--Top Section-->
        <div class="col-xs-8 col-sm-8 col-md-6 col-lg-6"> <!--Top Left-->
            <b>"""+(movie_franchise)+""" """+(movie_franchise_entry)+"""</b>  <!--Franchise Name and Installment Number-->
            <h2>"""+(movie_title)+"""</h2> <!--Movie Title-->
            <h4>"""+(movie_year)+""" | """+(movie_length)+""" | """+(movie_rating)+"""</h4> <!--Media type, run time, format-->
            <h5>"""+(movie_genres)+"""</h5> <!--Genres-->
            <b>"""+(movie_formats)+""" | """+(movie_director)+"""</b><!--Rating, Year, Director-->
            <h5>"""+(movie_starring)+"""</h5> <!--Top Billed Cast-->
        </div>  <!-- end of text-->
        <div class="col-xs-4 col-sm-4 col-md-6 col-lg-6"> <!--Poster-->
            <img src="""+(movie_poster)+""" width="100%">
        </div>  <!-- end of poster-->
    </div>  <!-- end of top section-->
    
  <!-- Button -->
    <p class="d-inline-flex gap-1">
      <button class="btn" type="button" data-bs-toggle="collapse" data-bs-target="#"""+(movie_tag)+"""" aria-expanded="false" aria-controls="""+(movie_tag)+""">
        Trailer, Description, and Reviews &#9660
      </button>
    </p>
    <div class="collapse" id="""+(movie_tag)+""">
      <div class="card card-body">

      <!--Trailer-->
      <center><h3><b><a href="""+(movie_trailer_link)+""">YouTube Trailer</a></b></h3></center>
      
      <p>"""+(movie_description)+"""</p> <!--Movie Description-->  
      
        <!-- Reviews -->
        <h4>&#129000; <a href="""+(movie_imdb_link)+""">IMDB: """+(movie_imdb_score)+"""</a><br>&#127813;<a href="""+(movie_rt_link)+""">RT: """+(movie_rt_score)+"""</a></h4>
        <p> <b><a href="""+(movie_review_link)+""">"""+(movie_reviewer)+""": </a></b>"""+(movie_review_text)+"""</p> 

      </div>
    </div>           
  </div>
  </div>  <!-- end -->
  """
  
  # writing the code into the file 
  f.write(html_template) 
  
  # close the file 
  f.close() 

  #loop ends
  current_row += 1

#write the end of the html
# to open/create a new html file in the write mode 
  # w overwrites file, a adds to existing contents
f = open('movies.html', 'a') 
  
  # the html code which will go in the file GFG.html 
html_template = """
  
</body>
</html>      

  """
  
  # writing the code into the file 
f.write(html_template) 
  
  # close the file 
f.close() 