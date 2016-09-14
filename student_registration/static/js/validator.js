/**
 * Created by Ali on 2016-09-12.
 */

var validation_mapping = new Array();

function validateSection(frame, sectionIndex)
{
    var result = true;

    if(sectionIndex.toString() in validation_mapping)
    {
        console.log(validation_mapping[sectionIndex]);
        var callback  = validation_mapping[sectionIndex];
        result = callback();
    }
    return result;
}

function validateSection5()
{
    var valid = true ;
    var selectedOption = $("#id_id_type").val();
    if(selectedOption == 1) {
        if($('#id_id_number').val() == ""){
            $('#id_number_UNHCR_Other_error').show();
            valid = false ;
        }else{
            $('#id_number_UNHCR_Other_error').hide();
        }
    }else if (selectedOption == 2 || selectedOption == 3 || selectedOption == 4|| selectedOption == 5) {

        if($('#id_id_number').val() == ""){
            $('#id_number_UNHCR_Other_error').show();
            valid = false ;
        }else{
            $('#id_number_UNHCR_Other_error').hide();
        }

         if($('#id_first_name').val() == ""){
            $('#first_name_error').show();
            valid = false ;
        }else{
            $('#first_name_error').hide();
        }

         if($('#id_father_name').val() == ""){
            $('#father_name_error').show();
            valid = false ;
        }else{
            $('#father_name_error').hide();
        }

         if($('#id_last_name').val() == ""){
            $('#last_name_error').show();
            valid = false ;
        }else{
            $('#last_name_error').hide();
        }

         if($('#id_mother_fullname').val() == ""){
            $('#mother_fullname_error').show();
            valid = false ;
        }else{
            $('#mother_fullname_error').hide();
        }

         if($('#id_age').val() == ""){
            $('#age_error').show();
            valid = false ;
        }else{
            $('#age_error').hide();
        }

         if($('#id_sex').val() == ""){
            $('#gender_error').show();
            valid = false ;
        }else{
            $('#gender_error').hide();
        }

        if($('#id_relation_to_householdhead').val() == ""){
            $('#relationship_householdhead_error').show();
            valid = false ;
        }else{
            $('#relationship_householdhead_error').hide();
        }

    }else if (selectedOption == 6) {
         if($('#id_first_name').val() == ""){
            $('#first_name_error').show();
            valid = false ;
        }else{
            $('#first_name_error').hide();
        }

         if($('#id_father_name').val() == ""){
            $('#father_name_error').show();
            valid = false ;
        }else{
            $('#father_name_error').hide();
        }

         if($('#id_last_name').val() == ""){
            $('#last_name_error').show();
            valid = false ;
        }else{
            $('#last_name_error').hide();
        }

         if($('#id_mother_fullname').val() == ""){
            $('#mother_fullname_error').show();
            valid = false ;
        }else{
            $('#mother_fullname_error').hide();
        }

         if($('#id_age').val() == ""){
            $('#age_error').show();
            valid = false ;
        }else{
            $('#age_error').hide();
        }

         if($('#id_sex').val() == ""){
            $('#gender_error').show();
            valid = false ;
        }else{
            $('#gender_error').hide();
        }

        if($('#id_relation_to_householdhead').val() == ""){
            $('#relationship_householdhead_error').show();
            valid = false ;
        }else{
            $('#relationship_householdhead_error').hide();
        }
    }
   // alert(result);
    return valid;
}

function validate_add_child_noid()
{
    var valid = true ;
    var form = $('.bootbox-body').find('#add_child_noid_form');
    // tr.append($('<td>').html(form.find('#id_school').find(':selected').text()));

    if(form.find('#id_first_name').val() == ""){
        form.find('#first_name_error').show();
        valid = false ;
    }else{
        form.find('#first_name_error').hide();
    }

    if(form.find('#id_father_name').val() == ""){
        form.find('#father_name_error').show();
        valid = false ;
    }else{
        form.find('#father_name_error').hide();
    }

    if(form.find('#id_last_name').val() == ""){
        form.find('#last_name_error').show();
        valid = false ;
    }else{
        form.find('#last_name_error').hide();
    }

    if(form.find('#id_mother_fullname').val() == ""){
        form.find('#mother_fullname_error').show();
        valid = false ;
    }else{
        form.find('#mother_fullname_error').hide();
    }

    if(form.find('#id_age').val() == ""){
        form.find('#age_error').show();
        valid = false ;
    }else{
        form.find('#age_error').hide();
    }

    if(form.find('#id_sex').val() == ""){
        form.find('#gender_error').show();
        valid = false ;
    }else{
        form.find('#gender_error').hide();
    }

    if(form.find('#id_relation_to_adult').val() == ""){
        form.find('#relation_to_adult_error').show();
        valid = false ;
    }else{
        form.find('#relation_to_adult_error').hide();
    }

    return valid;
 }

 function validate_add_child_withid()
{
    var valid = true ;
    var form = $('.bootbox-body').find('#add_child_withid_form');

    if(form.find('#id_relation_to_adult').val() == ""){
        form.find('#relation_to_household_reprentative_error').show();
        valid = false ;
    }else{
        form.find('#relation_to_household_reprentative_error').hide();
    }
     return valid;
}

function ValidateTextBoxMaximumSize(validationResult, message, id, size)
{
    return ValidateField
    (
            validationResult,
            message,
            id,
            function(id)
            {
                return $('#'+id).val().length <= size
            }
    );

    return validationResult;
}

function ValidateTextBoxRequired(validationResult, message, id)
{
    return ValidateField
    (
            validationResult,
            message,
            id,
            function(id)
            {
                return $('#'+id).val()!=""
            }
    );

    return validationResult;
}

function ValidateField(validationResult, message, id, isValidFunction)
{
    var isFieldValid = isValidFunction(id);

    if(!isFieldValid)
    {
        validationResult.ValidationMessage += message+"<br/>";
    }

    validationResult.IsValid = validationResult.IsValid && isFieldValid;

    return validationResult;
}

function checkArabicOnly(field)
{
    var sNewVal = "";

    var sFieldVal = field.val();

    for(var i = 0; i < sFieldVal.length; i++) {

        var ch = sFieldVal.charAt(i);

        var c = ch.charCodeAt(0);

        if((c < 1536 || c > 1791) && ch != " ") {
            // Discard
        }

        else {
            sNewVal += ch;
        }
    }

    if(field.val() != sNewVal) {
        field.val(sNewVal);
    }
}