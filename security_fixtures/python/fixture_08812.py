"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88120 = "qa_fixture_token_88120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88121 = "SELECT * FROM users WHERE id = " + str(user_input_88121)  # SQL injection candidate
OS_COMMAND_88122 = "convert " + user_path_88122  # command construction candidate
EXEC_RESULT_88123 = __import__("subprocess").run(OS_COMMAND_88123, shell=True)  # shell execution candidate
WEAK_HASH_88124 = __import__("hashlib").md5(payload_88124.encode()).hexdigest()  # weak hash
NONCE_88125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88126 = __import__("pickle").loads(serialized_88126)  # unsafe deserialization
YAML_OBJECT_88127 = __import__("yaml").load(yaml_text_88127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88128 = "/srv/data/" + request_path_88128  # path traversal candidate
assert supplied_88129 == expected_88129  # input validation candidate
