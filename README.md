# Letterboxd-Collect-Movie-Images
## Creating collage of all movie posters from your movies list

This program is for those **#ExtremeMovieAddicts**/**#Cinephilias** who like to keep a record of **all_movies_ever_watched** / **watchlist**

https://letterboxd.com/ site helps you add all movies to your list.
Seperate lists can also be created for Bollywood / Hollywood / ...etc

What this program does ?
- In short.. It goes to the site and downloads all images(in **H**igh**Q**uality) from your chosen list, and finally makes a collage out of all those images.

Program features :
- Automatically opens the site in your default browser
- Enters your credentials
- Lets you decide the range of movie images to download / generate collage
- Lets you decide number of movies to fit in a row of the collage (Dimensions calculated accordingly)
- Lets you decide the margin width to set between images
- Lets you decide the color of the background (Default : DarkBlue)
- Then the collage gets ready (depending on your internet connection)

Things used :
- IDE (for python3)

Project Dependencies
- Python modules
  - selenium  - used to automate web browser interaction
  - PIL       - image library for Python
  - BytesIO   - manipulate bytes data in memory (img)
  - urllib    - for working with URLs
- Chrome webdriver - for setting up your browser to be automated by selenium

## Screenshots of demo
My collection of all **Hollywood Movies** ever watched (sorted by name)
![Animated Movies](https://user-images.githubusercontent.com/67866166/147610642-d54e9e27-d120-47ef-adc0-b6d1e943c227.jpg)

My collection of all **Romantic Movies** ever watched (sorted by rating)
![Romantic Movies](https://user-images.githubusercontent.com/67866166/147611499-883b4443-c254-4862-90e6-5bbc05dc2eb0.jpg)
