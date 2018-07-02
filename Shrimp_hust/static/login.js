/**
 * Created by tcz on 18-7-2.
 */


function get_id(target) {
    var username = {"name":document.getElementById("Username-log").value};
    //alert(document.getElementById("Username-log").value);
    //
     $.ajax(
        {
            url: '/Shrimp_hust/getid/',
            type: "POST",
            data: username,
            async: false,
            success: function (data) {
                rname = data;
                //movie_data = JSON.parse(data);
                //movie_data = data;
                //alert(2);
                //movie_data = data;
                //document.getElementById("show").textContent = "TCZ";

            }
        }
    );
    //alert(rname);
    //alert(movie_data);
    sessionStorage.setItem("rname", rname);
    //alert(data1);
    window.open("http://127.0.0.1:8000/Shrimp_hust/movie/");
}