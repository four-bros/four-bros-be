from typing import List

from src.constants import session
from src.data_models.PlayerInfo import PlayerInfo
from src.models.Player import(
    PlayerAbilities,
    Player,
    PlayerDetails
)
from src.responses.Players import(
    PlayerSchema
)


player_schema_single = PlayerSchema()
player_schema_list = PlayerSchema(many=True)


def get_all_players(request):
    
    players: List[PlayerInfo] = session.query(PlayerInfo).all()

    players_json = []

    for player in players:
        player_details = PlayerDetails(
            id=player.id,
            team_id=player.team_id,
            first_name=player.first_name,
            last_name=player.last_name,
            height=player.height,
            weight=player.weight,
            jersey_number=player.jersey_number,
            player_year=player.player_year,
            redshirt=player.redshirt,
            position=player.position,
            hometown_desc=player.hometown_desc
        )

        player_abilities = PlayerAbilities(
            play_recognition=player.play_recognition,
            press=player.press,
            power_moves=player.power_moves,
            kick_accuracy=player.kick_accuracy,
            throwing_power=player.throwing_power,
            throwing_accuracy=player.throwing_accuracy,
            overall=player.overall,
            agility=player.agility,
            stamina=player.stamina,
            acceleration=player.acceleration,
            pursuit=player.pursuit,
            route_running=player.route_running,
            speed=player.speed,
            trucking=player.trucking,
            ball_carrier_vision=player.ball_carrier_vision,
            catch_in_traffic=player.catch_in_traffic,
            block_shedding=player.block_shedding,
            strength=player.strength,
            catch=player.catch,
            injury=player.injury,
            tackling=player.tackling,
            pass_blocking=player.pass_blocking,
            run_blocking=player.run_blocking,
            break_tackle=player.break_tackle,
            impact_blocking=player.impact_blocking,
            jump=player.jump,
            carry=player.carry,
            stiff_arm=player.stiff_arm,
            kick_power=player.kick_power,
            awareness=player.awareness,
            release=player.release,
            spec_catch=player.spec_catch,
            elusiveness=player.elusiveness,
            spin_move=player.spin_move,
            hit_power=player.hit_power,
            kick_return=player.kick_return,
            man_coverage=player.man_coverage,
            zone_coverage=player.zone_coverage,
            finesse_moves=player.finesse_moves,
            juke_move=player.juke_move,
        )

        player = Player(
            player_details=player_details,
            player_abilities=player_abilities
        )

        player_json = player_schema_single.dump(player)
        players_json.append(player_json)
    
    response = {
        'players': players_json
    }
    
    return response


def get_player_by_player_id(request, player_id) -> PlayerSchema:
    player: PlayerInfo = session.query(PlayerInfo).where(
        PlayerInfo.id == player_id).one()
    
    player_details = PlayerDetails(
        id=player.id,
        team_id=player.team_id,
        first_name=player.first_name,
        last_name=player.last_name,
        height=player.height,
        weight=player.weight,
        jersey_number=player.jersey_number,
        player_year=player.player_year,
        redshirt=player.redshirt,
        position=player.position,
        hometown_desc=player.hometown_desc
    )

    player_abilities = PlayerAbilities(
        play_recognition=player.play_recognition,
        press=player.press,
        power_moves=player.power_moves,
        kick_accuracy=player.kick_accuracy,
        throwing_power=player.throwing_power,
        throwing_accuracy=player.throwing_accuracy,
        overall=player.overall,
        agility=player.agility,
        stamina=player.stamina,
        acceleration=player.acceleration,
        pursuit=player.pursuit,
        route_running=player.route_running,
        speed=player.speed,
        trucking=player.trucking,
        ball_carrier_vision=player.ball_carrier_vision,
        catch_in_traffic=player.catch_in_traffic,
        block_shedding=player.block_shedding,
        strength=player.strength,
        catch=player.catch,
        injury=player.injury,
        tackling=player.tackling,
        pass_blocking=player.pass_blocking,
        run_blocking=player.run_blocking,
        break_tackle=player.break_tackle,
        impact_blocking=player.impact_blocking,
        jump=player.jump,
        carry=player.carry,
        stiff_arm=player.stiff_arm,
        kick_power=player.kick_power,
        awareness=player.awareness,
        release=player.release,
        spec_catch=player.spec_catch,
        elusiveness=player.elusiveness,
        spin_move=player.spin_move,
        hit_power=player.hit_power,
        kick_return=player.kick_return,
        man_coverage=player.man_coverage,
        zone_coverage=player.zone_coverage,
        finesse_moves=player.finesse_moves,
        juke_move=player.juke_move,
    )

    player = Player(
        player_details=player_details,
        player_abilities=player_abilities
    )

    response = player_schema_single.dump(player)
    
    return response


def get_players_by_team_id(request, team_id):
    players: List[PlayerInfo] = session.query(PlayerInfo).where(
        PlayerInfo.team_id == team_id).all()
    players.sort(key=lambda p: p.overall, reverse=True)
    players_json = player_schema_list.dump(players)
    
    response = {
        'players': players_json
    }
    
    return response


def get_players_by_team_id_and_position(team_id: int, position: str):
    
    players: List[PlayerInfo] = session.query(PlayerInfo).filter(
        PlayerInfo.team_id == team_id,
        PlayerInfo.position == position.upper()
    ).all()
    
    players_json = player_schema_list.dump(players)
    
    response = {
        'players': players_json
    }
    
    return response
