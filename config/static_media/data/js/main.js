function check_status_anggota(value) {
    let nomor_a = $("#id_nomor_anggota").val();
    let nomor_a_part = nomor_a.substring(1,);

    /*
    if (value == "NON_AKTIF") {
        $("div.form-group.field-alasan_non_aktif").show();
        $("#id_nomor_anggota").val('N' + nomor_a_part).change();
    } else {
        $("div.form-group.field-alasan_non_aktif").hide();
    }
    if (value == "ANGGOTA_SIDI") {
        $("#id_nomor_anggota").val('D' + nomor_a_part).change();
    }
    if (value == "ANGGOTA_ANAK") {
        $("#id_nomor_anggota").val('A' + nomor_a_part).change();
    }
    if (value == "SIMPATISAN") {
        $("#id_nomor_anggota").val('S' + nomor_a_part).change();
    }
    */
}

function check_status_kehidupan(value) {
    if (value == "ALMARHUM") {
        $("div.form-group.field-alasan_non_aktif").show();
        $("div.form-group.field-lokasi_pemakaman").show();
        /*
        let dataField = $("id_status_anggota");
        let dataFieldVal = "NON_AKTIF";
        dataField.val(dataFieldVal);
        dataField.find('option[value="'+ dataFieldVal +'"]').prop('selected', 'selected');
        */
        $("#id_status_anggota").val("NON_AKTIF").change();
        $("#id_alasan_non_aktif").val("ALMARHUM").change();
        check_lokasi_pemakaman($("#id_lokasi_pemakaman").val());
    } else {
        $("#id_alasan_non_aktif").val("TIDAK_ADA").change();
        $("div.form-group.field-lokasi_pemakaman").hide();
        $("div.form-group.field-lokasi_sari_mulia").hide();
    }
}

function check_lokasi_pemakaman(value) {
    if (value == "YES_SARIMULIA") {
        $("div.form-group.field-lokasi_sari_mulia").show();
    } else {
        $("div.form-group.field-lokasi_sari_mulia").hide();
    }
}

function check_kepala_keluarga(value) {
    if (value == false) {
        $("div.form-group.field-nama_kepala_keluarga").show();
    } else {
        $("div.form-group.field-nama_kepala_keluarga").hide();
    }
}

function check_alasan_non_aktif(value) {
    if (value == "ALMARHUM") {
        $("#id_status_kehidupan").val("ALMARHUM").change();
        $("div.form-group.field-lokasi_pemakaman").show();
    } else {
        $("#id_status_kehidupan").val("HIDUP").change();
        $("div.form-group.field-lokasi_pemakaman").hide();
    }
}

let status_anggota = $("#id_status_anggota").val();
let status_kehidupan = $("#id_status_kehidupan").val();
let lokasi_pemakaman = $("#id_lokasi_pemakaman").val();
let kepala_keluarga = $("#id_kepala_keluarga").is(":checked");
let alasan_non_aktif = $("#id_alasan_non_aktif").val();

check_status_anggota(status_anggota);
check_status_kehidupan(status_kehidupan);
check_lokasi_pemakaman(lokasi_pemakaman);
check_kepala_keluarga(kepala_keluarga);
check_alasan_non_aktif(alasan_non_aktif);

$("#id_status_anggota").on('change', function() {
    check_status_anggota(this.value);
});
$("#id_status_kehidupan").on('change', function() {
    check_status_kehidupan(this.value);
});
$("#id_lokasi_pemakaman").on('change', function() {
    check_lokasi_pemakaman(this.value);
});
$("#id_kepala_keluarga").on('change', function() {
    check_kepala_keluarga($("#id_kepala_keluarga").is(":checked"));
});
/*
$("#id_alasan_non_aktif").on('change', function(e) {
    console.log(e);
    if (e.isTrigger == 3) {
        check_alasan_non_aktif(this.value);
    }
});
*/
if($('#id_verifikasi').length){
    let is_verifikasi = $("#id_verifikasi").is(":checked");

    if (is_verifikasi == false) {
        $("#id_verifikasi_badge_ok").hide();   
        $("#id_verifikasi_badge_nok").show();
    } else {
        $("#id_verifikasi_badge_ok").show();   
        $("#id_verifikasi_badge_nok").hide();
        $("#id_verifikasi").attr("disabled", true);
    }
}else{
    $("#id_verifikasi_badge_ok").hide();   
    $("#id_verifikasi_badge_nok").hide();
}

