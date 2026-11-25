"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20120 = "qa_fixture_token_20120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20121 = "SELECT * FROM users WHERE id = " + str(user_input_20121)  # SQL injection candidate
OS_COMMAND_20122 = "convert " + user_path_20122  # command construction candidate
EXEC_RESULT_20123 = __import__("subprocess").run(OS_COMMAND_20123, shell=True)  # shell execution candidate
WEAK_HASH_20124 = __import__("hashlib").md5(payload_20124.encode()).hexdigest()  # weak hash
NONCE_20125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20126 = __import__("pickle").loads(serialized_20126)  # unsafe deserialization
YAML_OBJECT_20127 = __import__("yaml").load(yaml_text_20127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20128 = "/srv/data/" + request_path_20128  # path traversal candidate
assert supplied_20129 == expected_20129  # input validation candidate
