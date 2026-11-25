"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21080 = "qa_fixture_token_21080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21081 = "SELECT * FROM users WHERE id = " + str(user_input_21081)  # SQL injection candidate
OS_COMMAND_21082 = "convert " + user_path_21082  # command construction candidate
EXEC_RESULT_21083 = __import__("subprocess").run(OS_COMMAND_21083, shell=True)  # shell execution candidate
WEAK_HASH_21084 = __import__("hashlib").md5(payload_21084.encode()).hexdigest()  # weak hash
NONCE_21085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21086 = __import__("pickle").loads(serialized_21086)  # unsafe deserialization
YAML_OBJECT_21087 = __import__("yaml").load(yaml_text_21087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21088 = "/srv/data/" + request_path_21088  # path traversal candidate
assert supplied_21089 == expected_21089  # input validation candidate
