import io
import json
import warnings
import numpy as np
from base64 import b64encode, b64decode
from scipy.sparse import save_npz, load_npz
from sklearn.svm import SVC, LinearSVC

def mutation_warning():
    msg = 'Mutating this instance will also mutate the original superinstance.'
    warnings.warn(msg, UserWarning, stacklevel=2)

def bstr2np(bstr):
    f = io.BytesIO(b64decode(bstr))
    return np.load(f, allow_pickle=False)

def sp2bstr(sparse_matrix):
    f = io.BytesIO()
    save_npz(f, sparse_matrix)
    return b64encode((f.getvalue())).decode("ascii") 

def bstr2sp(bstr):
    f = io.BytesIO(b64decode(bstr))
    return load_npz(f)

def np2bstr(arr):
    f = io.BytesIO()
    np.save(file=f, arr=arr, allow_pickle=False)
    return b64encode((f.getvalue())).decode("ascii")

def bstr2array(bstr, is_sparse):
    """
    Interface to save array (sparse or dense) to binary string
    """
    if is_sparse:
        return bstr2sp(bstr)
    if type(bstr) is list:
        FutureWarning("purely for regression purpose, will be deprecated")
        return np.array(bstr) # to be compatable with list array
    return bstr2np(bstr)

def array2bstr(arr, is_sparse):
    """
    Interface to save array (sparse or dense) to binary string
    """
    if is_sparse:
        return sp2bstr(arr)
    return np2bstr(arr)

class Savable():
    """
        the method that saves current object into a string instance, the method itself returns json seralisable dictionary.
    """
    def saves(self):
        return {"class": ".".join([self.__class__.__module__, self.__class__.__name__]), "params": self.serialise()}

    @classmethod
    def loads(cls, serialised):
        """
            the class method that load a serialised artefact. It leverages ``from_dict`` method of the chield classes to do the de-serialisation.

            :param serialised: dictionary contains ``class`` and ``params`` keys.
            :type serialised: dict
        """
        class_fullname = ".".join([cls.__module__, cls.__name__])
        if serialised["class"] != class_fullname:
            raise TypeError("Expecting calss {}, but got {}".format(class_fullname, serialised["class"]))
        return cls.deserialise(serialised["params"])

    def save(self, filepath):
        with open(filepath, "w") as f:
            savejson = self.saves()
            json.dump(savejson, f)

    def serialise(self, *args, **kwargs):
        if not hasattr(self, "to_dict"):
            raise AttributeError(f"class {type(self)} does not have the to_dict method, either define or override the method")
        return self.to_dict(*args, **kwargs)

    @classmethod
    def deserialise(cls, *args, **kwargs):
        if not hasattr(cls, "from_dict"):
            raise AttributeError(f"class {type(cls)} does not have the from_dict method, either define or override the method")
        return cls.from_dict(*args, **kwargs)


