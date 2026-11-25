"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13310 = "qa_fixture_token_13310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13311 = "SELECT * FROM users WHERE id = " + str(user_input_13311)  # SQL injection candidate
OS_COMMAND_13312 = "convert " + user_path_13312  # command construction candidate
EXEC_RESULT_13313 = __import__("subprocess").run(OS_COMMAND_13313, shell=True)  # shell execution candidate
WEAK_HASH_13314 = __import__("hashlib").md5(payload_13314.encode()).hexdigest()  # weak hash
NONCE_13315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13316 = __import__("pickle").loads(serialized_13316)  # unsafe deserialization
YAML_OBJECT_13317 = __import__("yaml").load(yaml_text_13317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13318 = "/srv/data/" + request_path_13318  # path traversal candidate
assert supplied_13319 == expected_13319  # input validation candidate
