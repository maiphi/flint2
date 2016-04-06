/*=============================================================================

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

    Copyright (C) 2011 Fredrik Johansson
    Copyright (C) 2013 Mike Hansen

******************************************************************************/


#ifdef T

#include "templates.h"

#include <stdio.h>

int
main(void)
{
    slong i;
    FLINT_TEST_INIT(state);

    printf("mul....");
    fflush(stdout);

    /* Check aliasing C and A */
    for (i = 0; i < 10 * flint_test_multiplier(); i++)
    {
        TEMPLATE(T, ctx_t) ctx;
        TEMPLATE(T, mat_t) A, B, C;
        slong m, n;

        TEMPLATE(T, ctx_randtest) (ctx, state);

        m = n_randint(state, 20);
        n = n_randint(state, 20);

        TEMPLATE(T, mat_init) (A, m, n, ctx);
        TEMPLATE(T, mat_init) (B, n, n, ctx);
        TEMPLATE(T, mat_init) (C, m, n, ctx);

        TEMPLATE(T, mat_randtest) (A, state, ctx);
        TEMPLATE(T, mat_randtest) (B, state, ctx);
        TEMPLATE(T, mat_randtest) (C, state, ctx);  /* noise in output */

        TEMPLATE(T, mat_mul) (C, A, B, ctx);
        TEMPLATE(T, mat_mul) (A, A, B, ctx);

        if (!TEMPLATE(T, mat_equal) (C, A, ctx))
        {
            printf("FAIL:\n");
            printf("A:\n");
            TEMPLATE(T, mat_print) (A, ctx);
            printf("B:\n");
            TEMPLATE(T, mat_print) (B, ctx);
            printf("C:\n");
            TEMPLATE(T, mat_print) (C, ctx);
            printf("\n");
            abort();
        }

        TEMPLATE(T, mat_clear) (A, ctx);
        TEMPLATE(T, mat_clear) (B, ctx);
        TEMPLATE(T, mat_clear) (C, ctx);

        TEMPLATE(T, ctx_clear) (ctx);
    }

    /* Check aliasing C and B */
    for (i = 0; i < 10 * flint_test_multiplier(); i++)
    {
        TEMPLATE(T, ctx_t) ctx;
        TEMPLATE(T, mat_t) A, B, C;
        slong m, n;

        TEMPLATE(T, ctx_randtest) (ctx, state);

        m = n_randint(state, 20);
        n = n_randint(state, 20);

        TEMPLATE(T, mat_init) (A, m, m, ctx);
        TEMPLATE(T, mat_init) (B, m, n, ctx);
        TEMPLATE(T, mat_init) (C, m, n, ctx);

        TEMPLATE(T, mat_randtest) (A, state, ctx);
        TEMPLATE(T, mat_randtest) (B, state, ctx);
        TEMPLATE(T, mat_randtest) (C, state, ctx);  /* noise in output */

        TEMPLATE(T, mat_mul) (C, A, B, ctx);
        TEMPLATE(T, mat_mul) (B, A, B, ctx);

        if (!TEMPLATE(T, mat_equal) (C, B, ctx))
        {
            printf("FAIL:\n");
            printf("A:\n");
            TEMPLATE(T, mat_print) (A, ctx);
            printf("B:\n");
            TEMPLATE(T, mat_print) (B, ctx);
            printf("C:\n");
            TEMPLATE(T, mat_print) (C, ctx);
            printf("\n");
            abort();
        }

        TEMPLATE(T, mat_clear) (A, ctx);
        TEMPLATE(T, mat_clear) (B, ctx);
        TEMPLATE(T, mat_clear) (C, ctx);

        TEMPLATE(T, ctx_clear) (ctx);
    }

    FLINT_TEST_CLEANUP(state);
    printf("PASS\n");
    return 0;
}


#endif
