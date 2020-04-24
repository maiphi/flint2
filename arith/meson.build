
src_arith = ['bell_number.c', 'bell_number_bsplit.c', 'bell_number_multi_mod.c', 'bell_number_nmod.c', 'bell_number_nmod_vec.c', 'bell_number_nmod_vec_recursive.c', 'bell_number_nmod_vec_series.c', 'bell_number_size.c', 'bell_number_vec.c', 'bell_number_vec_multi_mod.c', 'bell_number_vec_recursive.c', 'bernoulli_number.c', 'bernoulli_number_denom.c', 'bernoulli_number_size.c', 'bernoulli_number_vec.c', 'bernoulli_number_vec_multi_mod.c', 'bernoulli_number_vec_recursive.c', 'bernoulli_number_vec_zeta.c', 'bernoulli_number_zeta.c', 'bernoulli_polynomial.c', 'cyclotomic_cos_polynomial.c', 'dedekind_cosine_sum_factored.c', 'divisors.c', 'euler_number.c', 'euler_number_size.c', 'euler_number_vec.c', 'euler_number_zeta.c', 'euler_polynomial.c', 'harmonic_number.c', 'inlines.c', 'landau_function_vec.c', 'number_of_partitions.c', 'number_of_partitions_mpfr.c', 'number_of_partitions_nmod_vec.c', 'number_of_partitions_vec.c', 'ramanujan_tau.c', 'stirling1.c', 'stirling2.c', 'stirlingmat.c', 'sum_of_squares.c', 'sum_of_squares_vec.c', 'zeta_inv_euler_product.c']

src_arith += generated_headers

headers_arith = files([])

headers += headers_arith

arith = static_library(
  'arith',
  src_arith,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