class SavableSVC(SVC, Savable):
    @classmethod
    def from_super(cls, superinstance):
        mutation_warning()
        if superinstance.kernel == "linear":
            instance = cls(kernel="linear")
        else:
            instance = cls()

        instance.C = superinstance.C
        instance._dual_coef_ = superinstance._dual_coef_
        instance._gamma = superinstance._gamma
        instance._impl = superinstance._impl
        instance._intercept_ = superinstance._intercept_
        instance._sparse = superinstance._sparse
        instance.cache_size = superinstance.cache_size
        instance.class_weight = superinstance.class_weight
        instance.class_weight_ = superinstance.class_weight_
        instance.classes_ = superinstance.classes_
        instance.coef0 = superinstance.coef0
        instance.decision_function_shape = superinstance.decision_function_shape
        instance.degree = superinstance.degree
        instance.dual_coef_ = superinstance.dual_coef_
        instance.epsilon = superinstance.epsilon
        instance.fit_status_ = superinstance.fit_status_
        instance.gamma = superinstance.gamma
        instance.intercept_ = superinstance.intercept_
        instance.kernel = superinstance.kernel
        instance.max_iter = superinstance.max_iter
        instance.n_support_ = superinstance.n_support_
        instance.nu = superinstance.nu
        instance.probA_ = superinstance.probA_
        instance.probB_ = superinstance.probB_
        instance.probability = superinstance.probability
        instance.random_state = superinstance.random_state
        instance.shape_fit_ = superinstance.shape_fit_
        instance.shrinking = superinstance.shrinking
        instance.support_ = superinstance.support_
        instance.support_vectors_ = superinstance.support_vectors_
        instance.tol = superinstance.tol
        instance.verbose = superinstance.verbose
        return instance

    def to_super(self):
        if self.kernel == "linear":
            superinstance = SVC(kernel="linear")
            # superinstance.coef_ = self.coef_
        else:
            superinstance = SVC()

        superinstance.C = self.C
        superinstance._dual_coef_ = self._dual_coef_
        superinstance._gamma = self._gamma
        superinstance._impl = self._impl
        superinstance._intercept_ = self._intercept_
        superinstance._sparse = self._sparse
        superinstance.cache_size = self.cache_size
        superinstance.class_weight = self.class_weight
        superinstance.class_weight_ = self.class_weight_
        superinstance.classes_ = self.classes_
        superinstance.coef0 = self.coef0
        superinstance.decision_function_shape = self.decision_function_shape
        superinstance.degree = self.degree
        superinstance.dual_coef_ = self.dual_coef_
        superinstance.epsilon = self.epsilon
        superinstance.fit_status_ = self.fit_status_
        superinstance.gamma = self.gamma
        superinstance.intercept_ = self.intercept_
        superinstance.kernel = self.kernel
        superinstance.max_iter = self.max_iter
        superinstance.n_support_ = self.n_support_
        superinstance.nu = self.nu
        superinstance.probA_ = self.probA_
        superinstance.probB_ = self.probB_
        superinstance.probability = self.probability
        superinstance.random_state = self.random_state
        superinstance.shape_fit_ = self.shape_fit_
        superinstance.shrinking = self.shrinking
        superinstance.support_ = self.support_
        superinstance.support_vectors_ = self.support_vectors_
        superinstance.tol = self.tol
        superinstance.verbose = self.verbose
        return superinstance

    @classmethod
    def from_dict(cls, dct):
        kernel = dct.get("kernel")
        instance = cls(kernel=kernel)

        instance._sparse = dct.get("_sparse")
        instance.C = dct.get("C")
        instance._dual_coef_ = bstr2array(dct.get("_dual_coef_"), is_sparse=instance._sparse)
        instance._intercept_ = np.array(dct.get("_intercept_"))
        instance.dual_coef_ = bstr2array(dct.get("dual_coef_"), is_sparse=instance._sparse)
        instance.support_vectors_ = bstr2array(dct.get("support_vectors_"), is_sparse=instance._sparse)
        instance._gamma = dct.get("_gamma")
        instance._impl = dct.get("_impl")
        instance.cache_size = dct.get("cache_size")
        instance.class_weight = dct.get("class_weight")
        instance.class_weight_ = np.array(dct.get("class_weight_"))
        instance.classes_ = np.array(dct.get("classes_"))
        instance.coef0 = dct.get("coef0")
        instance.decision_function_shape = dct.get("decision_function_shape")
        instance.degree = dct.get("degree")
        instance.epsilon = dct.get("epsilon")
        instance.fit_status_ = dct.get("fit_status_")
        instance.gamma = dct.get("gamma")
        instance.intercept_ = np.array(dct.get("intercept_"))
        instance.max_iter = dct.get("max_iter")
        instance.n_support_ = np.array(dct.get("n_support_"), dtype=np.int32)
        instance.nu = dct.get("nu")
        instance.probA_ = np.array(dct.get("probA_"))
        instance.probB_ = np.array(dct.get("probB_"))
        instance.probability = dct.get("probability")
        instance.random_state = dct.get("random_state")
        instance.shape_fit_ = dct.get("shape_fit_")
        instance.shrinking = dct.get("shrinking")
        instance.support_ = np.array(dct.get("support_"), dtype=np.int32)
        instance.tol = dct.get("tol")
        instance.verbose = dct.get("verbose")
        return instance

    def to_dict(self):
        dict_ = {
            'C': self.C,
            '_dual_coef_': array2bstr(self._dual_coef_, self._sparse),
            'dual_coef_': array2bstr(self.dual_coef_, self._sparse),
            'support_vectors_': array2bstr(self.support_vectors_, self._sparse),
            '_gamma': self._gamma,
            '_impl': self._impl,
            '_intercept_': self._intercept_.tolist(),
            '_sparse': self._sparse,
            'cache_size': self.cache_size,
            'class_weight': self.class_weight,
            'class_weight_': self.class_weight_.tolist(),
            'classes_': self.classes_.tolist(),
            'coef0': self.coef0,
            'decision_function_shape': self.decision_function_shape,
            'degree': self.degree,
            'epsilon': self.epsilon,
            'fit_status_': self.fit_status_,
            'gamma': self.gamma,
            'intercept_': self.intercept_.tolist(),
            'kernel': self.kernel,
            'max_iter': self.max_iter,
            'n_support_': self.n_support_.tolist(),
            'nu': self.nu,
            'probA_': self.probA_.tolist(),
            'probB_': self.probB_.tolist(),
            'probability': self.probability,
            'random_state': self.random_state,
            'shape_fit_': self.shape_fit_,
            'shrinking': self.shrinking,
            'support_': self.support_.tolist(),
            'tol': self.tol,
            'verbose': self.verbose,
        }
        return dict_


