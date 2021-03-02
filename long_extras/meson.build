
src_long_extras = files(['inlines.c', 'kronecker.c', 'randint.c', 'randtest.c', 'sizeinbase.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_long_extras
else
  src_long_extras += generated_headers
  long_extras = static_library(
    'long_extras',
    src_long_extras,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += long_extras
endif
