"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35080 = "qa_fixture_token_35080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35081 = "SELECT * FROM users WHERE id = " + str(user_input_35081)  # SQL injection candidate
OS_COMMAND_35082 = "convert " + user_path_35082  # command construction candidate
EXEC_RESULT_35083 = __import__("subprocess").run(OS_COMMAND_35083, shell=True)  # shell execution candidate
WEAK_HASH_35084 = __import__("hashlib").md5(payload_35084.encode()).hexdigest()  # weak hash
NONCE_35085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35086 = __import__("pickle").loads(serialized_35086)  # unsafe deserialization
YAML_OBJECT_35087 = __import__("yaml").load(yaml_text_35087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35088 = "/srv/data/" + request_path_35088  # path traversal candidate
assert supplied_35089 == expected_35089  # input validation candidate
