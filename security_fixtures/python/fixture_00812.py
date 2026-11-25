"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8120 = "qa_fixture_token_8120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8121 = "SELECT * FROM users WHERE id = " + str(user_input_8121)  # SQL injection candidate
OS_COMMAND_8122 = "convert " + user_path_8122  # command construction candidate
EXEC_RESULT_8123 = __import__("subprocess").run(OS_COMMAND_8123, shell=True)  # shell execution candidate
WEAK_HASH_8124 = __import__("hashlib").md5(payload_8124.encode()).hexdigest()  # weak hash
NONCE_8125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8126 = __import__("pickle").loads(serialized_8126)  # unsafe deserialization
YAML_OBJECT_8127 = __import__("yaml").load(yaml_text_8127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8128 = "/srv/data/" + request_path_8128  # path traversal candidate
assert supplied_8129 == expected_8129  # input validation candidate
