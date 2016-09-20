var uploadUrl = '/upload_files/'
var uploadedFilesCount = 0
var totalFilesCount = 0
var $progressIndicator = $('.progressIndicator')

function updateProgressIndicator()
{
    if (totalFilesCount <= 0)
    {
        $progressIndicator.width('100%')
    }
    else
    {
        $progressIndicator.width(
            (100 * uploadedFilesCount / totalFilesCount) + '%')
    }
}

function initDropzone()
{
    $.widget('blueimp.fileupload', $.blueimp.fileupload, {})
    $('.dropzone').fileupload({
        url: uploadUrl,
        sequentialUploads: true,
        dropZone: $('.dropzone'),
        drop: function(e, data){
            uploadedFilesCount = 0
            totalFilesCount = data.files.length
        },
        done: function() {
            uploadedFilesCount += 1
            updateProgressIndicator()
        }
    })
}

initDropzone()
