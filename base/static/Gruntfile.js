module.exports = function(grunt) {
	
	// config
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		less: {
			dist: {
				options: {
					cleancss: true
				},
				files: {
					'dist/style.css': 'src/style.less'
				}
			}
		},
		jshint: {
			files: ['src/script.js']
		},
		uglify: {
			dist: {
				files: {
					'dist/script.js': ['src/script.js']
				}
			}
		},
		watch: {
			css: {
				files: ['src/style.less'],
				tasks: ['less']
			},
			js: {
				files: ['src/script.js'],
				tasks: ['jshint', 'uglify']
			}
		}
	});
	
	// load plugins
	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-contrib-less');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-watch');
	
	// default tasks
	grunt.registerTask('default', ['less', 'jshint', 'uglify']);
	
}
