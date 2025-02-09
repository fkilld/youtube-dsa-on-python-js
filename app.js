// // # Positive or Negative number: C | C++ |  Java | Python
// function positive_negative(n) {
//     if (n>0) return  'positive number'
//     else return 'negative number'
// }
// console.log(positive_negative(12))
// # Even or Odd number: js | Python

// function evenOdd(n) {
//     if (n%2==0) return 'even'
//     else  return 'odd'
// }
// console.log(evenOdd(1234))
// console.log(evenOdd(12345))

//# Sum of First N Natural numbers:  js | Python

// function sumOfFirst(n) {
//     let i = 1 ,sum=0;
//     while (i<=n){
//         sum+=i
//         i++
//     }
//     return sum
// }
// console.log(sumOfFirst(10))

// # Greatest of two numbers: js | Python
// function greatest_of_two(a,b){
//     if (a>b){
//         return 'a is greater'
//     }else {

//         return 'a is greater'
//     }
// }
// console.log(greatest_of_two(10, 5))
// # Greatest of the Three numbers: js | Python
// function greatest_of_three(a,b,c){
//     if ( a>b && a>c  )    return 'a is greater'
//     else if ( b>a && b>c  )    return 'b is greater'
//     else return 'c is greater'

// }
// console.log(greatest_of_three(5,10,12))
// # Leap year or not: js | Python

// function is_leap_year(year) {
//     if ((year % 400==0) || (year % 4 == 0 && year % 100 != 0)) {
//          return ` ${year} is a leap year`
//     } else {
//         return ` ${year} is not  a leap year`
//     }
// }
// console.log(is_leap_year(2018))
//  Prime number: js | Python
// function prime_number(n) {
//   if (n <= 1) return false
//   let i = 2,
//     flag = true
//   while (i * i < n) {
//     if (n % i == 0) {
//       return false
//     }
//     i += 1
//   }
//   return flag
// }
// console.log(prime_number(15))

// # Prime number within a given range: js | Python
function prime_number(n) {
  let i = 2
  while (i <= n) {
    let flag = true
    let j = 2
    while (j * j <= i) {
      if (i % j == 0) {
        flag = false
        break
      }
      j += 1
    }
    if (flag) console.log(i, 'is a prime number')
    i += 1
  }
}

prime_number(15)
