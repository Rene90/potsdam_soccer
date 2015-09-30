#!/usr/bin/env python

# Master Script For Running #

import optparse
import sys

<<<<<<< HEAD
import extracting
import reasoning
=======
import ticker_to_kicker
import dt_to_kicktionary
import asp
>>>>>>> 1d4a1536e2969e96c9b5c08ee811d3564ba7c4d8

def main():
    parser = optparse.OptionParser()
    parser.add_option("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="data/kicktionary.xml")
    parser.add_option("--ticker", dest="ticker", help="location of parsed ticker conll file", default="data/parsed/p4.parsed")
    parser.add_option("--verbose", dest="verbose", help="print helpful messages about the progress", default=False)
    parser.add_option("--language", dest="language", help="language of tickers (en or de)", default="en")
    ## will need to add verbnet XML file(s) at some point, maybe a complete folder
    parser.add_option("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="data/verbnet")
    parser.add_option("--luorder", dest="luorder", help="location of folder with lexical unit order file", default="data/lu_order")
    (options, args) = parser.parse_args()

    verbose = options.verbose
    language = options.language
<<<<<<< HEAD
    
    # Reads in a kicktionary xml file and returns a list of lexical unit objects
    kicktionary = extracting.kicktionary.read_kicktionary(options.kicktionary, verbose, language)
    #verbnet = read_verbnet(options.verbnet)
    
    # Reads in a parsed ticker feed in dependency tree conll format and returns a list of tree objects
    ticker = extracting.ticker.read_ticker(options.ticker, verbose, language)
=======

	ticker = read_ticker(options.ticker, verbose, language)
    kicktionary = read_kicktionary(options.kicktionary, verbose, language)
    #verbnet = read_verbnet(options.verbnet)
>>>>>>> 1d4a1536e2969e96c9b5c08ee811d3564ba7c4d8
    #ticker_with_lus = kicktionary_lookup_possible_lu(kicktionary, ticker, verbose)
    #luorder = [line.rstrip('\n') for line in open(options.luorder).readlines()]
    
    # Iteration over all objects in the ticker list and returns a list of event objects, ready for translation to asp
    events = extracting.arguments.find_arguments(ticker, verbose)
    
    # converts each event object into asp format
    # then resolves event issues, processes.
    asp = reasoning.solver.solve(events)
    
    # What we want to do with the result?
    # asp -> whatever...
    

if __name__ == "__main__":
    main()

