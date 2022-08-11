let fill_color = 0;
let color_change = 1;
let radius = 50;

function setup() {
  createCanvas(400, 400);
  background(0);
}

function draw() {
  circle(mouseX, mouseY, radius);
  noStroke()
  
  fill_color += color_change;
  if (fill_color > 255 || fill_color < 0) {
    color_change = -color_change;
  }
  
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(fill_color,10);
  } 
}