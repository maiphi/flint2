
src_fft = ['adjust.c', 'adjust_sqrt2.c', 'butterfly_lshB.c', 'butterfly_rshB.c', 'combine_bits.c', 'convolution.c', 'convolution_precache.c', 'div_2expmod_2expp1.c', 'fermat_to_mpz.c', 'fft_mfa_truncate_sqrt2.c', 'fft_mfa_truncate_sqrt2_inner.c', 'fft_negacylic.c', 'fft_radix2.c', 'fft_truncate.c', 'fft_truncate_sqrt2.c', 'ifft_mfa_truncate_sqrt2.c', 'ifft_negacyclic.c', 'ifft_radix2.c', 'ifft_truncate.c', 'ifft_truncate_sqrt2.c', 'inlines.c', 'mul_2expmod_2expp1.c', 'mul_fft_main.c', 'mul_mfa_truncate_sqrt2.c', 'mul_truncate_sqrt2.c', 'mulmod_2expp1.c', 'normmod_2expp1.c', 'split_bits.c']

src_fft += generated_headers

headers_fft = files([])

headers += headers_fft

fft = static_library(
  'fft',
  src_fft,
  include_directories : include_dir,
  override_options : ['warning_level=0'],
  install : false)
