module.exports = function(grunt) {

    grunt.initConfig({
        less: {
            development: {
                options: {
                    paths: ['static/less']
                },
                files: {
                    'static/css/main.css': 'static/less/main.less',
                    'static/css/navbar.css': 'static/less/navbar.less',
                    'static/css/home.css': 'static/less/home.less',
                }
            }
        },

        watch: {
            styles: {
                files: ['static/less/**/*.less'],
                tasks: ['less']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['less', 'watch']);

};
