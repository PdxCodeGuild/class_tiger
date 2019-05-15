/*

HackerTyper Lab:

Use Textarea to add characters

event.preventDefault() to stop the original character from being typed

kilo win suitably small values blob concurrently python fatal tunnel in Donald Knuth. Terminal script kiddies hexadecimal char continue unix bytes alloc bar spoof firewall ctl-c float mega cat Linus Torvalds machine code. Leslie Lamport hello world rm -rf protocol big-endian new private hack the mainframe boolean tcp recursively echo


*/

// import {codeContent} from "./codeContentFile.js";

let textArea = document.getElementById('text-area');
textArea.focus();
var num = 0;
function hackFunc(){
  event.preventDefault();
  let textAreaHeight = textArea.scrollHeight;

  textArea.value += codeContent.slice(num,num+10);

  num += 10;
  if (num >= codeContent.length){
    num = 0;
  }

  if (textAreaHeight > (window.innerHeight - 50)){

    console.log('need to scroll');
    textArea.scrollTo(0, (textAreaHeight));

  }
}

textArea.addEventListener('keydown',hackFunc);
