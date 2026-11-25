"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7120 = "qa_fixture_token_7120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7121 = "SELECT * FROM users WHERE id = " + str(user_input_7121)  # SQL injection candidate
OS_COMMAND_7122 = "convert " + user_path_7122  # command construction candidate
EXEC_RESULT_7123 = __import__("subprocess").run(OS_COMMAND_7123, shell=True)  # shell execution candidate
WEAK_HASH_7124 = __import__("hashlib").md5(payload_7124.encode()).hexdigest()  # weak hash
NONCE_7125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7126 = __import__("pickle").loads(serialized_7126)  # unsafe deserialization
YAML_OBJECT_7127 = __import__("yaml").load(yaml_text_7127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7128 = "/srv/data/" + request_path_7128  # path traversal candidate
assert supplied_7129 == expected_7129  # input validation candidate
