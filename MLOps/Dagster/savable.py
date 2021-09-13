from sklearn.svm import SVC, LinearSVC

class SavableSVC(SVC, Savable):
    @classmethod
    def from_super(cls, superinstance):
        mutation_warning()
        if superinstance.kernel=='linear':
            instance = cls(kernel='linear')
        else:
            instance = cls()

        instance.C = superinstance.C
        instance._dual_coef_ = superinstance._dual_coef_
        _gamma = superinstance._gamma
        _impl = superinstance._impl
        intercept_ = superinstance._intercept_
        _sparse = superinstance._sparse
        cache_size = superinstance.cache_size