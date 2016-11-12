startorstop = function (c) {

    cur = c.parent().parent().parent().parent().parent()
//        console.log(c.attr('title'))
    if (c.attr('title') == '启用') {
        cur.attr('zll_status', "1")
        c.parent().prev().children('span').text('启用')
        c.parent().prev().children('span').removeClass('label-danger')
        c.parent().prev().children('span').addClass('label-primary')
    }
    if (c.attr('title') == '停用') {
        cur.attr('zll_status', "0")
        c.parent().prev().children('span').text('停用')
        c.parent().prev().children('span').removeClass('label-primary')
        c.parent().prev().children('span').addClass('label-danger')
    }
//        console.log(cur.attr('zll_status'))
    swal("设置为" + c.attr('title'), "重启后才能生效.", "success");
}

var debug = true
var svb = true
address = function (mos, alname, adr, netmask) {

    if (mos == '从')
        style = "label-info"
    else if (mos == '主')
        style = "label-primary"
    else {
        mos = '新'
        style = "label-warning"
    }
    if (alname) {

        sss = ['<tr zll_name="' + alname + '" class=" zll_json">',
            '  <td>',
            '    <span class="label ' + style + ' pull-right">' + mos + '</span>IP地址</td>',
            '  <td>',
            '    <input type="text" class="form-control adr" zll-type="ipv4" maxlength="15" placeholder="IP地址" tabindex=1 value="' + adr + '"></td>',
            '  <td>子网掩码</td>',
            '  <td>',
            '    <input type="text" class="form-control netmask" zll-type="ipv4" maxlength="15" placeholder="255.255.255.255"  tabindex=1 value="' + netmask + '"></td>',
            '  <td>',
            '    <div class="btn-group">',
            '      <button class="btn btn-warning   address-clean" title="清空地址" type="button">',
            '        <i class="fa fa-ban"></i>清空地址</button>',
            '      <button class="btn btn-danger    something-delete " zll-name="从地址" type="button">',
            '        <i class="fa fa-times"></i>删除地址</button>',
            '    </div>',
            '  </td>',
            '</tr>'].join("");


        return sss

    }
    else {
        sss = ['<tr zll_name="' + alname + '" class="new zll_json">',
            '  <td>',
            '    <span class="label ' + style + ' pull-right">' + mos + '</span>IP地址</td>',
            '  <td>',
            '    <input type="text" class="form-control adr" zll-type="ipv4" maxlength="15" placeholder="IP地址" tabindex=1 ></td>',
            '  <td>子网掩码</td>',
            '  <td>',
            '    <input type="text" class="form-control netmask" zll-type="ipv4" maxlength="15" placeholder="255.255.255.255"  tabindex=1 ></td>',
            '  <td>',
            '    <div class="btn-group">',
            '      <button class="btn btn-warning   address-clean" title="清空地址" type="button">',
            '        <i class="fa fa-ban"></i>清空地址</button>',
            '      <button class="btn btn-danger    something-delete " zll-name="从地址" type="button">',
            '        <i class="fa fa-times"></i>删除地址</button>',
            '    </div>',
            '  </td>',
            '</tr>'].join("");


        return sss

    }
}


router = function (network, netmask, gateway) {
    if (network) {
        ss = ['<tr class="zll_json">',
            '  <td>目标网络IP</td>',
            '  <td>',
            '    <input type="text" class="form-control network" zll-type="ipv4" maxlength="15" placeholder="IP地址" tabindex=1 value="' + network + '"></td>',
            '  <td>子网掩码</td>',
            '  <td>',
            '    <input type="text" class="form-control netmask" zll-type="ipv4" maxlength="15" placeholder="255.0.0.0" tabindex=1 value="' + netmask + '"></td>',
            '  <td>网关地址</td>',
            '  <td>',
            '    <input type="text" class="form-control gateway" zll-type="ipv4" maxlength="15" placeholder="IP地址" tabindex=1 value="' + gateway + '"></td>',
            '  <td>',
            '    <div class="btn-group">',
            '      <button class="btn btn-danger something-delete" zll-name="路由" type="button">',
            '        <i class="fa fa-times"></i>删除路由</button>',
            '    </div>',
            '  </td>',
            '</tr>'].join("");


        return ss


    }
    else {
        mos = "新"
        style = "label-warning"

        ss = ['<tr class="new zll_json">',
            '  <td>',
            '    <span class="label' + style + 'pull-right">' + mos + '</span>目标网络IP</td>',
            '  <td>',
            '    <input type="text" class="form-control network" zll-type="ipv4" maxlength="15" placeholder="IP地址"  tabindex=1 ></td>',
            '  <td>子网掩码</td>',
            '  <td>',
            '    <input type="text" class="form-control netmask" zll-type="ipv4" maxlength="15" placeholder="255.0.0.0"  tabindex=1 ></td>',
            '  <td>网关地址</td>',
            '  <td>',
            '    <input type="text" class="form-control gateway" zll-type="ipv4" maxlength="15" placeholder="IP地址"  tabindex=1 ></td>',
            '  <td>',
            '    <div class="btn-group">',
            '      <button class="btn btn-danger something-delete" zll-name="路由" type="button">',
            '        <i class="fa fa-times"></i>删除路由</button>',
            '    </div>',
            '  </td>',
            '</tr>'].join("");


        return ss
    }

}


