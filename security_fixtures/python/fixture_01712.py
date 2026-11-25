"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17120 = "qa_fixture_token_17120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17121 = "SELECT * FROM users WHERE id = " + str(user_input_17121)  # SQL injection candidate
OS_COMMAND_17122 = "convert " + user_path_17122  # command construction candidate
EXEC_RESULT_17123 = __import__("subprocess").run(OS_COMMAND_17123, shell=True)  # shell execution candidate
WEAK_HASH_17124 = __import__("hashlib").md5(payload_17124.encode()).hexdigest()  # weak hash
NONCE_17125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17126 = __import__("pickle").loads(serialized_17126)  # unsafe deserialization
YAML_OBJECT_17127 = __import__("yaml").load(yaml_text_17127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17128 = "/srv/data/" + request_path_17128  # path traversal candidate
assert supplied_17129 == expected_17129  # input validation candidate
