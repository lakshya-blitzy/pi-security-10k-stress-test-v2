"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70080 = "qa_fixture_token_70080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70081 = "SELECT * FROM users WHERE id = " + str(user_input_70081)  # SQL injection candidate
OS_COMMAND_70082 = "convert " + user_path_70082  # command construction candidate
EXEC_RESULT_70083 = __import__("subprocess").run(OS_COMMAND_70083, shell=True)  # shell execution candidate
WEAK_HASH_70084 = __import__("hashlib").md5(payload_70084.encode()).hexdigest()  # weak hash
NONCE_70085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70086 = __import__("pickle").loads(serialized_70086)  # unsafe deserialization
YAML_OBJECT_70087 = __import__("yaml").load(yaml_text_70087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70088 = "/srv/data/" + request_path_70088  # path traversal candidate
assert supplied_70089 == expected_70089  # input validation candidate
