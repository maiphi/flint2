
# Copy all header files to include/flint/, so that they can be included
# as <flint/header.h> before installation when FLINT is built as a subproject.

header_copies = []

if meson.version().version_compare('>=0.47.0')
  foreach h : headers
    header_copies += configure_file(
      input : h,
      output : '@PLAINNAME@',
      copy : true)
  endforeach
else
  foreach h : headers
    empty_conf = configuration_data()
    header_copies += configure_file(
      input : h,
      output : '@PLAINNAME@',
      configuration : empty_conf)
  endforeach
endif

install_headers(header_copies, subdir : 'flint')