nints = function (netname, v) {

    ss = ['<div zll_int="lan' + v + '" class="panel panel-default lan' + v + '">',
        '  <div class="panel-heading">' + netname + '',
        '    <button class="btn btn-primary   address-add" type="button">',
        '      <i class="fa fa-plus"></i>增加地址</button></div>',
        '  <div class="panel-body">',
        '    <table class="table table-striped  table-condensed tb_adr">',
        '      <tbody></tbody>',
        '    </table>',
        '  </div>',
        '</div>'].join("");

    return ss
}


gapline = function (name, myadr, myport, hisadr, hisport) {
    if (name) {

        mos = ""
        ss = ['<tr class="zll_json">',
            '  <td>',
            '    <span class="label ' + style + ' pull-right">' + mos + '</span>',
            '  </td>',
            '  <td>',
            '    <input type="text" placeholder="名称" maxlength="8" class="form-control rule_name" tabindex=1  value="' + name + '"></td>',
            '  <td>',
            '    <input type="text" class="form-control rule_myadr" zll-type="ipv4" maxlength="15"  tabindex=1  placeholder="IP地址" value="' + myadr + '"></td>',
            '  <td>',
            '    <input type="text" placeholder="端口号" zll-type="port" value="' + myport + '" maxlength="5" tabindex=1  class="form-control rule_myport"></td>',
            '  <td>',
            '    <input type="text" class="form-control rule_hisadr" zll-type="ipv4" maxlength="15" tabindex=1  value="' + hisadr + '" placeholder="IP地址"></td>',
            '  <td>',
            '    <input type="text" placeholder="端口号" value="' + hisport + '" zll-type="port" tabindex=1  maxlength="5" class="form-control rule_hisport"></td>',
            '  <td>',
            '    <div class="btn-group">',
            '      <button class="btn btn-danger    something-delete " zll-name="策略" type="button">',
            '        <i class="fa fa-times"></i>删除策略</button>',
            '    </div>',
            '  </td>',
            '</tr>'].join("");

        return ss
    }
    else {
        mos = '新'
        style = "label-warning"
        ss = ['<tr class="new zll_json">',
            '  <td>',
            '    <span class="label ' + style + ' pull-right">' + mos + '</span></td>',
            '  <td>',
            '    <input type="text" placeholder="名称" maxlength="8" tabindex=1 class="form-control rule_name"></td>',
            '  <td>',
            '    <input type="text" class="form-control rule_myadr" tabindex=1 zll-type="ipv4" maxlength="15" placeholder="IP地址"></td>',
            '  <td>',
            '    <input type="text" placeholder="端口号" zll-type="port" tabindex=1 maxlength="5" class="form-control rule_myport"></td>',
            '  <td>',
            '    <input type="text" class="form-control rule_hisadr" tabindex=1 zll-type="ipv4" maxlength="15" placeholder="IP地址"></td>',
            '  <td>',
            '    <input type="text" placeholder="端口号" zll-type="port" tabindex=1 maxlength="5" class="form-control rule_hisport"></td>',
            '  <td>',
            '    <div class="btn-group">',
            '      <button class="btn btn-warning   something-delete " zll-name="策略" type="button">',
            '        <i class="fa fa-times"></i>删除策略</button>',
            '    </div>',
            '  </td>',
            '</tr>'].join("");
        return ss

    }

}
hsline = function (adr, netmask, gid, master, on) {
    var gid_shuzu = new Array();
    $.each($(".hs_gid"), function (s, m) {

        gid_shuzu.push(parseInt($(m).val()))


    })
    style = ""
    select_gid_begin = '<select class="form-control hs_gid" tabindex=1>'
    select_gid_mid = ''
    select_gid_end = '</select>'
    checkbox_master = ' <input type="checkbox" tabindex=1 class="hs_master">'
    checkbox_on = ' <input type="checkbox" tabindex=1 class="hs_on">'
    if (adr) {

        for (var i = 1; i <= 20; i++) {
            select_gid_mid += '<option value="' + i + '"'
            if (i == parseInt(gid))
                select_gid_mid += ' selected="true" '
            select_gid_mid += '>' + i + '</option>'
        }
        select_gid = select_gid_begin + select_gid_mid + select_gid_end;


        if (master == '1')
            checkbox_master = ' <input type="checkbox" tabindex=1 checked class="hs_master">'
        if (on == '1')
            checkbox_on = ' <input type="checkbox" tabindex=1 checked class="hs_on">'
        mos = ""

        ss = ['<tr class="new zll_json">',
            '  <td>',
            '    <span class="label ' + style + ' pull-right">' + mos + '</span>',
            '  </td>',
            '  <td>',
            '    <input type="text" zll-type="ipv4" maxlength="15" tabindex=1 placeholder="虚拟IP" value="' + adr + '" class="form-control hs_adr"></td>',
            '  <td>',
            '    <input type="text" placeholder="子网掩码" zll-type="ipv4" tabindex=1 maxlength="15" value="' + netmask + '" class="form-control hs_netmask"></td>',
            '  <td>',
            select_gid,
            '  </td>',
            '  <td>',
            checkbox_master,
            '  <td>',
            checkbox_on,
            '  <td>',
            '    <div class="btn-group">',
            '      <button class="btn btn-warning   something-delete " zll-name="虚拟IP" type="button">',
            '        <i class="fa fa-times"></i>删除虚拟IP</button>',
            '    </div>',
            '  </td>',
            '</tr>'].join("");

        return ss
    }
    else {
        for (var i = 1; i <= 20; i++) {
            if (jQuery.inArray(i, gid_shuzu) > -1)
                continue
            select_gid_mid += '<option value="' + i + '"'
            select_gid_mid += '>' + i + '</option>'
        }
        select_gid = select_gid_begin + select_gid_mid + select_gid_end;
        mos = '新'
        style = "label-warning"

        ss = ['<tr class="new zll_json">',
            '  <td>',
            '    <span class="label ' + style + ' pull-right">' + mos + '</span></td>',
            '  <td>',
            '    <input type="text" zll-type="ipv4" maxlength="15" placeholder="虚拟IP" class="form-control hs_adr"></td>',
            '  <td>',
            '    <input type="text" placeholder="子网掩码" zll-type="ipv4" maxlength="15" class="form-control hs_netmask"></td>',
            '  <td>',
            select_gid,
            '  </td>',
            '  <td>',
            checkbox_master,
            '  <td>',
            checkbox_on,
            '  <td>',
            '    <div class="btn-group">',
            '      <button class="btn btn-warning   something-delete " zll-name="虚拟IP" type="button">',
            '        <i class="fa fa-times"></i>删除虚拟IP</button>',
            '    </div>',
            '  </td>',
            '</tr>'].join("");

        return ss
    }

}
function checkINPUT(valid, value) {

    if (valid == 'port') {
        if (value >= 1 && value <= 65535)
            return true
        else
            return false
    }

    if (valid == 'ipv4') {
        var exp = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
        var reg = value.match(exp);
        if (reg == null)
            return false;
        else
            return true;
    }
}

