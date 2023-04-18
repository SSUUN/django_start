
//w자바스크립트 주석
/*
문단줙
*/
function alertview(){
        alert("알림창");
    }

function gocss1(x){

    alert("알림창");
    location.href="/front/css_"+x;
}
function gologin(){
    alert("함수가 잘 호출 됩니다")
}

//redio button
function redio(){
    fm=document.getelementById("fm");
    //alert("asd")
    //라디오 버튼값은 여러개
    // for 문을 이용해서 체크여부 확인
    // 체크가 되었다면 checked가 True
    // 체크안된 버튼은 checked False
    for (i=0 ;i<fm.city.length;i++){
        if (fm.city[i].checked==true){
        alert(fm.city[i].value)}
        }
    }
function goinsert(){
    fm=document.getelementById("fm");
    //a.city.value
    alert(a.city.value);
    //location.href="/front/";
}

//checkbox
function out3(){
    fm=document.getElementById("fm")
    
    for (i=0;i<fm.city.length;i++){
        fm.city[i].checked=false;
    }
}
// city 가져와서 바로 value
function out2(){
    fm=document.getElementsByName("city")
    
    for (i=0;i<fm.length;i++){
        fm[i].checked=false;
    }
}
function out1(){
    fm=document.getElementById("fm")
    list=""
    for (i=0;i<fm.city.length;i++){
        if (fm.city[i].checked){
            if (list==""){
                list+=fm.city[i].value
            }
            else{
            list+=","+fm.city[i].value}
        }
    }
    //slice (시작 , 끝 ) 문자열 슬라이싱
    //list.slice(0,-1)
    alert(list)
}

//selectbox

function oneselect(){
    fm=document.getElementById("fm")
    alert(fm.city_one.value)
    alert(fm.city_one[4].selected)
}

function multiselect(){
    fm=document.getElementById("fm")
    list=""
    for(i=0;i<fm.city_multi.length;i++){
        //선택여부확인
        if (fm.city_multi[i].selected){
            list+=fm.city_multi[i].value+","
        }
    }
    alert(list.slice(0,-1))
}
function multiclear(){
    fm=document.getElementById("fm")

    for(i=0;i<fm.city_multi.options.length;i++){
        if(fm.city_multi.options[i].selected){
            fm.city_multi.options[i].selected=false
        }
    }
   
}

function multiclear1(){
    fm=document.getElementsByName("city_multi")
    for(i=0;i<fm[0].options.length;i++){
        
        fm[0].options[i].selected=true
        
    }
   
}