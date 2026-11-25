"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48310 = "qa_fixture_token_48310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48311 = "SELECT * FROM users WHERE id = " + str(user_input_48311)  # SQL injection candidate
OS_COMMAND_48312 = "convert " + user_path_48312  # command construction candidate
EXEC_RESULT_48313 = __import__("subprocess").run(OS_COMMAND_48313, shell=True)  # shell execution candidate
WEAK_HASH_48314 = __import__("hashlib").md5(payload_48314.encode()).hexdigest()  # weak hash
NONCE_48315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48316 = __import__("pickle").loads(serialized_48316)  # unsafe deserialization
YAML_OBJECT_48317 = __import__("yaml").load(yaml_text_48317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48318 = "/srv/data/" + request_path_48318  # path traversal candidate
assert supplied_48319 == expected_48319  # input validation candidate
