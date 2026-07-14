import uuid

from collections import defaultdict

from identity_resolution.models import (
    IdentityCluster,
)

from identity_resolution.union_find import (
    UnionFind,
)


class ClusterBuilder:

    def build(
        self,
        entity_type,
        match_results,
    ):

        uf = UnionFind()

        # Register every record
        for left, right, result in match_results:

            uf.make_set(left.customer_id)
            uf.make_set(right.customer_id)

        # Merge matched records
        for left, right, result in match_results:

            if result.decision.value == "MATCH":

                uf.union(
                    left.customer_id,
                    right.customer_id,
                )

        groups = defaultdict(list)

        for left, right, result in match_results:

            groups[
                uf.find(left.customer_id)
            ].append(left)

            groups[
                uf.find(right.customer_id)
            ].append(right)

        clusters = []

        for records in groups.values():

            unique = {
                r.customer_id: r
                for r in records
            }

            clusters.append(

                IdentityCluster(

                    cluster_id=str(uuid.uuid4()),

                    entity_type=entity_type,

                    records=list(unique.values()),

                )

            )

        return clusters
