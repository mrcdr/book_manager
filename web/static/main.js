/* 貸出時のモーダルダイアログ */
Vue.component('modal-borrow', {
    props: ["item"],
    template: `
    <div class="overlay">
        <div class="content">
          <p>以下の書籍を貸し出します</p>
          <p><strong>{{ item.name }}</strong></p>
          <p>貸出者：<input type="text" v-model="nameInput" ref="nameField"></p>
          <div align="right">
            <button v-on:click="applyEvent"
　　　　　　　　　　v-bind:disabled="isEmptyName">OK</button>
            <button v-on:click="cancelEvent">キャンセル</button>
          </div>
        </div>
    </div>
    `,
    data: function() {
        return {nameInput: ""}
    },
    mounted: function() {
        this.$refs.nameField.focus()
    },
    methods: {
        applyEvent: function() {
            if(!this.isEmptyName) {
                this.$emit('from-child-ok', this.item, this.nameInput)
            }
        },
        cancelEvent: function() {
            this.$emit('from-child-cancel')
        }
    },
    computed: {
        isEmptyName: function() {
            return !Boolean(this.nameInput.trim())
        }
    }
})


/* 返却時のモーダルダイアログ */
Vue.component('modal-take-back', {
    props: ["item", "borrower"],
    template: `
    <div class="overlay">
        <div class="content">
          <p>以下の書籍を返却します</p>
          <p><strong>{{ item.name }}</strong></p>
          <p>貸出者：{{ borrower }}</p>
          <div align="right">
            <button v-on:click="applyEvent">OK</button>
            <button v-on:click="cancelEvent">キャンセル</button>
          </div>
        </div>
    </div>
    `,
    methods :{
        applyEvent: function(){
            this.$emit('from-child-ok', this.item)
        },
        cancelEvent: function(){
            this.$emit('from-child-cancel')
        }
    }
})


/* アプリ本体 */
new Vue({
    el: '#app',

    data: {
        books: [],
        borrowModalShow: false,
        takeBackModalShow: false,
        borrower: "",
        item: {name: ""}
    },

    created() {
        this.fetchData()
    },

    methods: {
        edit: function (item) {
            this.item = item

            if(item.is_borrowed) {
                this.borrower = item.borrower
                this.takeBackModalShow = true
            } else {
                this.borrowModalShow = true
            }
        },

        closeBorrowModal: function() {
            this.borrowModalShow = false
        },

        borrowModalOK: function(item, borrower) {
            this.patchData(item, borrower)
            this.borrowModalShow = false
        },

        closeTakeBackModal: function() {
            this.takeBackModalShow = false
        },

        takeBackModalOK: function(item) {
            this.patchData(item)
            this.takeBackModalShow = false
        },

        fetchData: function() {
            axios.get("/api/books")
            .then(response => {
                this.books = response.data.books
            })
            .catch(error => {
                console.log(error)
            })
        },

        patchData: function(item, borrower="") {
            endpoint = "/api/books/" + String(item.id)

            data = {to_borrow: !(item.is_borrowed),
                    borrower: borrower}

            axios.patch(endpoint, data)
            .catch(error => {
                console.log(error)
            })

            this.fetchData()
        }
    }
})
