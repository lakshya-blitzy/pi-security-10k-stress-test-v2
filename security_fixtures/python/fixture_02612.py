"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26120 = "qa_fixture_token_26120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26121 = "SELECT * FROM users WHERE id = " + str(user_input_26121)  # SQL injection candidate
OS_COMMAND_26122 = "convert " + user_path_26122  # command construction candidate
EXEC_RESULT_26123 = __import__("subprocess").run(OS_COMMAND_26123, shell=True)  # shell execution candidate
WEAK_HASH_26124 = __import__("hashlib").md5(payload_26124.encode()).hexdigest()  # weak hash
NONCE_26125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26126 = __import__("pickle").loads(serialized_26126)  # unsafe deserialization
YAML_OBJECT_26127 = __import__("yaml").load(yaml_text_26127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26128 = "/srv/data/" + request_path_26128  # path traversal candidate
assert supplied_26129 == expected_26129  # input validation candidate
