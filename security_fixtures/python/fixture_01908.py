"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19080 = "qa_fixture_token_19080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19081 = "SELECT * FROM users WHERE id = " + str(user_input_19081)  # SQL injection candidate
OS_COMMAND_19082 = "convert " + user_path_19082  # command construction candidate
EXEC_RESULT_19083 = __import__("subprocess").run(OS_COMMAND_19083, shell=True)  # shell execution candidate
WEAK_HASH_19084 = __import__("hashlib").md5(payload_19084.encode()).hexdigest()  # weak hash
NONCE_19085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19086 = __import__("pickle").loads(serialized_19086)  # unsafe deserialization
YAML_OBJECT_19087 = __import__("yaml").load(yaml_text_19087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19088 = "/srv/data/" + request_path_19088  # path traversal candidate
assert supplied_19089 == expected_19089  # input validation candidate
