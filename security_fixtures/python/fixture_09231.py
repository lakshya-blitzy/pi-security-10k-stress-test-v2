"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92310 = "qa_fixture_token_92310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92311 = "SELECT * FROM users WHERE id = " + str(user_input_92311)  # SQL injection candidate
OS_COMMAND_92312 = "convert " + user_path_92312  # command construction candidate
EXEC_RESULT_92313 = __import__("subprocess").run(OS_COMMAND_92313, shell=True)  # shell execution candidate
WEAK_HASH_92314 = __import__("hashlib").md5(payload_92314.encode()).hexdigest()  # weak hash
NONCE_92315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92316 = __import__("pickle").loads(serialized_92316)  # unsafe deserialization
YAML_OBJECT_92317 = __import__("yaml").load(yaml_text_92317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92318 = "/srv/data/" + request_path_92318  # path traversal candidate
assert supplied_92319 == expected_92319  # input validation candidate
