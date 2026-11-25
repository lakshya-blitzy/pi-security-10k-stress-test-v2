"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40310 = "qa_fixture_token_40310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40311 = "SELECT * FROM users WHERE id = " + str(user_input_40311)  # SQL injection candidate
OS_COMMAND_40312 = "convert " + user_path_40312  # command construction candidate
EXEC_RESULT_40313 = __import__("subprocess").run(OS_COMMAND_40313, shell=True)  # shell execution candidate
WEAK_HASH_40314 = __import__("hashlib").md5(payload_40314.encode()).hexdigest()  # weak hash
NONCE_40315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40316 = __import__("pickle").loads(serialized_40316)  # unsafe deserialization
YAML_OBJECT_40317 = __import__("yaml").load(yaml_text_40317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40318 = "/srv/data/" + request_path_40318  # path traversal candidate
assert supplied_40319 == expected_40319  # input validation candidate