function getstatus() {
    var reqpath = "/gap2py/index/get_status"
    $.getJSON(reqpath, {}, function (data) {
//            console.log(data.ia)
        if (data) {
            var mach = ["ia", "oa"];
            $.each(mach, function (i, val) {
                $("#" + val + "_uptime").text(eval('data.' + val + '.uptime'))
                $("#" + val + " .use_cpu").text(eval('data.' + val + '.cpu') + '%')
                $("#" + val + " .use_cpu_bar").css("width", eval('data.' + val + '.cpu') + '%')
                $("#" + val + " .use_mem").text(eval('data.' + val + '.memory') + '%')
                $("#" + val + " .use_mem_bar").css("width", eval('data.' + val + '.memory') + '%')
                $("#" + val + " .use_disk").text(eval('data.' + val + '.disk') + '%')
                $("#" + val + " .use_disk_bar").css("width", eval('data.' + val + '.disk') + '%')
            });
        }
    });
}

getlog = function () {
    var reqpath = "/gap2py/index/get_log"
    $.getJSON(reqpath, {}, function (data) {

        htmls = ''
        if (data.ia) {
            $.each(data.ia, function (i, val) {
                htmls += '<tr><td class="issue-info"><code>' + val + '</code></td></tr>'
            })

            $("#ialog").html(htmls)
            $("#iacount").html(data.iacount)
        }

        if (data.oa) {
            $.each(data.oa, function (i, val) {
                htmls += '<tr><td class="issue-info"><code>' + val + '</code></td></tr>'
            })

            $("#oalog").html(htmls)
            $("#oacount").text(data.oacount)
        }


    })


}


