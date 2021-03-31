let form_image = document.querySelectorAll(".form_image");

//slider logic--------------------------------------------------------------------------

//height slider---------------------------------------------------

let height_slider = document.getElementById("height_slider");
let height_text = document.getElementById("height_text");
let height_image = document.getElementById("height_image");

// Display the default slider value
height_text.innerHTML = "5'9\"";

function height() {
  //Display height in ft and inches
  let slider_value = parseInt(height_slider.value);
  let ft_value = 0;
  let inch_value = 0;
  //logic to display as ft and inch
  if (slider_value < 12) {
    ft_value = 5;
    inch_value = slider_value;
  } else {
    ft_value = 6;
    inch_value = slider_value - 12;
  }
  //concatenate values
  let height_inch = ft_value + "'" + inch_value + '"';

  //add edge cases and display height
  if (slider_value === 0) {
    height_text.innerHTML = height_inch + " and below";
  } else if (slider_value === 18) {
    height_text.innerHTML = height_inch + " and above";
  } else {
    height_text.innerHTML = height_inch;
  }

  //change image height depending on slider
  height_image.style.height = parseInt(height_slider.value) + 82 + "%";
  //grab the new height and make the width equal
  let height = height_image.offsetHeight.toString() + "px";
  height_image.style.width = height;
}

// change image and image size when slider changed
height_slider.addEventListener("input", height);

// change image and image size when page loads
height();


//discipline slider----------------------------------------------
let disc_slider = document.getElementById("disc_slider");
let disc_image1 = document.getElementById("disc_image1");
let disc_image2 = document.getElementById("disc_image2");
let disc_image3 = document.getElementById("disc_image3");

//hide and show images while setting width and height equal to height of parent element

function discipline() {
  let slider_value = parseInt(disc_slider.value);

  if (slider_value < 6) {
    disc_image1.style.display = "none";
    disc_image1.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image1.style.width = form_image[1].offsetHeight.toString() + "px";

    disc_image2.style.display = "none";
    disc_image2.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image2.style.width = form_image[1].offsetHeight.toString() + "px";

    disc_image3.style.display = "block";
    disc_image3.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image3.style.width = form_image[1].offsetHeight.toString() + "px";
  } else if (slider_value < 13) {
    disc_image1.style.display = "none";
    disc_image1.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image1.style.width = form_image[1].offsetHeight.toString() + "px";

    disc_image2.style.display = "block";
    disc_image2.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image2.style.width = form_image[1].offsetHeight.toString() + "px";

    disc_image3.style.display = "none";
    disc_image3.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image3.style.width = form_image[1].offsetHeight.toString() + "px";
  } else {
    disc_image1.style.display = "block";
    disc_image1.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image1.style.width = form_image[1].offsetHeight.toString() + "px";

    disc_image2.style.display = "none";
    disc_image2.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image2.style.width = form_image[1].offsetHeight.toString() + "px";

    disc_image3.style.display = "none";
    disc_image3.style.height = form_image[1].offsetHeight.toString() + "px";
    disc_image3.style.width = form_image[1].offsetHeight.toString() + "px";
  }
};

disc_slider.addEventListener("input", discipline);

discipline();


//price slider---------------------------------------------------
let price_slider = document.getElementById("price_slider");
let price_text = document.getElementById("price_text");
let price_image = document.getElementById("price_image");

// Display the default price value
price_text.innerHTML = "Less than £350";


//change price html and image size on slider input (function now)

function price() {
  let slider_value = parseInt(price_slider.value);
  let price = "";

  //show price message depending on slider value

  switch (slider_value) {
    case 0:
      price = "Up to £150";
      break;
    case 1:
      price = "Up to £200";
      break;
    case 2:
      price = "Up to £250";
      break;
    case 3:
      price = "Up to £300";
      break;
    case 4:
      price = "Up to £350";
      break;
    case 5:
      price = "Up to £400";
      break;
    case 6:
      price = "Up to £450";
      break;
    case 7:
      price = "Up to £500";
      break;
    case 8:
      price = "More than £500";
  }

  price_text.innerHTML = price;

  //change price image height depending on slider
  price_image.style.height = slider_value * 3 + 76 + "%";
  //grab the new price image height and make the width equal
  let height = price_image.offsetHeight.toString() + "px";
  price_image.style.width = height;
}

//call the function when slider is changed

price_slider.addEventListener("input", price);

//call the function when the page is loaded

price();


//stat indicator-------------------------------------------

//set indicator height to equal width

let indicator = document.querySelectorAll(".stat_indicator");

for (var i = 0; i < indicator.length; i++) {
  height = indicator[i].offsetHeight.toString() + "px";
  indicator[i].style.width = height;
}

//resize image 1:1 aspect ratio----------------------------


//When page initially loaded

for (var i = 0; i < 3; i++) {
  height = form_image[i].offsetHeight.toString() + "px";
  form_image[i].style.width = height;
}

//when window resized
function resize() {
  for (var i = 0; i < form_image.length; i++) {
    height = form_image[i].offsetHeight.toString() + "px";
    form_image[i].style.width = height;
  }
  //fix for this image not resizing after the slider is used
  disc_image1.style.width = "100%";
  disc_image1.style.height = "100%";
  disc_image2.style.width = "100%";
  disc_image2.style.height = "100%";
  disc_image3.style.width = "100%";
  disc_image3.style.height = "100%";

  //resize frame stat indicator

  for (var i = 0; i < indicator.length; i++) {
    height = indicator[i].offsetHeight.toString() + "px";
    indicator[i].style.width = height;
  }
}

window.addEventListener("resize", resize);
