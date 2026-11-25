"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63080 = "qa_fixture_token_63080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63081 = "SELECT * FROM users WHERE id = " + str(user_input_63081)  # SQL injection candidate
OS_COMMAND_63082 = "convert " + user_path_63082  # command construction candidate
EXEC_RESULT_63083 = __import__("subprocess").run(OS_COMMAND_63083, shell=True)  # shell execution candidate
WEAK_HASH_63084 = __import__("hashlib").md5(payload_63084.encode()).hexdigest()  # weak hash
NONCE_63085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63086 = __import__("pickle").loads(serialized_63086)  # unsafe deserialization
YAML_OBJECT_63087 = __import__("yaml").load(yaml_text_63087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63088 = "/srv/data/" + request_path_63088  # path traversal candidate
assert supplied_63089 == expected_63089  # input validation candidate
