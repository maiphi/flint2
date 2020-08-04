
src_perm = files(['inlines.c', 'parity.c', 'randtest.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_perm
else
  src_perm += generated_headers
  perm = static_library(
    'perm',
    src_perm,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += perm
endif
