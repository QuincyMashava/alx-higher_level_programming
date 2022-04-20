$(function () {
  $('#btn_translate').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/' + $('#city_search').val() + '%22)&format=json', function (resp, status) {
      if (status === 'success') {
        $('#hello').text(resp.query.results.hello);
      }
    });
  });
});
