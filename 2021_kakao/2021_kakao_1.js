function solution(new_id) {
    var step1 = new_id.toLowerCase()
    var step2 = ''
    var isOk = ['-',"_","."]
    const alpha = /^[a-zA-Z]*$/;
    const num = /^[0-9]*$/;
    for (var i = 0; i < step1.length; i++){
        if(isOk.includes(step1[i])){
            step2 += step1[i]
        }else if(alpha.test(step1[i])){
            step2 += step1[i]
        }else if(num.test(step1[i])){
            step2 += step1[i]
        }
    }
    var step3 = ''
    var cnt = 0
    for (var i = 0; i < step2.length; i++){
        if(step2[i] === '.'){
            if (cnt === 0){
                step3 += step2[i]
                cnt += 1
            }
        }else{
            var cnt = 0
            step3 += step2[i]
        }
    }
    var step4 = ''
    for (var i = 0; i < step3.length; i++){
        if(i === 0 || i === (step3.length-1)){
            if (step3[i] !== '.'){
                step4 += step3[i]
            }
        }else{
            step4 += step3[i]
        }
    }
    var step5 = step4
    if (step5 === ''){
        step5 = 'a'
    }
    var step6 = step5
    if (step6.length >= 16){
        var step6 = step5.substring(0,15)
    }
    if (step6[step6.length-1] === '.'){
        var step6 = step6.substring(0,step6.length-1)
    }
    var step7 = step6
    if (step7.length <= 2){
        while (step7.length < 3){
            step7 += step7[step7.length-1]
        }
    }
    var answer = step7
    return answer
}
// console.log(solution("z-+.^."))


// console.log(solution("...!@BaT#*..y.abcdefghijklm"))
// console.log(solution("z-+.^."))
console.log(solution("=.="))
console.log(solution("123_.def"))
console.log(solution("abcdefghijklmn.p"))

