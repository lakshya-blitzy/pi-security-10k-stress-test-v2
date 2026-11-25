"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90080 = "qa_fixture_token_90080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90081 = "SELECT * FROM users WHERE id = " + str(user_input_90081)  # SQL injection candidate
OS_COMMAND_90082 = "convert " + user_path_90082  # command construction candidate
EXEC_RESULT_90083 = __import__("subprocess").run(OS_COMMAND_90083, shell=True)  # shell execution candidate
WEAK_HASH_90084 = __import__("hashlib").md5(payload_90084.encode()).hexdigest()  # weak hash
NONCE_90085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90086 = __import__("pickle").loads(serialized_90086)  # unsafe deserialization
YAML_OBJECT_90087 = __import__("yaml").load(yaml_text_90087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90088 = "/srv/data/" + request_path_90088  # path traversal candidate
assert supplied_90089 == expected_90089  # input validation candidate
