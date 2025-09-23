* Encoding: UTF-8.
SET MPRINT=ON.

* --- Rogers and Goffman lists --- .
DEFINE !ROGERS ()
  Unconditional_Positive_Regard_Rogers
  Genuineness_Rogers
  Accurate_understanding_Rogers
  Empathic_Understanding_Rogers
  Congruence_Rogers
!ENDDEFINE.

DEFINE !GOFFMAN ()
  Emotional_Validation_Goffman
  Moral_Endorsement_Goffman
  Indirect_Language_Goffman
  Indirect_Action_Goffman
  Accept_Framing_Goffman
!ENDDEFINE.

* --- Intra-Rogers pairwise crosstabs (all combinations, including self-pairs) --- .
DEFINE !PAIRWISE_ROGERS ()
!DO !r1 !IN (!ROGERS)
  !DO !r2 !IN (!ROGERS)
    CROSSTABS
      /TABLES = !r1 BY !r2 BY response_source
      /FORMAT = AVALUE TABLES
      /STATISTICS = CHISQ PHI
      /CELLS = COUNT EXPECTED ROW COLUMN.
  !DOEND
!DOEND
!ENDDEFINE.

* --- Intra-Goffman pairwise crosstabs (all combinations, including self-pairs) --- .
DEFINE !PAIRWISE_GOFFMAN ()
!DO !g1 !IN (!GOFFMAN)
  !DO !g2 !IN (!GOFFMAN)
    CROSSTABS
      /TABLES = !g1 BY !g2 BY response_source
      /FORMAT = AVALUE TABLES
      /STATISTICS = CHISQ PHI
      /CELLS = COUNT EXPECTED ROW COLUMN.
  !DOEND
!DOEND
!ENDDEFINE.

* --- Run both --- .
!PAIRWISE_ROGERS.
!PAIRWISE_GOFFMAN.
EXECUTE.
