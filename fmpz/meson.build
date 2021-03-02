
src_fmpz = files(['is_perfect_power.c', 'CRT.c', 'CRT_ui.c', 'abs.c', 'abs_fits_ui.c', 'abs_lbound_ui_2exp.c', 'abs_ubound_ui_2exp.c', 'add.c', 'add_ui.c', 'addmul.c', 'addmul_si.c', 'addmul_ui.c', 'and.c', 'bin_uiui.c', 'bit_pack.c', 'bit_unpack.c', 'bits.c', 'cdiv_q.c', 'cdiv_q_2exp.c', 'cdiv_q_si.c', 'cdiv_q_ui.c', 'cdiv_qr.c', 'cdiv_r_2exp.c', 'cdiv_ui.c', 'clear_readonly.c', 'clog.c', 'clog_ui.c', 'clrbit.c', 'cmp.c', 'cmp_si.c', 'cmp_ui.c', 'cmpabs.c', 'comb_clear.c', 'comb_init.c', 'combit.c', 'complement.c', 'divexact.c', 'divexact_si.c', 'divexact_ui.c', 'divides_mod_list.c', 'divisible.c', 'divisible_si.c', 'divisor_in_residue_class_lenstra.c', 'divisor_sigma.c', 'dlog.c', 'equal.c', 'equal_si.c', 'equal_ui.c', 'euler_phi.c', 'fac_ui.c', 'fdiv_q.c', 'fdiv_q_2exp.c', 'fdiv_q_si.c', 'fdiv_q_ui.c', 'fdiv_qr.c', 'fdiv_qr_preinvn.c', 'fdiv_r.c', 'fdiv_r_2exp.c', 'fdiv_ui.c', 'fib_ui.c', 'fits_si.c', 'flog.c', 'flog_ui.c', 'fmma.c', 'fmms.c', 'fprint.c', 'fread.c', 'gcd.c', 'gcdinv.c', 'get_d.c', 'get_d_2exp.c', 'get_mpf.c', 'get_mpfr.c', 'get_mpn.c', 'get_mpz.c', 'get_si.c', 'get_str.c', 'get_ui.c', 'get_ui_array.c', 'init2.c', 'init_set_readonly.c', 'inlines.c', 'inp_raw.c', 'invmod.c', 'is_prime.c', 'is_prime_morrison.c', 'is_prime_pocklington.c', 'is_prime_pseudosquare.c', 'is_probabprime.c', 'is_probabprime_BPSW.c', 'is_probabprime_lucas.c', 'is_square.c', 'is_strong_probabprime.c', 'jacobi.c', 'kronecker.c', 'lcm.c', 'lucas_chain.c', 'mod.c', 'mod_ui.c', 'moebius_mu.c', 'mpz_clear_readonly.c', 'mpz_init_set_readonly.c', 'mul.c', 'mul_2exp.c', 'mul_si.c', 'mul_si_tdiv_q_2exp.c', 'mul_tdiv_q_2exp.c', 'mul_ui.c', 'multi_CRT_ui.c', 'multi_crt.c', 'multi_mod_ui.c', 'nextprime.c', 'or.c', 'out_raw.c', 'popcnt.c', 'pow_fmpz.c', 'pow_ui.c', 'powm.c', 'powm_ui.c', 'powmod2_fmpz_preinv.c', 'preinvn_clear.c', 'preinvn_init.c', 'primorial.c', 'print.c', 'randbits.c', 'randm.c', 'randprime.c', 'randtest.c', 'randtest_mod.c', 'read.c', 'remove.c', 'rfac_ui.c', 'rfac_uiui.c', 'root.c', 'set.c', 'set_d.c', 'set_d_2exp.c', 'set_mpf.c', 'set_mpz.c', 'set_signed_ui_array.c', 'set_signed_uiui.c', 'set_signed_uiuiui.c', 'set_str.c', 'set_ui_array.c', 'setbit.c', 'sgn.c', 'size.c', 'sizeinbase.c', 'smod.c', 'sqrt.c', 'sqrtmod.c', 'sqrtrem.c', 'sub.c', 'sub_ui.c', 'submul.c', 'submul_si.c', 'submul_ui.c', 'tdiv_q.c', 'tdiv_q_2exp.c', 'tdiv_q_si.c', 'tdiv_q_ui.c', 'tdiv_qr.c', 'tdiv_r_2exp.c', 'tdiv_ui.c', 'tstbit.c', 'val2.c', 'xgcd.c', 'xgcd_partial.c', 'xor.c'])

headers += files([])

if meson.version().version_compare('>=0.55.0')
  src += src_fmpz
else
  src_fmpz += generated_headers
  fmpz = static_library(
    'fmpz',
    src_fmpz,
    include_directories : include_dir,
    override_options : [override_warning_level],
    install : false)
  subdir_static_libs += fmpz
endif