class SavableLinearSVC(LinearSVC, Savable):
    @classmethod
    def from_super(cls, superinstance):
        mutation_warning()
        instance = cls()
        instance.C = superinstance.C
        instance.class_weight = superinstance.class_weight
        instance.classes_ = superinstance.classes_
        instance.coef_ = superinstance.coef_
        instance.dual = superinstance.dual
        instance.fit_intercept = superinstance.fit_intercept
        instance.intercept_ = superinstance.intercept_
        instance.intercept_scaling = superinstance.intercept_scaling
        instance.loss = superinstance.loss
        instance.max_iter = superinstance.max_iter
        instance.multi_class = superinstance.multi_class
        instance.n_iter_ = superinstance.n_iter_
        instance.penalty = superinstance.penalty
        instance.random_state = superinstance.random_state
        instance.tol = superinstance.tol
        instance.verbose = superinstance.verbose
        return instance

    def to_super(self):
        superinstance = LinearSVC()
        superinstance.C = self.C
        superinstance.class_weight = self.class_weight
        superinstance.classes_ = self.classes_
        superinstance.coef_ = self.coef_
        superinstance.dual = self.dual
        superinstance.fit_intercept = self.fit_intercept
        superinstance.intercept_ = self.intercept_
        superinstance.intercept_scaling = self.intercept_scaling
        superinstance.loss = self.loss
        superinstance.max_iter = self.max_iter
        superinstance.multi_class = self.multi_class
        superinstance.n_iter_ = self.n_iter_
        superinstance.penalty = self.penalty
        superinstance.random_state = self.random_state
        superinstance.tol = self.tol
        superinstance.verbose = self.verbose
        return superinstance

    def to_dict(self):
        return {
            'C': self.C,
            'class_weight': self.class_weight,
            'classes_': self.classes_.tolist(),
            'coef_': self.coef_.tolist(),
            'dual': self.dual,
            'fit_intercept': self.fit_intercept,
            'intercept_': self.intercept_.tolist(),
            'intercept_scaling': self.intercept_scaling,
            'loss': self.loss,
            'max_iter': self.max_iter,
            'multi_class': self.multi_class,
            'n_iter_': int(self.n_iter_),
            'penalty': self.penalty,
            'random_state': self.random_state,
            'tol': self.tol,
            'verbose': self.verbose,
    }

    @classmethod
    def from_dict(cls, dct):
        instance = cls()
        instance.C = dct["C"]
        instance.class_weight = dct["class_weight"]
        instance.classes_ = np.array(dct["classes_"])
        instance.coef_ = np.array(dct["coef_"])
        instance.dual = dct["dual"]
        instance.fit_intercept = dct["fit_intercept"]
        instance.intercept_ = np.array(dct["intercept_"])
        instance.intercept_scaling = dct["intercept_scaling"]
        instance.loss = dct["loss"]
        instance.max_iter = dct["max_iter"]
        instance.multi_class = dct["multi_class"]
        instance.n_iter_ = dct["n_iter_"]
        instance.penalty = dct["penalty"]
        instance.random_state = dct["random_state"]
        instance.tol = dct["tol"]
        instance.verbose = dct["verbose"]
        return instance
