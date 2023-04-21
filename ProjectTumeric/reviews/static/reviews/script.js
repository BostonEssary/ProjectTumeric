var text = document.getElementById('text-body').textContent;
text = text.trim();
text = text.replace(/(\r\n|\n|\r)/gm, "");
var words = text.split(" ");
words = words.filter(item => item);



var section1Text = "";



for (let i = 0; i < words.length/3; i++) {
    if (i == 0) {
        section1Text = section1Text.concat(words[i]);
        console.log("if statement")
    }
    else{
        console.log("else statement")
        section1Text = section1Text.concat(' ', words[i]);
    }
}


document.getElementById('section-1').textContent = section1Text;
console.log(section1Text);
document.getElementsByTagName('p').textContent = " ";
document.getElementById('master-text').textContent = " ";