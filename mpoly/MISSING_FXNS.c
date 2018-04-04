/*
    Copyright (C) 2018 Daniel Schultz

    This file is part of FLINT.

    FLINT is free software: you can redistribute it and/or modify it under
    the terms of the GNU Lesser General Public License (LGPL) as published
    by the Free Software Foundation; either version 2.1 of the License, or
    (at your option) any later version.  See <http://www.gnu.org/licenses/>.
*/

#include "mpoly.h"


/*
    Assuming that "in" is non negative and has a limb count <= out_len,
    write the limbs to "out" and zero extend to "out_len" limbs.
*/

void fmpz_get_ui_array(ulong * out, slong out_len, const fmpz_t in)
{
    slong size = 0;
    FLINT_ASSERT(out_len > 0);

    /* copy limbs */
    if (fmpz_abs_fits_ui(in))
    {
        *out++ = fmpz_get_ui(in);
        size++;
    } else
    {
        __mpz_struct * mpz = COEFF_TO_PTR(*in);
        FLINT_ASSERT(mpz->_mp_size <= out_len);
        while (size < mpz->_mp_size)
            *out++ = mpz->_mp_d[size++];
    }

    /* zero extend to out_len */
    while (size++ < out_len)
        *out++ = UWORD(0);
}


/*
    Given an array of limbs "in" representing a non negative integer,
    set "out" to this integer.
*/

void fmpz_set_ui_array(fmpz_t out, const ulong * in, slong in_len)
{
    slong size = in_len;
    FLINT_ASSERT(in_len > 0);

    /* find end of zero extension */
    while (size > WORD(1) && in[size - 1] == UWORD(0))
        size--;

    /* copy limbs */
    if (size == WORD(1))
    {
        fmpz_set_ui(out, in[0]);
    } else
    {
        __mpz_struct * mpz = _fmpz_promote(out);
        mpz_realloc2(mpz, FLINT_BITS*size);
        mpz->_mp_size = size;
        do {
            size--;
            mpz->_mp_d[size] = in[size];
        } while (size > 0);
    }
}


/*
    set sumabs = bit_count(sum of absolute values of coefficients);
    set maxabs = bit_count(max of absolute values of coefficients);
*/
void _fmpz_vec_sum_max_bits(slong * sumabs, slong * maxabs,
                                             const fmpz * coeffs, slong length)
{
    slong j;
    ulong hi = 0, lo = 0;

    maxabs[0] = 0;

    for (j = 0; j < length && fmpz_fits_si(coeffs + j); j++)
    {
        slong c = fmpz_get_si(coeffs + j);
        ulong uc = (ulong) FLINT_ABS(c);
        add_ssaaaa(hi, lo, hi, lo, UWORD(0), uc);
        maxabs[0] = FLINT_MAX(maxabs[0], FLINT_BIT_COUNT(uc));
    }

    if (j == length)
    {
        /* no large coeffs encountered */
        if (hi != 0)
            sumabs[0] = FLINT_BIT_COUNT(hi) + FLINT_BITS;
        else
            sumabs[0] = FLINT_BIT_COUNT(lo);
    } else
    {
        /* restart with multiprecision routine */
        fmpz_t sum;
        fmpz_init(sum);

        for (j = 0; j < length; j++)
        {
            maxabs[0] = FLINT_MAX(maxabs[0], fmpz_sizeinbase(coeffs + j, 2));

            if (fmpz_sgn(coeffs + j) < 0)
                fmpz_sub(sum, sum, coeffs + j);
            else
                fmpz_add(sum, sum, coeffs + j);
        }

        sumabs[0] = fmpz_sizeinbase(sum, 2);
        fmpz_clear(sum);
   }
}


/* vec1 = pointwise max of vec1 and vec2 */
void _fmpz_vec_max_inplace(fmpz * vec1, const fmpz * vec2, slong len)
{
    slong i;
    for (i = 0; i < len; i++)
    {
        if (fmpz_cmp(vec1 + i, vec2 + i) < 0)
            fmpz_set(vec1 + i, vec2 + i);
    }
}


/* vec1 = pointwise max of vec2 and vec3 */
void _fmpz_vec_max(fmpz * vec1, const fmpz * vec2, const fmpz * vec3, slong len)
{
    slong i;
    for (i = 0; i < len; i++)
    {
        int cmp = fmpz_cmp(vec2 + i, vec3 + i);
        fmpz_set(vec1 + i, (cmp > 0 ? vec2 : vec3) + i);
    }
}
