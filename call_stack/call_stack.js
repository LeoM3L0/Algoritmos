function saudation(name){
    console.log(`Hello ${name}`);
    console.log('Welcome to the call stack example');
    saudation2(name);
    console.log('Goodbye from saudation');
    goodbye();
    return "SEE YOU SPACE COWBOY!!";
}

function saudation2(name){
    console.log(`Hello ${name} from saudation2`);
}

function goodbye(){
    return 'Call Stack Finished';
}

console.log('Starting the call stack example');
console.log(saudation('John Doe'));