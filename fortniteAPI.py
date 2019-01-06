from FortniteAPI import FortniteAPI

def get_lifetime_stats(*player):
    FortniteAPI.api_key = '' # add fortnitetracker API-key here
    player = FortniteAPI('pc', ' '.join(player))

    stats = {}

    stats['wins'] = player.stats.LIFETIME_WINS
    stats['win_percent'] = player.stats.LIFETIME_WIN_PERCENTAGE
    stats['kills'] = player.stats.LIFETIME_KILLS
    stats['kd'] = player.stats.LIFETIME_KD

    return stats


def get_current_season_stats(*player):
    FortniteAPI.api_key = ''
    player = FortniteAPI('pc', ' '.join(player))

    stats = {}

    stats['solo_wins'] = player.stats.CURRENT_SOLO_WINS
    stats['duo_wins'] = player.stats.CURRENT_DUO_WINS
    stats['squad_wins'] = player.stats.CURRENT_SQUAD_WINS

    stats['solo_win_percent'] = str(round((int(stats['solo_wins']) / int(player.stats.CURRENT_SOLO_MATCHES)) * 100)) + '%'
    stats['duo_win_percent'] = str(round((int(stats['duo_wins']) / int(player.stats.CURRENT_DUO_MATCHES)) * 100)) + '%'
    stats['squad_win_percent'] = str(round((int(stats['squad_wins']) / int(player.stats.CURRENT_SQUAD_MATCHES)) * 100)) + '%'

    stats['solo_kills'] = player.stats.CURRENT_SOLO_KILLS
    stats['duo_kills'] = player.stats.CURRENT_DUO_KILLS
    stats['squad_kills'] = player.stats.CURRENT_SQUAD_KILLS

    stats['solo_kd'] = player.stats.CURRENT_SOLO_KD
    stats['duo_kd'] = player.stats.CURRENT_DUO_KD
    stats['squad_kd'] = player.stats.CURRENT_SQUAD_KD

    return stats
