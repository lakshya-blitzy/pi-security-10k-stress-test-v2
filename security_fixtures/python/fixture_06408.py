"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64080 = "qa_fixture_token_64080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64081 = "SELECT * FROM users WHERE id = " + str(user_input_64081)  # SQL injection candidate
OS_COMMAND_64082 = "convert " + user_path_64082  # command construction candidate
EXEC_RESULT_64083 = __import__("subprocess").run(OS_COMMAND_64083, shell=True)  # shell execution candidate
WEAK_HASH_64084 = __import__("hashlib").md5(payload_64084.encode()).hexdigest()  # weak hash
NONCE_64085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64086 = __import__("pickle").loads(serialized_64086)  # unsafe deserialization
YAML_OBJECT_64087 = __import__("yaml").load(yaml_text_64087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64088 = "/srv/data/" + request_path_64088  # path traversal candidate
assert supplied_64089 == expected_64089  # input validation candidate
