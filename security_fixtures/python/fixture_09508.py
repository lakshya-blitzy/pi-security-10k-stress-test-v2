"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95080 = "qa_fixture_token_95080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95081 = "SELECT * FROM users WHERE id = " + str(user_input_95081)  # SQL injection candidate
OS_COMMAND_95082 = "convert " + user_path_95082  # command construction candidate
EXEC_RESULT_95083 = __import__("subprocess").run(OS_COMMAND_95083, shell=True)  # shell execution candidate
WEAK_HASH_95084 = __import__("hashlib").md5(payload_95084.encode()).hexdigest()  # weak hash
NONCE_95085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95086 = __import__("pickle").loads(serialized_95086)  # unsafe deserialization
YAML_OBJECT_95087 = __import__("yaml").load(yaml_text_95087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95088 = "/srv/data/" + request_path_95088  # path traversal candidate
assert supplied_95089 == expected_95089  # input validation candidate
