import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes</title>
    <link rel="shortcut icon" href="data:image/jpeg;base64,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"/>
    
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
    
        body {
            background-color:#800000;
            padding-top: 70px;
        }



        
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -10px;
            right: -8px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 15px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            padding=10% 5%
            cursor: pointer;
        }
        
        #navig{
        display: flex;
      background-color: green;
      overflow-y: auto;
      position: float;
      left: 3;
      top: -5;
      
      line-height: 20px;
      text-align: left;
      width: 100%;
      z-index: 1000;
      box-sizing: border-box;
    }
             
        .scale-media {
            padding: 36.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 60%;
            left: 0;
            top: 0;
            background-color=black;
            
            <!--background-image:
            url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRco7B-oEndkbV8sz3t0n0DxzFTVvCNG_sAU11u6GkJ-QBOr_Ca8Q");
            background-repeat:repeat;-->
        }


       <!-- <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
          <div class="navbar navbar-default" role="navigation">
        <div class="navbar-header">
         <button type="button" class="navbar-toggle" data-toggle="collapse" ></button>
         

         <div class="navbar-collapse collapse"> 
          
            
            <a class="navbar-brand" href="#" padding=20px>Telugu</a>
            <a class="navbar-brand" href="#">Hindi</a>
            <a class="navbar-brand" href="#">English</ar>
            <a class="navbar-brand" href="#">Action</a>
            <a class="navbar-brand" href="#">Thrilling</a>
            <a class="navbar-brand" href="#">Entertainment</a>
            <a class="navbar-brand" href="#">Family movies</a>
            
            <input type="text" placeholder="Search for movies.."style="float:right">
            
            
          </div>
        </div>
      </div>
    </div> -->
   


        
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body >
  
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation"> -->
        <div class="container">

        <div class="navbar navbar-default" id="navig" role="navigation">
        <div class="navbar-header">
        <span class="navbar-brand"></span>
         <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">OPT</button>
         
        
          <div class="navbar-collapse collapse">
          <div class="navbar">
            <ul class=" nav navbar-nav">
            <li><a  href="#">Action</a></li>
            <li><a  href="#">Thrilling</a></li>
            <li><a  href="#">Entertainment</a></li>
            <li><a  href="#">Family movies</a></li>
           
           
            
            <ul class="nav navbar-nav navbar-right">
             <li><input type="text"  placeholder="Search..."  name="srch-term" ></input></li>
      <li><button type="button" style="padding: 4.6px 9px;"<a href="#"><span class="glyphicon glyphicon-search"></span> </a></button></li>
      </ul>
      </ul>
    
            
          </div>
        </div>
      </div>
    </div>
   <!-- <div class="container"> -->
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" >
    <h2>{movie_title}</h2>
    <div class="video-thumbnail">
  <img src="https://s3.postimg.org/vhd9in5ib/toyota_yaris_4.jpg" alt="Video thumbnail" />
</div>
    <p style="color:#800000;">{storyline}</p>
</div>
'''






def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
