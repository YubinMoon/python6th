// switch
var digit = parseInt(prompt("Enter a digit : "));
switch (digit) {
	case 0:
		document.write("zero");
		break;
	case 1:
		document.write("one");
		break;
	case 2:
		document.write("two");
		break;
	case 3:
		document.write("three");
		break;
	case 4:
		document.write("four");
		break;
	case 5:
		document.write("five");
		break;
	case 6:
		document.write("six");
		break;
	case 7:
		document.write("seven");
		break;
	case 8:
		document.write("eight");
		break;
	case 9:
		document.write("nine");
		break;
	default:
		document.write("not a digit");
		break;
}

// // 모음 찾기
// var letter = prompt("Enter a letter : ");
// letter = letter.toLowerCase();
// if (letter == "a" || letter == "e" || letter == "i" || letter == "o" || letter == "u") {
// 	console.log("voewl");
// } else {
// 	console.log("Consonant");
// }

// // 제어문
// var num1 = parseInt(prompt("첫번째 숫자 입력 : "));
// var num2 = parseInt(prompt("두번째 숫자 입력 : "));
// if (num1 > num2) {
// 	document.write("큰 수 num1 : " + num1);
// }
// if (num1 < num2) {
// 	document.write("큰 수 num2 : " + num2);
// }
// if (num1 == num2) {
// 	document.write("같은 수");
// }
// if (num > num2) {
// 	document.write("큰 수 num1 : " + num1);
// } else if (num1 < num2) {
// 	document.write("큰 수 num2 : " + num2);
// } else if (num1 == num2) {
// 	document.write("같은 수");
// }
// if (num > num2) {
// 	document.write("큰 수 num1 : " + num1);
// } else if (num1 < num2) {
// 	document.write("큰 수 num2 : " + num2);
// } else {
// 	document.write("같은 수");
// }
// // 비교문
// var num1 = 20;
// var num2 = 10;
// var num3 = "10";
// var num4 = 20;
// var num5 = 15;
// console.log("일반 크기 비교");
// console.log(num1 > num2, num1, ">", num2);
// console.log(num1 >= num2, num1, ">=", num2);
// console.log(num1 < num2, num1, "<", num2);
// console.log(num1 <= num2, num1, "<=", num2);
// console.log("같은지 여부 확인");
// console.log(num1 == num4, num1, "==", num4);
// console.log(num1 != num4, num1, "!=", num4);
// console.log("===");
// console.log(num1 === num3, num1, "===", num3);
// console.log(num2 === num3, num2, "===", num3);
// console.log(num2 == num3, num2, "==", num3);
// console.log(num1 > num2 && num1 < num5, num1, ">", num2, "&&", num1, "<", num5);
// console.log(num1 > num2 || num1 < num5, num1, ">", num2, "||", num1, "<", num5);

// // 온도 변환
// var cels = parseFloat(prompt("섭씨 입력 : "));
// var farn = cels * (9 / 5) + 32;
// document.write("화씨 : " + farn);

// // 소수
// var base = parseFloat(prompt("Enter 밑변 : "));
// var height = parseFloat(prompt("Enter 높이 : "));
// var area = base * height * 0.5;
// document.write("삼각형의 넓이 : " + area);

// // 연산자
// var num1 = parseFloat(prompt("Enter first number : "));
// var num2 = parseFloat(prompt("Enter second number : "));
// var lineBreak = "<br>";
// var result = num1 + num2;
// document.write("the sum is : " + result + lineBreak);
// result = num1 - num2;
// document.write("the sub is : " + result + lineBreak);
// result = num1 * num2;
// document.write("the multiplication is : " + result + lineBreak);
// result = num1 / num2;
// document.write("the division is : " + result + lineBreak);
// result = num1 % num2;
// document.write("the remainder is : " + result + lineBreak);

// // type 변환
// var num = "20";
// num = num.toString();
// console.log(typeof num);
// var number = 20;
// console.log(typeof number);
// number = number.toString();
// console.log(number, typeof number);
// var x = 2.56789;
// console.log(x.toFixed(2));
// console.log(x.toPrecision(2));
// console.log(Number(true));
// console.log(Number(false));
// console.log(Number("10"));
// console.log(Number("  10  "));
// console.log(Number("10.25"));

// // 문자열 함수
// var text = prompt("Enter your name");
// document.write("your name : " + text + "<br/>");
// var len = text.length;
// document.write("Number of characters : " + len + "<br/>");
// document.write(text.charAt(2) + "<br/>");
// document.write(text.toUpperCase() + "<br/>");
// document.write(text.toLowerCase() + "<br/>");
// var text1 = "hi ";
// var text2 = "bye";
// var text3 = text1.concat(text2);
// document.write(text3 + "<br/>");
// var text4 = "Hello";
// var result = text4.slice(0, 2);
// document.write(result + "<br/>");

// // 문자열 연결하기
// var lName = "홍";
// var fName = "길동";
// var fullName = lName + fName;
// console.log(fullName);
// console.log("Today is " + "a" + "beautiful day");
// console.log("My name is " + fullName);
// var num1 = 20;
// var num2 = 30;
// var sum = num1 + num2;
// console.log(num1 + num2);
// console.log("" + num1 + num2);
// console.log(num1 + " + " + num2 + " = " + sum);

// // variable
// var name = "이승훈";
// var age = 29;
// var cgpa = 3.92;
// var lineBreak = "<br>";
// document.write("이름: " + name + lineBreak);
// document.write("나이: " + age + lineBreak);
// document.write("학점: " + cgpa + lineBreak);

// // type
// console.log(123, typeof 123);
// console.log(123.5, typeof 123.5);
// console.log("123", typeof "123");
// console.log(true, typeof true);
// console.log(false, typeof false);

// // value
// var car;
// console.log(car, typeof car);
// var car = "";
// console.log(car, typeof car);
// var person = { firstname: "John", lastname: "Doe", age: 50, eyeColor: "blue" };
// console.log(typeof person, person);
// person = null;
// console.log(typeof person, person);

// // document write
// document.write("Hello World!");
// document.write("<h1>Welcom to JS Program!</h1>");
// document.write("<h2>Welcom to JS Program!</h2>");

// // console
// console.debug("Welcom to JS Program!");
// console.log("Welcom to JS Program!");
// console.warn("Welcom to JS Program!");
// console.error("Welcom to JS Program!");

// // alert
// alert("Welcom to JS Program!");
// var a = prompt("Enter your name");
// console.log(a)
