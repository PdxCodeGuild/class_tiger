let webpages = ['https://www.google.com/',  
                'https://runawaymaryk.wordpress.com/',
                'https://www.outdoorproject.com/',
                'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                'https://www.instagram.com/runawaymaryk/'
];


let submit = document.getElementById("btn");
submit.addEventListener("click", function(){
    setTimeout(function(){
        let pick = Math.floor(Math.random()*webpages.length);
        window.location.href=webpages[pick];
        }, 5000);       
    let count = 5;
    let timer = setInterval(function(){
        document.getElementById("countdown").innerHTML = count;
        count -= 1;
        if(count <= 0){
        clearInterval(downloadTimer);
        }
    }, 1000);
});

            


   
    
