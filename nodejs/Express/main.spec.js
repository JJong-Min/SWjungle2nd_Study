const assert = require('assert');
const should = require('should');
const request = require('supertest');
const app = require('./main');

describe('GET /users', () => {
    it('배열을 반환한다.', (done) => {
        request(app)
            .get('/users')
            .end((err, res) => {
                res.body.should.be.instanceOf(Array);
                res.body.forEach(user => {
                    user.should.have.property('name');
                });
                done();
            });
    });
})