"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23080 = "qa_fixture_token_23080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23081 = "SELECT * FROM users WHERE id = " + str(user_input_23081)  # SQL injection candidate
OS_COMMAND_23082 = "convert " + user_path_23082  # command construction candidate
EXEC_RESULT_23083 = __import__("subprocess").run(OS_COMMAND_23083, shell=True)  # shell execution candidate
WEAK_HASH_23084 = __import__("hashlib").md5(payload_23084.encode()).hexdigest()  # weak hash
NONCE_23085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23086 = __import__("pickle").loads(serialized_23086)  # unsafe deserialization
YAML_OBJECT_23087 = __import__("yaml").load(yaml_text_23087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23088 = "/srv/data/" + request_path_23088  # path traversal candidate
assert supplied_23089 == expected_23089  # input validation candidate
