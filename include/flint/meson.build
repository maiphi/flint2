
# Copy all header files to include/flint/, so that they can be included
# as <flint/header.h> before installation when FLINT is built as a subproject.

header_copies = []

foreach h : headers
  header_copies += configure_file(
    input : h,
    output : '@PLAINNAME@',
    copy : true)
endforeach

install_headers(header_copies, subdir : 'flint')
