## File name usages in: (change the text in these if you rename this file)
##                      AcousticT0.py



help_str = '''
Use this as a template for deciding which "fit_type" to use when creating the correlation signal within AcousticT0.py.
* Default is Type 0

Fit Type 0 -- Exponential decay starting at 0

      1 *+------------+------------+-------------+------------+------------++
        +*            +            +             +           exp(-x) ****** +
    0.9 +*                                                                 ++
        | *                                                                 |
    0.8 ++ *                                                               ++
        |   *                                                               |
    0.7 ++   *                                                             ++
        |    **                                                             |
    0.6 ++     *                                                           ++
        |       *                                                           |
    0.5 ++       **                                                        ++
        |         **                                                        |
    0.4 ++          **                                                     ++
        |             **                                                    |
    0.3 ++              **                                                 ++
        |                 ***                                               |
    0.2 ++                   ***                                           ++
        |                       *****                                       |
    0.1 ++                           *******                               ++
        +             +            +        ***************   +             +
      0 ++------------+------------+-------------+---------******************
        0             1            2             3            4             5


Fit Type 1 -- Step function followed by an exponential decay. "shift" can be supplied to say how many datapoints
          you want in the step function. Default shift is 5

    1.2 ++------------+------------+-------------+------------+------------++
        +             +            +             +            + t(x) ****** +
        |                                                                   |
      1 **************                                                     ++
        |             *                                                     |
        |              *                                                    |
        |               *                                                   |
    0.8 ++              **                                                 ++
        |                 **                                                |
        |                  *                                                |
    0.6 ++                  **                                             ++
        |                    ***                                            |
        |                      **                                           |
    0.4 ++                       **                                        ++
        |                          **                                       |
        |                            ***                                    |
        |                               ***                                 |
    0.2 ++                                 *****                           ++
        |                                       *******                     |
        +             +            +             +     ***************      +
      0 ++------------+------------+-------------+------------+-------*******
        0             1            2             3            4

Fit Type 2 -- Similar to Type 1 in how shift works, but instead of being constantly 1 we have a linear increase

    1.2 ++------------+------------+-------------+------------+------------++
        +             +            +             +            + t(x) ****** +
        |                                                                   |
      1 ++                                                                 ++
        |            **                                                     |
        |           *  *                                                    |
        |           *   *                                                   |
    0.8 ++        **    **                                                 ++
        |         *       **                                                |
        |        *         *                                                |
    0.6 ++      *           **                                             ++
        |       *            ***                                            |
        |     **               **                                           |
    0.4 ++   *                   **                                        ++
        |    *                     **                                       |
        |   *                        ***                                    |
        |  *                            ***                                 |
    0.2 ++**                               *****                           ++
        |*                                      *******                     |
        +*            +            +             +     ***************      +
      0 *+------------+------------+-------------+------------+-------*******
        0             1            2             3            4             5

Fit Type 3 -- Similar to Type 1 in how shift works, but has a logorithmically increasing function instead of being constant


    1.2 ++---------+-----------+----------+----------+-----------+---------++
        +          +           +          +          +          t(x) ****** +
        |                                                                   |
      1 ++                                     *                           ++
        |                                  **** *                           |
        |                              ****      *                          |
        |                          ****           *                         |
    0.8 ++                      ****               *                       ++
        |                    ***                   *                        |
        |                  ***                      **                      |
    0.6 ++              ***                          **                    ++
        |             **                               *                    |
        |          ***                                 **                   |
    0.4 ++        *                                      **                ++
        |       **                                         **               |
        |     **                                             **             |
        |    *                                                 ***          |
    0.2 ++ **                                                     ****     ++
        | **                                                          ******|
        +*         +           +          +          +           +         **
      0 *+---------+-----------+----------+----------+-----------+---------++
        0          1           2          3          4           5          6


Fit Type 4 -- Similar to type 1 in how shift works, but has an exponentially increasing function instead of being constant


    1.2 ++------------+------------+-------------+------------+------------++
        +             +            +             +            + t(x) ****** +
        |                                                                   |
      1 ++                                                                 ++
        |             *                                                     |
        |             **                                                    |
        |             * *                                                   |
    0.8 ++            * **                                                 ++
        |             *   **                                                |
        |             *    *                                                |
    0.6 ++            *     **                                             ++
        |             *      ***                                            |
        |             *        **                                           |
    0.4 ++           *           **                                        ++
        |            *             **                                       |
        |            *               ***                                    |
        |            *                  ***                                 |
    0.2 ++           *                     *****                           ++
        |            *                          *******                     |
        +            *+            +             +     ***************      +
      0 **************+------------+-------------+------------+-------*******
        0             1            2             3            4             5
'''