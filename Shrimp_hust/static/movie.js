/**
 * Created by tcz on 18-6-30.
 */
$(document).ready(function () {
        data = sessionStorage.getItem("rname");
        rname = JSON.parse(data);
        for (i = 0; i < 13; i++) {
            recom = "rname" + i;
            document.getElementById(recom).textContent = rname[recom];
        }
    }
)

function search_movie(target) {
    var movie_type = {"type": $(target).text()};
    $.ajax(
        {
            url: '/Shrimp_hust/type/',
            type: "POST",
            data: movie_type,
            success: function (data) {
                data = JSON.parse(data);
                for (i = 0; i < 6; i++) {
                    var src = "src" + i;
                    var type = "type" + i;
                    var name = "name" + i;
                    document.getElementById(src).src = data[src];
                    document.getElementById(type).textContent = data[type];
                    document.getElementById(name).textContent = data[name];

                }
            }
        }
    )

}

function show_movie(target) {
    var movie_name = {"name": $(target).text()};
    $.ajax(
        {
            url: '/Shrimp_hust/show/',
            type: "POST",
            data: movie_name,
            async: false,
            success: function (data) {
                movie_data = data;
            }
        }
    );
    sessionStorage.setItem("key", movie_data);
    window.open("detail/");
}

function select_movie() {
    if (event.keyCode == 13) {
        var info = {"info": document.getElementById("search").value};
        $.ajax(
            {
                url: '/Shrimp_hust/select/',
                type: "POST",
                data: info,
                async: false,
                success: function (data) {
                    data = JSON.parse(data);
                    var num = data["num"];
                    if (num == 0) {
                        alert("NO MOVIE WITH SUCH KEYWORD!!!")
                    }
                    else if (num < 6) {
                        for (i = 0; i < num; i++) {
                            var src = "src" + i;
                            var type = "type" + i;
                            var name = "name" + i;
                            document.getElementById(src).src = data[src];
                            document.getElementById(type).textContent = data[type];
                            document.getElementById(name).textContent = data[name];
                        }
                    }
                    else if(num >= 6)
                    {
                        for (i = 0; i < 6; i++) {
                            var src1 = "src" + i;
                            var type1 = "type" + i;
                            var name1 = "name" + i;
                            document.getElementById(src1).src = data[src1];
                            document.getElementById(type1).textContent = data[type1];
                            document.getElementById(name1).textContent = data[name1];
                        }
                    }
                }

            }
        );
    }
}


