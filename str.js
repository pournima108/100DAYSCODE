var str = "acba";

function isPalindrome(str) {
  // split the string to array, reverse the array, then join the array with ''

  
  return str === str.split('').reverse().join(''); 
  

}

result=isPalindrome(str); // return true
console.log(result)