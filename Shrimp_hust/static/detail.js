 /**
 * Created by tcz on 18-7-1.
 */
$(document).ready(function () {
    data = sessionStorage.getItem("key");
    //alert(data);
    res = JSON.parse(data);
    //alert(res["name1"]);
    document.getElementById("name").textContent = res["name"];
    document.getElementById("src").src = res["src"];
    document.getElementById("director").textContent ="导演：" + res["director"];
    document.getElementById("editor").textContent ="编剧：" + res["editor"];
    document.getElementById("actor").textContent = "演员：" + res["actor"];
    document.getElementById("type").textContent ="类型：" + res["type"];
    document.getElementById("area").textContent ="国家/地区：" + res["area"];
    document.getElementById("time").textContent ="时长：" + res["time"] +"分钟";
    document.getElementById("rate").textContent ="评分：" + res["rate"];
    for(i=1;i<6;i++){
        var name = "name" + i ;
        var type = "type" + i;
        var src = "src" + i;
        document.getElementById(src).src =res[src];
        document.getElementById(name).textContent =res[name];
        document.getElementById(type).textContent =res[type];

    }
    }
);



