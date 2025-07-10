function infnity_recursion(i){
    console.log(i);
    infnity_recursion(i - 1);
}

//console.log(infnity_recursion(100));

// function to example base_case and recusion_case
function recursion_cases(i){
    if (i === 0){
        console.log("Recursion Finished!")
    } else {
        console.log(i);
        recursion_cases(i - 1);
    }
    return 0;
}

console.log(recursion_cases(100));