getconfig = function () {

    var reqpath = "/gap2py/index/get_config"
    $.getJSON(reqpath, {}, function (data) {

//            console.log(data)
        config = data
        if (data) {
            $(".ia .defaultgateway").val(data.ia.defaultgateway)
            $(".oa .defaultgateway").val(data.oa.defaultgateway)

            var mach = ["ia", "oa"];
            $.each(mach, function (s, m) {
                var ints = eval('data.' + m + '.interface');

                $.each(ints, function (i, val) {
                    if (val.name) {
                        var em = val.name.split('_');
                        var mos = "主";
                        if (em.length > 1)
                            mos = "从";
                        var tbody = $("." + m + " ." + em[0] + " .tb_adr tbody")[0]


                        var htm = address(mos, val.name, val.adr, val.netmask);
                        $(htm).appendTo(tbody)

                    }

                })


                var routers = eval('data.' + m + '.router');
                $.each(routers, function (i, val) {
                    if (val.network) {
                        var htm = router(val.network, val.netmask, val.gateway);
                        $(htm).appendTo($("." + m + " .router")[0])

                    }

                })
                var hsstatus = $("." + m + ".hs .status")
                if (eval('data.' + m + '.hs').on == "1") {

                    hsstatus.text('启用')
                    hsstatus.addClass('label-primary')
                }

                else {
                    hsstatus.text('停用')
                    hsstatus.addClass('label-danger')
                }
                $.each(eval('data.' + m + '.hs.rules'), function (s, mm) {

                    var tbody = $("." + m + ".hs tbody")[0]
                    var htm = hsline(mm.adr, mm.netmask, mm.gid, mm.master, mm.on);
                    $(htm).appendTo(tbody)

                })


            });

            var rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA", "IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"];


            $.each(rs, function (i, rule) {

//                    console.log(rs)
//                    console.log(rule)
                var rules = eval('data.' + rule);
//                    console.log(data.OUT_TCP)
                var rulestatus = $($("." + rule + " .status")[0])
                if (eval('data.' + rule).on == "1") {

                    rulestatus.text('启用')
                    rulestatus.addClass('label-primary')
                }

                else {
                    rulestatus.text('停用')
                    rulestatus.addClass('label-danger')
                }


                $.each(rules['rules'], function (i, val) {
//                        console.log($("." + rule + " .tcpinside tbody")[0])
                    if (val.name) {
                        var htm = gapline(val.name, val.myadr, val.myport, val.hisadr, val.hisport);
//                            console.log($(htm).html())

                        $(htm).appendTo($("." + rule + " .tcpinside tbody")[0])

                    }


                })
            })


        }
    });

}

CallBack = function () {


}
gap_reload = function () {

    swal({
        title: "<span id='rid'>重启!?<span>",
        text: "配置确定保存了吗?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "确认重启",
        cancelButtonText: "取消",
        closeOnConfirm: false,
        html: true
    }, function () {
        //sweetAlert({
        //    title: "正在重启!",
        //    text: "大约还需要60秒",
        //    closeOnConfirm: false,
        //    closeOnCancel: false,
        //    showCancelButton: false,
        //    showConfirmButton: false
        //});
        syms = 60
        $.ajax({
            url: "/gap2py/service/gap_reload/",
            data: {
                cmd: "reload",
                password: "zll"
            },
            type: "POST",
            dataType: 'json'
        });
        $(".showSweetAlert p").text('')
        $("#rid").text('正在重启中 !!')
        $(".sa-button-container").hide()
        function show() {

            $(".showSweetAlert p").text("大约还需要" + syms + "秒")
            syms = syms - 5
            if (syms <= 0)
                syms = 0
            $.ajax({
                url: '/gap2py/service/online/',
                dataType: 'json',
                data: {r:Math.random()},
                success: function () {
                    clearInterval(si1)
                    //swal.close()

                    swal({
                        title: "重启成功!",
                        text: "设备已经就绪",
                    })
                    location.href = '/gap2py/login/logout/'
                },
                timeout: 5000,
                error: function (jqXHR, status, errorThrown) {   //the status returned will be "timeout"
                    console.log(status)
                    console.log('关机中')
                }
            });

        }

        si1 = setInterval(show, 5000);// 注意函数名没有引号和括弧！


    });


}
gap_stop = function () {


    swal({
        title: "关机!?",
        text: "配置确定保存了吗?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "确认关机",
        cancelButtonText: "取消",
        closeOnConfirm: false
    }, function () {
        //sweetAlert({
        //    title: "正在关机!",
        //    text: "请稍等片刻",
        //    closeOnConfirm: false,
        //    closeOnCancel: false,
        //    showCancelButton: false,
        //    showConfirmButton: false
        //});
        $.ajax({
            url: "/gap2py/service/gap_stop/",
            data: {
                cmd: "stop",
                password: "zll"
            },
            type: "POST",
            dataType: 'json',
        });
        $(".showSweetAlert p").text('')
        $("#rid").text('正在关机中 !!')
        $(".sa-button-container").hide()
        function show() {
            $.ajax({
                url: '/gap2py/service/online/',
                dataType: 'json',
                data: {r:Math.random()},
                success: function () {
                },
                timeout: 5000,
                error: function (jqXHR, status, errorThrown) {   //the status returned will be "timeout"
                    clearInterval(si2)
                    //swal.close()

                    swal({
                        title: "设备即将关机!",
                        text: "15秒后可轻按圆形开关使其弹出",
                    }, function () {
                        $("html").html("<p style='text-align:center'>已停机</p>")
                    });


                }
            });

        }

        si2 = setInterval(show, 1000);// 注意函数名没有引号和括弧！

    });
}


