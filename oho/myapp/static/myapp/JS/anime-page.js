fetch("/static/myapp/Data/action-packed-adventure.json")
  .then(response => response.json())
  .then(data => {
    const animer = data.find(a => a.id === animeId);
    const ratingpoint = animer.rating/2;

    document.querySelectorAll('.star-rating').forEach(container => {
      const stars = container.querySelectorAll('.star');

      const fullStars = Math.floor(ratingpoint);
      const hasHalf = ratingpoint - fullStars >= 0.5;

      stars.forEach((star, index) => {
        if (index < fullStars) {
          star.classList.add('filled');
        } else if (index === fullStars && hasHalf) {
          star.innerHTML = '&#9733;'; // full star symbol; could use a half-star style if needed
          star.classList.add('filled'); // replace with 'half-filled' if using half icons
        }
      });
    });
  });


// {{{{GRID FUNCTION}}}}
// ==================================================================================================================================
// Random suggestion
// ==================================================================================================================================

function getRandomInt(max) {
  return Math.floor(Math.random() * max) + 1;
}

//function to display content.
function displayrandom() {
  const totalitem = 50; //Total number of items
  const itemdisplay = 25; //Total number of items to display
  const tempitems = new Set(); //set that will contain only uniq item num.

  //for randomly selecting 9 items.
  while (tempitems.size < itemdisplay) {
    const randomnum = getRandomInt(totalitem);
    tempitems.add(randomnum);
  }

  // Loop through all the grid items and hide or show based on selected random item
  const grid_items = document.querySelectorAll(".ani-con-ARP");
  grid_items.forEach((item, index) => {
    if (tempitems.has(index + 1)) {
      item.classList.add("show"); //shows the element
    } else {
      item.classList.remove("show"); // Hide the item
    }
  });
}

//when page reload the random grid function will be called
window.onload = displayrandom;












// data retriver
const params = new URLSearchParams(window.location.search);
const animeId = params.get("id");
console.log(animeId)

fetch("/static/myapp/Data/action-packed-adventure.json")
  .then(response => response.json())
  .then(data => {
    console.log(data)
    const anime = data.find(a => a.id === animeId);
    console.log(anime);  // ADD THIS LINE
    console.log(anime.images);
    if (anime) {
      document.getElementById("Anititle").textContent = anime.title;
      for (i=0;i<5;i++) {
        document.getElementById(`ap${i+1}`).src = 'static/' + anime.images[i] ;
        console.log(document.getElementById(`ap${i+1}`).src)
      }
      // document.getElementById("anime-image").src = anime.image;
      // document.getElementById("anime-image").alt = anime.title;
      // document.getElementById("anime-rating").textContent = anime.rating;
      // document.getElementById("description").textContent = anime.description;
      document.getElementById("description").innerHTML = anime.description;
    } else {
      document.querySelector("#anititle").textContent = "<p>Anime not found.</p>";
    }
  });
