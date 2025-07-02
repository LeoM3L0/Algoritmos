// Function to find index with minor element in array
function find_minor(array) {
    let minor = array[0]; // set minor value as first element of array
    let minor_index = 0; // set index of the minor element

    for (let i = 1; i < array.length; i++){
        if (array[i] < minor) {
            minor = array[i];
            minor_index = i;
        }
    }
    return minor_index; // return index of minor value
}

function selection_sort(array){
    let sorted_array = []; // New array for save sorted values

    while (array.length > 0) { // while array is not empty
        let minor_index = find_minor(array); // find index of minor element
        let minor_value = array.splice(minor_index, 1)[0]; // remove minor value and return then
        sorted_array.push(minor_value); // add minor element to sorted array
    }
    return sorted_array; // return sorted_array
}

let array = [7, 3, 5, 2, 9];
console.log(selection_sort(array));