getconfig_now = function () {


}

var config = {};
var newconfig = {};

createconfig_new = function () {

    $.each(['ia', 'oa'], function (i, mash) {
        jSing.create(newconfig, mash, {
            "interface": [],
            "router": [],
            "defaultgateway": "",
            "hs": {}
        });

        var defaultgateway = $("." + mash + " .defaultgateway").val().trim()
        if (defaultgateway)
            jSing.set(newconfig, mash, "defaultgateway", defaultgateway)


//            console.log($(".ia .tb_adr tbody .zll_json").html())


        var ints = $("." + mash + " .tb_adr tbody .zll_json")
        var ints_json = []
        $.each(ints, function (i, val) {

            var int_tr = $(val)
            var name = $.trim(int_tr.attr('zll_name'))
            var adr = $.trim(int_tr.find('.adr').val())
            var netmask = $.trim(int_tr.find('.netmask').val())

            //alert(name)
            if (name && adr && netmask) {

                var int_adr_info = {
                    "name": name,
                    "adr": adr,
                    "netmask": netmask
                };
//                    console.log(int_adr_info)
                ints_json.push(int_adr_info)
            }
        })

        //console.log(ints_json)

        var routers = $("." + mash + " .router .zll_json")

        var routers_json = []
        $.each(routers, function (i, val) {
            var int_tr = $(val)
            var network = $.trim(int_tr.find('.network').val())
            var netmask = $.trim(int_tr.find('.netmask').val())
            var gateway = $.trim(int_tr.find('.gateway').val())


            if (network && netmask && gateway) {

                var router_info = {
                    "network": network,
                    "netmask": netmask,
                    "gateway": gateway
                };
//                    console.log(router_info)
                routers_json.push(router_info)
            }
        })


//            console.log(routers_json)
        jSing.set(newconfig, mash, "interface", ints_json)
        jSing.set(newconfig, mash, "router", routers_json)

        var hss = $("." + mash + ".hs .zll_json")
        var hss_json = []
        $.each(hss, function (i, val) {
            var int_tr = $(val)
            var adr = $.trim(int_tr.find('.hs_adr').val())
            var netmask = $.trim(int_tr.find('.hs_netmask').val())
            var gid = $.trim(int_tr.find('.hs_gid').val())
            var master = $.trim(int_tr.find('.hs_master:checked').val())
            if (master)
                master = '1'
            else
                master = '0'
            var on = $.trim(int_tr.find('.hs_on:checked').val())
            if (on)
                on = '1'
            else
                on = '0'
            var hs_info = {
                "adr": adr,
                "netmask": netmask,
                "gid": gid,
                "master": master,
                "on": on
            };
            hss_json.push(hs_info)

        })
        if ($($("." + mash + ".hs .status")[0]).text() == "启用")
            var on = '1'
        else
            var on = '0'
        jSing.set(newconfig, mash, "hs", {
            "on": on,
            "rules": hss_json
        })


    });


    $.each(["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA", "IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"], function (i, rule) {


        if ($($("." + rule + " .status")[0]).text() == "启用")
            var on = '1'
        else
            var on = '0'

        var rules_tr = $("." + rule + " .zll_json")

        var rule_json = []


        $.each(rules_tr, function (i, val) {
            var rule_tr = $(val)

            var name = $.trim(rule_tr.find('.rule_name').val())
            var myadr = $.trim(rule_tr.find('.rule_myadr').val())
            var myport = $.trim(rule_tr.find('.rule_myport').val())
            var hisadr = $.trim(rule_tr.find('.rule_hisadr').val())
            var hisport = $.trim(rule_tr.find('.rule_hisport').val())

//                console.log(name)

            if (name && myadr && myport && hisadr && hisport) {

                var rule_info = {
                    "name": name,
                    "myadr": myadr,
                    "myport": myport,
                    "hisadr": hisadr,
                    "hisport": hisport
                };
//                    console.log(rule_info)
                rule_json.push(rule_info)
            }
        })

        jSing.create(newconfig, rule, {
            "on": on,
            "rules": rule_json
        });

    })

    var oldpass = $("#oldpass").val()
    var newpass1 = $("#newpass1").val()
    var newpass2 = $("#newpass2").val()


    if (oldpass && newpass1 && newpass2)
        if (newpass1 == newpass2)
            jSing.create(newconfig, "changepass", {
                "oldpass": oldpass,
                "newpass1": newpass1,
                "newpass2": newpass2
            });
    //console.log(JSON.stringify(newconfig))
    //console.log(JSON.stringify(config))
    //console.log(JSON.stringify(newconfig) == JSON.stringify(config))

}


