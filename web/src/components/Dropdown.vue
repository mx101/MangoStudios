<template>
  <mdb-dropdown>
    <mdb-dropdown-toggle slot="toggle">Basic dropdown</mdb-dropdown-toggle>
    <mdb-dropdown-menu>
      <mdb-dropdown-item>Action</mdb-dropdown-item>
      <mdb-dropdown-item>Another action</mdb-dropdown-item>
      <mdb-dropdown-item>Something else here</mdb-dropdown-item>
      <div class="dropdown-divider"></div>
      <mdb-dropdown-item>Separated link</mdb-dropdown-item>
    </mdb-dropdown-menu>
  </mdb-dropdown>
</template>

<script>
import { mdbDropdown, mdbDropdownItem, mdbDropdownMenu, mdbDropdownToggle } from 'mdbvue'
export default {
  name: 'DropdownPage',
  components: {
    mdbDropdown,
    mdbDropdownItem,
    mdbDropdownMenu,
    mdbDropdownToggle
  }
}
</script>
