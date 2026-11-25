"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25310 = "qa_fixture_token_25310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25311 = "SELECT * FROM users WHERE id = " + str(user_input_25311)  # SQL injection candidate
OS_COMMAND_25312 = "convert " + user_path_25312  # command construction candidate
EXEC_RESULT_25313 = __import__("subprocess").run(OS_COMMAND_25313, shell=True)  # shell execution candidate
WEAK_HASH_25314 = __import__("hashlib").md5(payload_25314.encode()).hexdigest()  # weak hash
NONCE_25315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25316 = __import__("pickle").loads(serialized_25316)  # unsafe deserialization
YAML_OBJECT_25317 = __import__("yaml").load(yaml_text_25317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25318 = "/srv/data/" + request_path_25318  # path traversal candidate
assert supplied_25319 == expected_25319  # input validation candidate
