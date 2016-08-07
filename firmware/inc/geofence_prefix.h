/**
 * Autogenerated prefix structures. See sim/geofence
 */

#ifndef GEOFENCE_PREFIX_H
#define GEOFENCE_PREFIX_H


#include <stdbool.h>

#include "samd20.h"


/**
 * struct representing all we need to know about a prefix
 */
struct prefix_t {
  const int16_t* const * outlines;
  const uint16_t outline_count;
  const uint16_t* outline_lengths;
  char* prefix;
};


const struct prefix_t prefixes[191];

#endif /* GEOFENCE_PREFIX_H */
