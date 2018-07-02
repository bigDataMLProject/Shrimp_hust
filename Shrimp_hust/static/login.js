/**
 * Created by tcz on 18-7-2.
 */


function get_id(target) {
    var username = {"name":document.getElementById("Username-log").value};
     $.ajax(
        {
            url: '/Shrimp_hust/getid/',
            type: "POST",
            data: username,
            async: false,
            success: function (data) {
                rname = data;

            }
        }
    );
    sessionStorage.setItem("rname", rname);
    window.open("http://127.0.0.1:8000/Shrimp_hust/movie/");
}