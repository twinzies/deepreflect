* Encoding: UTF-8.
* --- Define Rogers and Goffman variable lists --- .
DEFINE !ROGERS ()
  Unconditional_Positive_Regard_Rogers
  Genuineness_Rogers
  Accurate_understanding_Rogers
!ENDDEFINE.

DEFINE !GOFFMAN ()
  Emotional_Validation_Goffman
  Moral_Endorsement_Goffman
  Indirect_Language_Goffman
  Indirect_Action_Goffman
  Accept_Framing_Goffman
!ENDDEFINE.

* --- Macro to loop through all pairwise comparisons with response_source layer --- .
DEFINE !PAIRWISE ()
!DO !r !IN (!ROGERS)
  !DO !g !IN (!GOFFMAN)
    CROSSTABS
      /TABLES=!r BY !g BY response_source
      /FORMAT=AVALUE TABLES
      /STATISTICS=PHI
  !DOEND
!DOEND
!ENDDEFINE.

* --- Run the macro --- .
!PAIRWISE.

