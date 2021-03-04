from localidad import Localidad
import vocabulario as voc

vestibulo = Localidad('VESTÍBULO', 'Estás en el vestíbulo del castillo.')
pasillo = Localidad('PASILLO', 'Te encuentras en el pasillo...')
cocina = Localidad('COCINA', 'Estás en la cocina...')
biblioteca = Localidad('BIBLIOTECA', 'La biblioteca del castillo...')

vestibulo.set_conexiones({
    voc.NORTE: pasillo
})

pasillo.set_conexiones({
    voc.SUR: vestibulo,
    voc.ESTE: biblioteca,
    voc.OESTE: cocina
})

cocina.set_conexiones({
    voc.ESTE: pasillo
})

biblioteca.set_conexiones({
    voc.OESTE: pasillo
})
