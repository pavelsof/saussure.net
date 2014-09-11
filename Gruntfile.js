module.exports = function(grunt) {
	
	// config
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		concat: {
			vendor: {
				files: {
					'static/vendor/style.css': [
						'bower_components/bootstrap/dist/css/bootstrap.min.css'
					],
					'static/vendor/script.js': [
						'bower_components/jquery/dist/jquery.min.js',
						'bower_components/bootstrap/dist/js/bootstrap.min.js'
					]
				}
			}
		},
		copy: {
			fonts: {
				expand: true,
				cwd: 'bower_components/bootstrap/dist',
				src: 'fonts/**',
				dest: 'static/'
			},
			images: {
				expand: true,
				cwd: 'base/static',
				src: 'images/**',
				dest: 'static/'
			}
		},
		less: {
			main: {
				options: {
					cleancss: true
				},
				files: {
					'static/style.css': 'base/static/styles/style.less'
				}
			}
		},
		jshint: {
			files: ['base/static/scripts/**/*.js']
		},
		uglify: {
			main: {
				files: {
					'static/script.js': ['base/static/scripts/script.js']
				}
			}
		},
		watch: {
			options: {
				livereload: true
			},
			images: {
				files: ['base/static/images/**'],
				tasks: ['copy:images']
			},
			css: {
				files: ['base/static/styles/**/*.less'],
				tasks: ['less']
			},
			js: {
				files: ['base/static/scripts/**/*.js'],
				tasks: ['jshint', 'uglify']
			}
		}
	});
	
	// load plugins
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-copy');
	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-contrib-less');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-watch');
	
	// default tasks
	grunt.registerTask('build', ['copy', 'less', 'concat', 'jshint', 'uglify']);
	grunt.registerTask('serve', ['build', 'watch']);
	grunt.registerTask('default', ['build']);
	
}