styleset = function () {

    $("body").addClass('fixed-sidebar');
    $('.sidebar-collapse').slimScroll({
        height: '100%',
        railOpacity: 0.9
    });
    if (localStorageSupport) {
        localStorage.setItem("fixedsidebar", 'on');
    }
    $('#boxedlayout').prop('checked', false);
    $("body").removeClass('boxed-layout');
    $(".footer").addClass('fixed');

    if (localStorageSupport) {
        localStorage.setItem("boxedlayout", 'off');
    }

    if (localStorageSupport) {
        localStorage.setItem("fixedfooter", 'on');
    }

}

need_restart_set = function () {

    $.getJSON('/gap2py/service/need_restart', {}, function (data) {
        if (data.succ) {

            $("#nr_tip").text('1')
            $("#nr_info").text('配置已经改变,重启之后才能生效!')


            swal({
                title: "提示!",
                text: "配置已经改变,重启之后才能生效!",
                type: "warning",
                showCancelButton: false,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确认",
                closeOnConfirm: true
            });

        }
    });


}

setgaptime = function (){


  $.getJSON('/gap2py/service/gap_time', {}, function (data) {
        if (data.succ) {

            $("#systime").text(data.time)
          
        }
    });



}
// common variables
var iBytesUploaded = 0;
var iBytesTotal = 0;
var iPreviousBytesLoaded = 0;
var iMaxFilesize = 1073741824; // 1G
var oTimer = 0;
var sResultFileSize = '';

function secondsToTime(secs) { // we will use this function to convert seconds in normal time format
    var hr = Math.floor(secs / 3600);
    var min = Math.floor((secs - (hr * 3600))/60);
    var sec = Math.floor(secs - (hr * 3600) -  (min * 60));
    if (hr < 10) {hr = "0" + hr; }
    if (min < 10) {min = "0" + min;}
    if (sec < 10) {sec = "0" + sec;}
    if (hr) {hr = "00";}
    return hr + ':' + min + ':' + sec;
};

function bytesToSize(bytes) {
    var sizes = ['Bytes', 'KB', 'MB'];
    if (bytes == 0) return 'n/a';
    var i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
    return (bytes / Math.pow(1024, i)).toFixed(1) + ' ' + sizes[i];
};
function fileSelected() {
    // hide different warnings
    document.getElementById('upload_response').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    document.getElementById('error2').style.display = 'none';
    document.getElementById('abort').style.display = 'none';
    document.getElementById('warnsize').style.display = 'none';
    // get selected file element
    var oFile = document.getElementById('image_file').files[0];

    if (oFile.name != 'newsys.bin') {

        document.getElementById('error').style.display = 'block';
        return;
    }

    // little test for filesize
    if (oFile.size > iMaxFilesize) {

        document.getElementById('warnsize').style.display = 'block';
        return;
    }
    $("#StartUploading").show('quick')
}
function needUpdate(){

swal({   title: "确定要升级吗?", 
  text: "升级有风险!", 
    type: "warning",   
    showCancelButton: true, 
      confirmButtonColor: "#DD6B55", 
        confirmButtonText: "确定升级", 
          cancelButtonText: "取消",  
           closeOnConfirm: false,  
            closeOnCancel: false },
            function(isConfirm){  
             if (isConfirm) {   
               swal("升级即将开始!", 
                "系统稍后开始升级请勿操作", 
                "success");   } 
               else {   
                 swal("提示！", 
                    "升级已经被取消",
                    "error"); 
                      } 

                  });




}

