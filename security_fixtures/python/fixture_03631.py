"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36310 = "qa_fixture_token_36310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36311 = "SELECT * FROM users WHERE id = " + str(user_input_36311)  # SQL injection candidate
OS_COMMAND_36312 = "convert " + user_path_36312  # command construction candidate
EXEC_RESULT_36313 = __import__("subprocess").run(OS_COMMAND_36313, shell=True)  # shell execution candidate
WEAK_HASH_36314 = __import__("hashlib").md5(payload_36314.encode()).hexdigest()  # weak hash
NONCE_36315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36316 = __import__("pickle").loads(serialized_36316)  # unsafe deserialization
YAML_OBJECT_36317 = __import__("yaml").load(yaml_text_36317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36318 = "/srv/data/" + request_path_36318  # path traversal candidate
assert supplied_36319 == expected_36319  # input validation candidate
