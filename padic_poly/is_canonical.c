/*============================================================================

    This file is part of FLINT.

    FLINT is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    FLINT is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with FLINT; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

=============================================================================*/
/******************************************************************************

    Copyright (C) 2012 Sebastian Pancratz
 
******************************************************************************/

#include "padic_poly.h"

int _padic_poly_is_canonical(const fmpz *op, long val, long len, 
                             const padic_ctx_t ctx)
{
    if (len == 0)
    {
        return (val == 0);
    }
    else
    {
        long w = _fmpz_vec_ord_p(op, len, ctx->p);

        return (w == 0);
    }
}

int padic_poly_is_canonical(const padic_poly_t op, const padic_ctx_t ctx)
{
    return _padic_poly_is_canonical(op->coeffs, op->val, op->length, ctx);
}