function startUploading() {
    // cleanup all temp states
    iPreviousBytesLoaded = 0;
    document.getElementById('upload_response').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    document.getElementById('error2').style.display = 'none';
    document.getElementById('abort').style.display = 'none';
    document.getElementById('warnsize').style.display = 'none';
    document.getElementById('progress_percent').innerHTML = '';
    var oProgress = document.getElementById('progress');
    oProgress.style.display = 'block';
    oProgress.style.width = '0px';
    // get form data for POSTing
    //var vFD = document.getElementById('upload_form').getFormData(); // for FF3
    var vFD = new FormData(document.getElementById('upload_form')); 
    // create XMLHttpRequest object, adding few event listeners, and POSTing our data
    var oXHR = new XMLHttpRequest();        
    oXHR.upload.addEventListener('progress', uploadProgress, false);
    oXHR.addEventListener('load', uploadFinish, false);
    oXHR.addEventListener('error', uploadError, false);
    oXHR.addEventListener('abort', uploadAbort, false);
    oXHR.open('POST', '/gap2py/service/gap_newsystem');
    oXHR.send(vFD);
    // set inner timer
    oTimer = setInterval(doInnerUpdates, 300);
}
function doInnerUpdates() { // we will use this function to display upload speed
    var iCB = iBytesUploaded;
    var iDiff = iCB - iPreviousBytesLoaded;
    // if nothing new loaded - exit
    if (iDiff == 0)
    return;
    iPreviousBytesLoaded = iCB;
    iDiff = iDiff * 2;
    var iBytesRem = iBytesTotal - iPreviousBytesLoaded;
    var secondsRemaining = iBytesRem / iDiff;
    // update speed info
    var iSpeed = iDiff.toString() + 'B/s';
    if (iDiff > 1024 * 1024) {
        iSpeed = (Math.round(iDiff * 100/(1024*1024))/100).toString() + 'MB/s';
    } else if (iDiff > 1024) {
        iSpeed =  (Math.round(iDiff * 100/1024)/100).toString() + 'KB/s';
    }
    document.getElementById('speed').innerHTML = iSpeed;
    document.getElementById('remaining').innerHTML = '| ' + secondsToTime(secondsRemaining);        
}
function uploadProgress(e) { // upload process in progress
    if (e.lengthComputable) {
        iBytesUploaded = e.loaded;
        iBytesTotal = e.total;
        var iPercentComplete = Math.round(e.loaded * 100 / e.total);
        var iBytesTransfered = bytesToSize(iBytesUploaded);
        document.getElementById('progress_percent').innerHTML = iPercentComplete.toString() + '%';
        document.getElementById('progress').style.width = iPercentComplete.toString() + '%';
        document.getElementById('b_transfered').innerHTML = iBytesTransfered;
        if (iPercentComplete == 100) {
            var oUploadResponse = document.getElementById('upload_response');
            oUploadResponse.innerHTML = '<h1>正在上传...请稍等！</h1>';
            oUploadResponse.style.display = 'block';
        }
    } else {
        document.getElementById('progress').innerHTML = '未能完成';
    }
}
function uploadFinish(e) { // upload successfully finished
    var oUploadResponse = document.getElementById('upload_response');
    oUploadResponse.innerHTML = e.target.responseText;
    oUploadResponse.style.display = 'block';
    document.getElementById('progress_percent').innerHTML = '100%';
    document.getElementById('progress').style.width = '100%';
    document.getElementById('remaining').innerHTML = '| 00:00:00';
    clearInterval(oTimer);
    $("#NNeedUpdate").show('quick')
}
function uploadError(e) { // upload error
    document.getElementById('error2').style.display = 'block';
    clearInterval(oTimer);
}  
function uploadAbort(e) { // upload abort
    document.getElementById('abort').style.display = 'block';
    clearInterval(oTimer);
}
$(document).ready(function () {
    $("#NeedUpdate,#StartUploading").hide('quick')
    setInterval(setgaptime,1000)
    styleset()
    need_restart_set()
    getstatus()
    getconfig()
    getlog()

    $(".startorstop").on('click', function () {
        startorstop($(this))
    })
    //var Status = setInterval(getstatus, 60000);
    $("#changt").on('click',function(){

       swal({   title: "输入当前时间",  
        text: "例: <code>201611111111</code> 表示 <code>2016-11-11 11:11:00</code>", 
          type: "input",  
           showCancelButton: true, 
           html:true,
            closeOnConfirm: false, 
              animation: "slide-from-top",  
               inputPlaceholder: "201611111111" }, 
               function(inputValue){   
                if (inputValue === false) return false;  
                    if (inputValue === "") {   
                      swal.showInputError("请按照正确格式填写时间");     
                      return false   
                  }     
                   swal("提示", "设置完成!"); 
               });


    })

    $(".zll_fresh li").on('click', function () {
//            console.log($(this).attr('zll_act'))
        if ($(this).attr('zll_act') == '0') {
            //clearInterval(Status);
            $("#refresh_info").html('不刷新')
        }
        else if ($(this).attr('zll_act') == '60') {
            //clearInterval(Status);
            //Status = setInterval(getstatus, 60000);
            $("#refresh_info").html('每1分钟刷新')
        }
        else if ($(this).attr('zll_act') == '600') {
            //clearInterval(Status);
            //Status = setInterval(getstatus, 600000);
            $("#refresh_info").html('每10分钟刷新')
        }
        else
            ;
    })


//        $(document).on("click", ".address-delete",function () {
//            var $tmp = $(this)
//
//                swal({
//                    title: "确定吗?",
//                    text: "确定要删除这个地址吗?",
//                    type: "warning",
//                    showCancelButton: true,
//                    confirmButtonColor: "#DD6B55",
//                    confirmButtonText: "删除!",
//                    closeOnConfirm: false
//                }, function (isConfirm) {
//                    if (isConfirm) {
////                        $tmp.parent().parent().remove()
//                        swal("成功!", "从地址已经删除!.", "成功");
//                    } else {
//                        swal("取消删除!", "取消删除从地址已经删除!.", "取消删除成功");
//                    }
//
//                });
//        });
    var ints = ["LAN1", "LAN2", "LAN3", "LAN4", "LAN5"];


    for (var i = 0; i < ints.length; i++) {
        $(".address").append(nints(ints[i], i+1))
    }




    $(document).on("click", ".save", function () {
        createconfig_new()

        console.log(newconfig)
        var $tmp = $(this)
        swal({
            title: "确定吗?",
            text: "确定要保存吗?点击确认保存后,请耐心等待...",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "确认保存",
            cancelButtonText: "取消",
            closeOnConfirm: false
        }, function () {
            if (svb) {
                svb = false
                $.post("save",
                    {
                        cmd: "save",
                        config: JSON.stringify(newconfig)
                    },
                    function (data, status) {
                        svb = true
                        if (jQuery.parseJSON(data).succ) {
                            swal("成功!", "配置已经保存,重启后生效.", "success");
                        }
                        else
                            swal("不成功!", "配置保存出错", "warning");
                    });
            }
            else {
                alert("配置正在保存中,请勿连续点击..")
            }
        });
    });


    $(document).on("click", ".something-delete", function () {
        var $tmp = $(this)
        if ($tmp.parent().parent().parent().hasClass('new'))
            $tmp.parent().parent().parent().remove();
        else {
//                console.log($tmp.parent().parent().parent())
            swal({
                title: "确定吗?",
                text: "确定要删除这条" + $tmp.attr('zll-name') + "吗?",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确认删除",
                cancelButtonText: "取消",
                closeOnConfirm: false
            }, function () {
                if (debug)
//                        console.log($tmp.parent().parent())
                    $tmp.parent().parent().parent().remove()
                swal("成功!", $tmp.attr("zll-name") + "已经删除.重启后生效", "success");
            });
        }
    });


    $(document).on("click", ".address-add", function () {
        lasttr = $(this).parent().parent().find('tbody > tr:last-child')

        intname = $(this).parent().parent().attr('zll_int')

        if (lasttr.hasClass(' zll_json')) {
            name = lasttr.attr('zll_name')

            if (name == intname) {
                $(this).parent().parent().find('tbody').append(address("从", name + "_alias0", "", ""))
            } else {
                var em = name.split('alias');
                newname = intname + "_alias" + String(parseInt(em[em.length - 1]) + 1)
                $(this).parent().parent().find('tbody').append(address("从", newname, "", ""))
            }
        }
        else
            $(this).parent().parent().find('tbody').append(address("主", intname, "", ""))
    });


    $(document).on("blur", "[zll-type]", function () {
        $(this).removeClass('animated tada')
//            console.log($(this).val())
        if ($(this).val()) {
            flag = checkINPUT($(this).attr('zll-type'), $(this).val())
//                console.log(flag)
            if (flag) {
            } else {
                $(this).focus()
                swal({
                    title: $(this).attr('placeholder') + "格式错误",
                    text: "请修改" + $(this).attr('placeholder') + "格式"
                });
                $(this).addClass('animated tada')
            }
        }
//            console.log(checkINPUT($(this).val()))
    });
    $(document).on("blur", "#newpass2,#oldpass,#newpass1", function () {
        oldpass = $("#oldpass").val()
        if (oldpass) {
            newpass1 = $("#newpass1").val()
            newpass2 = $("#newpass2").val()
            if (newpass1 && newpass2) {

                if (newpass1 == newpass2) {
                } else {
                    swal({
                        title: "新密码两次输入必须相同",
                        text: "请修改两次新密码"
                    });
                    $("#newpass1").val('')
                    $("#newpass2").val('')
                }

            }
        }
    });

    $(document).on("blur","#newpass1,#newpass2",function(){
        var newpwd = $(this).val();  
  
        var reg = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[~!@#$%^&*()_+`\-={}:";'<>?,.\/]).{11,25}$/;  
        var flag = reg.test(newpwd);  
        if(flag == false){  
            swal("新密码必须由 11-25位字母、数字、特殊符号线组成.");      
            return false;     
        }  
    });

    $(document).on("click", ".router-add", function () {
        $(this).parent().parent().find('tbody').append(router())
    });

    $(document).on("click", ".gapline-add", function () {
        $(this).parent().parent().find('tbody').append(gapline())
    });
    $(document).on("click", ".hsline-add", function () {
        var check1 = new Array();
        var check2 = new Array();
        $.each($(".hs_adr"), function (s, m) {
            check1.push($(m).val())
        })
        if (jQuery.inArray("", check1) > -1) {
            swal("虚拟IP不能为空!", "添加虚拟IP失败", "warning");
            return;
        }
        $.each($(".hs_netmask"), function (s, m) {

            check2.push($(m).val())
        })
        if (jQuery.inArray("", check2) > -1) {
            swal("子网掩码不能为空!", "添加虚拟IP失败", "warning");
            return;
        }
        $(this).parent().parent().find('tbody').append(hsline())
    });

    $(document).on("click", ".address-clean", function () {

        $(this).parent().parent().parent().find('input').val('')
        var $tmp = $(this)

        if ($tmp.parent().parent().parent().hasClass('new')) {


            ;

        }
        else
            swal({
                title: "成功",
                text: "清空地址成功,重启后生效",
                type: "success"
            });

    });
});
