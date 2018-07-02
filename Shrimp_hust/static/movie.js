/**
 * Created by tcz on 18-6-30.
 */
$(document).ready(function () {
    data = sessionStorage.getItem("rname");
    rname = JSON.parse(data);
    //alert(res["name"]);
    for(i =0; i<13; i++){
        recom = "rname" + i;
        document.getElementById(recom).textContent = rname[recom];
    }


    }
)

function search_movie(target) {
    var movie_type = {"type":$(target).text()};
    //alert(movie_type);

    $.ajax(
        {
            url: '/Shrimp_hust/type/',
            type: "POST",
            data: movie_type,
            //dataType: 'json',
            success: function (data){
                data = JSON.parse(data);
                // alert(data["src0"]);
                for(i=0;i<6;i++){
                    var src = "src"+i;
                    //alert(src);
                    var type = "type"+i;
                    var name = "name"+i;
                    document.getElementById(src).src = data[src];
                    document.getElementById(type).textContent = data[type];
                    document.getElementById(name).textContent = data[name];

    }
            }
        }
    )

}

function show_movie(target) {
    var movie_name = {"name":$(target).text()};
    // window.open("http://www.baidu.com");

     $.ajax(
        {
            url: '/Shrimp_hust/show/',
            type: "POST",
            data: movie_name,
            async: false,
            success: function (data) {
                //data1 = data;
                //movie_data = JSON.parse(data);
                movie_data = data;
                //alert(2);
                //movie_data = data;
                //document.getElementById("show").textContent = "TCZ";

            }
        }
    );
    // alert(3);
    //alert(movie_data);
    sessionStorage.setItem("key", movie_data);
    //alert(data1);
    window.open("detail/");
}

function select_movie(){
    if(event.keyCode == 13){
        var info = {"info": document.getElementById("search").value};
        alert(document.getElementById("search").value)
        $.ajax(
        {
            url: '/Shrimp_hust/select/',
            type: "POST",
            data: info,
            async: false,
            success: function (data) {
                movie_data = data;
            }
        }
    );
    }
}


