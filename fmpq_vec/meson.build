
src_fmpq_vec = ['dot.c', 'fprint.c', 'init.c', 'randtest.c', 'randtest_uniq_sorted.c', 'set_fmpz_vec.c', 'sort.c']

src_fmpq_vec += generated_headers

headers_fmpq_vec = files([])

headers += headers_fmpq_vec

fmpq_vec = static_library(
  'fmpq_vec',
  src_fmpq_vec,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
