# MonteCarloPlanner

Ce projet a permis de comparer l'efficacité des algorithmes de MRW (monte carlo random walk) et HSP sur les problèmes de plannification automatiques fournis (blocks, depot, gripper, logistics)

L'algo MRW a pour caractéristiques de ne s'arrêter que lorsqu'une solution est trouvée, pas forcément la plus efficace.
L'efficacité d'une solution trouvée se traduit par le nombre d'actions nécessaires pour aller de l'état initial à l'état solution.
On mesure également pour chaque problème le temps passé à rechercher une solution.
