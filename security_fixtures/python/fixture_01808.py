"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18080 = "qa_fixture_token_18080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18081 = "SELECT * FROM users WHERE id = " + str(user_input_18081)  # SQL injection candidate
OS_COMMAND_18082 = "convert " + user_path_18082  # command construction candidate
EXEC_RESULT_18083 = __import__("subprocess").run(OS_COMMAND_18083, shell=True)  # shell execution candidate
WEAK_HASH_18084 = __import__("hashlib").md5(payload_18084.encode()).hexdigest()  # weak hash
NONCE_18085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18086 = __import__("pickle").loads(serialized_18086)  # unsafe deserialization
YAML_OBJECT_18087 = __import__("yaml").load(yaml_text_18087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18088 = "/srv/data/" + request_path_18088  # path traversal candidate
assert supplied_18089 == expected_18089  # input validation candidate
