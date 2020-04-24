
src_nmod_vec = ['add.c', 'discrete_log_pohlig_hellman.c', 'dot.c', 'dot_bound_limbs.c', 'dot_ptr.c', 'inlines.c', 'max_bits.c', 'neg.c', 'randtest.c', 'reduce.c', 'scalar_addmul_nmod.c', 'scalar_mul_nmod.c', 'scalar_mul_nmod_shoup.c', 'sub.c']

src_nmod_vec += generated_headers

headers_nmod_vec = files([])

headers += headers_nmod_vec

nmod_vec = static_library(
  'nmod_vec',
  src_nmod_vec,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
