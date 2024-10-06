let i;
let run = true;
i=0;
for(; run;){
    console.log(`for loop - ${i}`);
    i++;
    if(i>5){
        run = false;
    }
}
i = 0
run = true;
while(run){
    console.log(`while loop - ${i}`);
    i++;
    if(i>5){
        run = false;
    }    
}