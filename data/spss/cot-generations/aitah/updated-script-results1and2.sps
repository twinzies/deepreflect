* Encoding: UTF-8.
* --- Define Rogers and Goffman variable lists --- .
DEFINE !ROGERS ()
  Unconditional_Positive_Regard_Rogers
  Genuineness_Rogers
!ENDDEFINE.

DEFINE !GOFFMAN ()
  Emotional_Validation_Goffman
  Indirect_Language_Goffman
!ENDDEFINE.

* --- Macro to loop through all pairwise comparisons with response_source layer --- .
DEFINE !PAIRWISE ()
!DO !r !IN (!ROGERS)
  !DO !g !IN (!GOFFMAN)
    CROSSTABS
      /TABLES=!r BY !g BY response_source
      /FORMAT=AVALUE TABLES
      /STATISTICS=CHISQ PHI
      /CELLS=COUNT EXPECTED ROW COLUMN.
  !DOEND
!DOEND
!ENDDEFINE.

* --- Run the macro --- .
!PAIRWISE.

