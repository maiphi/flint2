
src_fmpq_vec = files(['dot.c', 'fprint.c', 'init.c', 'randtest.c', 'randtest_uniq_sorted.c', 'set_fmpz_vec.c', 'sort.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpq_vec
else
  src_fmpq_vec += generated_headers
  fmpq_vec = static_library(
    'fmpq_vec',
    src_fmpq_vec,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpq_vec
endif
