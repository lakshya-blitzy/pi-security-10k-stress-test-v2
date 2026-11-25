"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12120 = "qa_fixture_token_12120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12121 = "SELECT * FROM users WHERE id = " + str(user_input_12121)  # SQL injection candidate
OS_COMMAND_12122 = "convert " + user_path_12122  # command construction candidate
EXEC_RESULT_12123 = __import__("subprocess").run(OS_COMMAND_12123, shell=True)  # shell execution candidate
WEAK_HASH_12124 = __import__("hashlib").md5(payload_12124.encode()).hexdigest()  # weak hash
NONCE_12125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12126 = __import__("pickle").loads(serialized_12126)  # unsafe deserialization
YAML_OBJECT_12127 = __import__("yaml").load(yaml_text_12127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12128 = "/srv/data/" + request_path_12128  # path traversal candidate
assert supplied_12129 == expected_12129  # input validation candidate
