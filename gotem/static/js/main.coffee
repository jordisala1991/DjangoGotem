window.onpopstate = (event) ->

    load_sprint_callback(event.state.data) if event.state isnt null


form_error = (fieldname, error) ->
    
    input = $("#id_#{fieldname}")
    error_msg = $('<span />').addClass('ajax-error').text(error[0])
    error_msg.insertAfter(input)

    
clear_errors = (form) ->
    
    $('.ajax-error', $(form)).remove()


load_sprint_callback = (data) ->
    
    sprint_detail = $(data).find('#active-sprint').html()
    objectives = $(data).find('#objective-list').html()
    form = $(data).find('#objective-form').html()
    sprints = $(data).find('#sprint-list').html()
    $('#active-sprint').html sprint_detail
    $('#objective-list').html objectives
    $('#objective-form').html form
    $('#sprint-list').html sprints
    false


@load_sprint = (sprint_id) ->
    
    callback = (response) ->
        load_sprint_callback(response, sprint_id)
        history.pushState({ data : response }, "Sprint_#{sprint_id}", "/sprint/#{sprint_id}/")
    $.get "/sprint/#{sprint_id}", callback, 'html'
    false


$(document).ready ->
    history.replaceState({ data : $('html').html() }, null, null);
    $('#objective-form').submit (e) ->
        e.preventDefault()
        clear_errors(@)
        $.ajax
            type: $(@).attr 'method'
            data: $(@).serialize()
            url: $(@).attr 'action'
            success: (data, textStatus, jqXHR) ->
                $('#id_description').val ''
                $('#id_name').val ''
                $('#objective-list').prepend data
            error: (data, textStatus, jqXHR) ->
                errors = $.parseJSON data.responseText
                form_error index, value for index, value of errors
        false