#!/usr/bin/env python

# Master Script For Running #

import argparse
import sys

import extracting.kicktionary
import extracting.ticker
import extracting.arguments
import extracting.frame_extract
import reasoning.solver
import reasoning.asp_conversion

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kicktionary", dest="kicktionary", help="location of kicktionary xml file", default="data/kicktionary.xml")
    parser.add_argument("--tickers", dest="tickers", help="location of parsed ticker conll file", default=['data/parsed/p5.parsed'], nargs="*")
    parser.add_argument("--verbose", dest="verbose", help="print helpful messages about the progress", default=False)
    parser.add_argument("--language", dest="language", help="language of tickers (en or de)", default="en")
    ## will need to add verbnet XML file(s) at some point, maybe a complete folder
    parser.add_argument("--verbnet", dest="verbnet", help="location of folder with verbnet xml files", default="data/verbnet")
    parser.add_argument("--luorder", dest="luorder", help="location of folder with lexical unit order file", default="data/lu_order")
    args = parser.parse_args()

    verbose = args.verbose
    language = args.language

    print args.tickers

    events = []

    for ticker in args.tickers:
        # Reads in a kicktionary xml file and returns a list of lexical unit objects
        kicktionary = extracting.kicktionary.read_kicktionary(args.kicktionary, verbose, language)
        #verbnet = read_verbnet(options.verbnet)

        # Reads in a parsed ticker feed in dependency tree conll format and returns a list of tree objects
        ticker = extracting.ticker.read_ticker(ticker, verbose, language)
        #print ticker

        ticker_with_lus = extracting.frame_extract.kicktionary_lookup_possible_lu(kicktionary, ticker, verbose)
        #luorder = [line.rstrip('\n') for line in open(options.luorder).readlines()]
        #print ticker_with_lus

        # Iteration over all objects in the ticker list and returns a list of event objects, ready for translation to asp
        events.extend(extracting.arguments.find_arguments(ticker, ticker_with_lus, kicktionary, verbose))

    #print events
    #print [e.minute for e in events]

    #print reasoning.asp_conversion.to_asp(events)

    # converts each event object into asp format
    # then resolves event issues, processes.
    asp = reasoning.solver.solve(events)
    
    # What we want to do with the result?
    print "\n".join(map(str,asp))


if __name__ == "__main__":
    main()
