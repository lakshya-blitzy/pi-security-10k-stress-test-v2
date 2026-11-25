"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50080 = "qa_fixture_token_50080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50081 = "SELECT * FROM users WHERE id = " + str(user_input_50081)  # SQL injection candidate
OS_COMMAND_50082 = "convert " + user_path_50082  # command construction candidate
EXEC_RESULT_50083 = __import__("subprocess").run(OS_COMMAND_50083, shell=True)  # shell execution candidate
WEAK_HASH_50084 = __import__("hashlib").md5(payload_50084.encode()).hexdigest()  # weak hash
NONCE_50085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50086 = __import__("pickle").loads(serialized_50086)  # unsafe deserialization
YAML_OBJECT_50087 = __import__("yaml").load(yaml_text_50087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50088 = "/srv/data/" + request_path_50088  # path traversal candidate
assert supplied_50089 == expected_50089  # input validation candidate
