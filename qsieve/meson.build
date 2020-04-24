
src_qsieve = ['block_lanczos.c', 'clear.c', 'collect_relations.c', 'compute_poly_data.c', 'factor.c', 'init.c', 'knuth_schroeppel.c', 'large_prime_variant.c', 'linalg_clear.c', 'linalg_init.c', 'poly_clear.c', 'poly_init.c', 'primes_init.c', 'square_root.c']

src_qsieve += generated_headers

headers_qsieve = files([])

headers += headers_qsieve

qsieve = static_library(
  'qsieve',
  src_qsieve,
  include_directories : include_dir,
  override_options : [override_warning_level],
  install : false)
