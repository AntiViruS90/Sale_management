$(document).ready(function () {

    $('#configuration').click(function () {
        $('#configuration_menu').slideDown(200);
        $('#configuration_angle').css({
            'transform': 'rotate(-90deg)'
        });
        $('#settings_menu').slideUp(200);
        $('#settings_angle').css({
            'transform': 'rotate(0deg)'
        });
    });

    $('#inventory').click(function () {
        $('#inventory_menu').slideDown(200);
        $('#inventory_angle').css({
            'transform': 'rotate(-90deg)'
        });
        $('#configuration_menu').slideUp(200);
        $('#configuration_angle').css({
            'transform': 'rotate(0deg)'
        });

    });

    $('#product').click(function () {
        $('#product_menu').slideDown(200);
        $('#product_angle').css({
            'transform': 'rotate(-90deg)'
        });
        $('#inventory_menu').slideUp(200);
        $('#inventory_angle').css({
            'transform': 'rotate(0deg)'
        });

    });

    $('#POS').click(function () {
        $('#POS_menu').slideDown(200);
        $('#POS_angle').css({
            'transform': 'rotate(-90deg)'
        });
        $('#product_menu').slideUp(200);
        $('#product_angle').css({
            'transform': 'rotate(0deg)'
        });

    });

    $('#settings').click(function () {
        $('#settings_menu').slideDown(200);
        $('#settings_angle').css({
            'transform': 'rotate(-90deg)'
        });
        $('#POS_menu').slideUp(200);
        $('#POS_angle').css({
            'transform': 'rotate(0deg)'
        });

    });

    $('.dropdown-toggle').click(function () {
        $('.dropdown-menu').slideDown(200);
    })
    $('#fa-close').click(function () {
        $('.dropdown-menu').slideUp(200);
    })












});