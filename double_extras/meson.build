
src_double_extras = files(['inlines.c', 'is_nan.c', 'lambertw.c', 'log2.c', 'randtest.c', 'randtest_signed.c', 'randtest_special.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_double_extras
else
  src_double_extras += generated_headers
  double_extras = static_library(
    'double_extras',
    src_double_extras,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += double_extras
endif
