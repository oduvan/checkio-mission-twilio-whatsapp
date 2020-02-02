//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'send_message',
            }
        });
        io.parseOutputArguments = function(val) {
            return "Message from " + val.from_ + " to " + val.to +": \"" + val.body + '"';
        }
        io.start();
    }
);
