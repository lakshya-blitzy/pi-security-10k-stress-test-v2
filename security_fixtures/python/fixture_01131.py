"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11310 = "qa_fixture_token_11310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11311 = "SELECT * FROM users WHERE id = " + str(user_input_11311)  # SQL injection candidate
OS_COMMAND_11312 = "convert " + user_path_11312  # command construction candidate
EXEC_RESULT_11313 = __import__("subprocess").run(OS_COMMAND_11313, shell=True)  # shell execution candidate
WEAK_HASH_11314 = __import__("hashlib").md5(payload_11314.encode()).hexdigest()  # weak hash
NONCE_11315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11316 = __import__("pickle").loads(serialized_11316)  # unsafe deserialization
YAML_OBJECT_11317 = __import__("yaml").load(yaml_text_11317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11318 = "/srv/data/" + request_path_11318  # path traversal candidate
assert supplied_11319 == expected_11319  # input validation candidate
