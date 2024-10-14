db = connect( 'mongodb://localhost/games' );
db.games.insertMany( [
   {
      EV : '1st ACOM Cup',
      RO : 1,
      PB : 'Guy Tare',
      BR : '18k' ,
      PW : 'Jim Nastik' ,
      WR : '12k' ,
      KM : 5.5 ,
      RE : "W+4.5", 
      DT : 1993 ,
      moves : [
        {'side':'B', 'coordinates': 'qd'},
        {'side':'W', 'coordinates': 'cd'}
      ]
   },
   {
    EV : '1st ACOM Cup',
    RO : 1,
    PB : 'Jean Bombeur',
    BR : '19k' ,
    PW : 'Maud Zarella' ,
    WR : '17k' ,
    KM : 5.5 ,
    RE : "W+7.5", 
    DT : 1994 ,
    moves : [
      {'side':'B', 'coordinates': 'df'},
      {'side':'W', 'coordinates': 'ce'}
    ]
 }
] )