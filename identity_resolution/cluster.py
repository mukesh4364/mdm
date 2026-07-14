from identity_resolution.cluster_builder import (
    ClusterBuilder,
)


class ClusterEngine:

    def __init__(self):

        self.builder = ClusterBuilder()

    def build_clusters(
        self,
        entity_type,
        match_results,
    ):

        return self.builder.build(
            entity_type,
            match_results,
        )
