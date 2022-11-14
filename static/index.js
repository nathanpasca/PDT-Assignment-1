function square() {
    var numberClient = document.getElementById("sqrnumber").value;

    var url = "/square";

    axios({
        method: "post",
        url: url,
        data: {
            sqrnumber: numberClient,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            console.log(response);
            document.getElementById("result").innerHTML = "Result: " + result["result"];
            // document.getElementById("message").innerHTML = result["message"];
        },
        (error) => {
            console.log(error);
        }
    );
}

function triangle() {
    var a = document.getElementById("a").value;
    var b = document.getElementById("b").value;
    
    var url = "/triangle";

    axios({
        method: "post",
        url: url,
        data: {
            a: a,
            b: b,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            console.log(response);
            document.getElementById("result").innerHTML = "Result: " +  result["result"];
            // document.getElementById("message").innerHTML = result["message"];
        },
        (error) => {
            console.log(error);
        }
    );
}

function convert() {
    var numberClient = document.getElementById("cvtnumber").value;

    var url = "/convert";

    axios({
        method: "post",
        url: url,
        data: {
            cvtnumber: numberClient,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            console.log(response);
            document.getElementById("result").innerHTML = "Your score is: " + result["result"];
            document.getElementById("message").innerHTML = "Congratulation! You got " + result["message"];
        },
        (error) => {
            console.log(error);
        }
    );
}