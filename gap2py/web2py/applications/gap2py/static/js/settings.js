/**
 * Created by zhulielie on 16/7/26.
 */


$(function () {


    //$.getJSON()
    $.getJSON('dtype', {r: Math.random()}, function (data) {
        $("#ct").val(data.ct)
        $("#cd").val(data.cd)
        $("#rt").val(data.rt)
        $("#rd").val(data.rd)
    })

    $("#save").on('click', function () {

        var nowt = $("#nct").val()
        var nowd = $("#ncd").val()
        $.getJSON('sdtype', {r: Math.random(), rt: nowt, rd: nowd}, function (data) {

            if (data) {

                if (data.fb == 1) {
                    $("#rt").val(nowt)
                    $("#rd").val(nowd)
                    sweetAlert("保存成功!")
                }
                else if (data.fb == -1) {
                    sweetAlert("什么都没有修改!!")
                }
                else
                    sweetAlert("哪里出错了!")
            }
        })


    })


})