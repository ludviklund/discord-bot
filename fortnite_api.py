from FortniteAPI import FortniteAPI 
import config

def get_lifetime_stats(*args):
    FortniteAPI.api_key = '06805a5a-0c04-4239-9d73-61fb22cb8ef6'
    player = FortniteAPI('pc', ' '.join(args))

    stats = {}
    stat_titles = config.lifetime_titles
    stat_values = [
        player.stats.LIFETIME_MATCHES, player.stats.LIFETIME_WINS, player.stats.LIFETIME_WIN_PERCENTAGE,
        player.stats.LIFETIME_KILLS, player.stats.LIFETIME_KD, player.stats.LIFETIME_SCORE
    ]

    for k, v in zip(stat_titles, stat_values):
        stats[k] = v

    return stats


def get_current_season_stats(*args):
    FortniteAPI.api_key = '06805a5a-0c04-4239-9d73-61fb22cb8ef6'
    player = FortniteAPI('pc', ' '.join(args))

    stats = {}
    stat_names = config.current_season_titles
    stat_values = [
        player.stats.CURRENT_SOLO_WINS, player.stats.CURRENT_DUO_WINS, player.stats.CURRENT_SQUAD_WINS,
        str(round((int(player.stats.CURRENT_SOLO_WINS) / int(player.stats.CURRENT_SOLO_MATCHES)) * 100)) + '%',
        str(round((int(player.stats.CURRENT_DUO_WINS) / int(player.stats.CURRENT_DUO_MATCHES)) * 100)) + '%',
        str(round((int(player.stats.CURRENT_SQUAD_WINS) / int(player.stats.CURRENT_SQUAD_MATCHES)) * 100)) + '%',
        player.stats.CURRENT_SOLO_KILLS, player.stats.CURRENT_DUO_KILLS, player.stats.CURRENT_SQUAD_KILLS, 
        player.stats.CURRENT_SOLO_KD, player.stats.CURRENT_DUO_KD, player.stats.CURRENT_SQUAD_KD
    ]

    for k, v in zip(stat_names, stat_values):
        stats[k] = v

    return stats
