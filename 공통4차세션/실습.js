// 공통된 속성 - 배열, 다양한 속성 - 객체
const jiwon = {
    name: 'Jiwon Jeong',
    age: 24,
    bloodType: 'B'
}

//객체에서 const는 수정 불가, let은 수정 가능

//alert, confirm은 웹 브라우저에서만 작동하는 함수
//alert - 알림창 & 확인
//confirm - 알림창 + 취소, 확인 -> true/false
console.log("츌력");
alert("경고 메세지");
const isConfirmed = confirm("괜찮나요!~");

//조건문, 반복문
let age = 24;

if(age>19){
    alert("어른입니다.");
} else if(age <= 19 && age > 10) {
    alert("청소년입니다.");
} else {
    alert('애기네요!');
}

//
let Age = 1;
for (let i=1; i<6; i++) {
    Age = Age + 1 // age += 1
    console.log(`${i}년 후 나이는 ${Age}입니다.`);
}

