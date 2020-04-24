
src_fmpz_vec = ['add.c', 'clear.c', 'content.c', 'dot.c', 'dot_ptr.c', 'equal.c', 'fprint.c', 'fread.c', 'get_d_vec_2exp.c', 'get_fft.c', 'get_mpf_vec.c', 'get_nmod_vec.c', 'height.c', 'height_index.c', 'init.c', 'inlines.c', 'is_zero.c', 'lcm.c', 'max.c', 'max_bits.c', 'max_bits_ref.c', 'max_limbs.c', 'min.c', 'neg.c', 'prod.c', 'randtest.c', 'scalar_abs.c', 'scalar_addmul_fmpz.c', 'scalar_addmul_si.c', 'scalar_addmul_si_2exp.c', 'scalar_divexact_fmpz.c', 'scalar_divexact_si.c', 'scalar_divexact_ui.c', 'scalar_fdiv_q_2exp.c', 'scalar_fdiv_q_fmpz.c', 'scalar_fdiv_q_si.c', 'scalar_fdiv_q_ui.c', 'scalar_fdiv_r_2exp.c', 'scalar_mod_fmpz.c', 'scalar_mul_2exp.c', 'scalar_mul_fmpz.c', 'scalar_mul_si.c', 'scalar_mul_ui.c', 'scalar_smod_fmpz.c', 'scalar_submul_fmpz.c', 'scalar_submul_si.c', 'scalar_submul_si_2exp.c', 'scalar_tdiv_q_2exp.c', 'scalar_tdiv_q_fmpz.c', 'scalar_tdiv_q_si.c', 'scalar_tdiv_q_ui.c', 'set.c', 'set_fft.c', 'set_nmod_vec.c', 'sort.c', 'sub.c', 'sum.c', 'sum_max_bits.c', 'swap.c', 'zero.c']

src_fmpz_vec += generated_headers

headers_fmpz_vec = files([])

headers += headers_fmpz_vec

fmpz_vec = static_library(
  'fmpz_vec',
  src_fmpz_vec,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
