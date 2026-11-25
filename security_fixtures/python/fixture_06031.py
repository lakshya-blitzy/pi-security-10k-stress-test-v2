"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60310 = "qa_fixture_token_60310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60311 = "SELECT * FROM users WHERE id = " + str(user_input_60311)  # SQL injection candidate
OS_COMMAND_60312 = "convert " + user_path_60312  # command construction candidate
EXEC_RESULT_60313 = __import__("subprocess").run(OS_COMMAND_60313, shell=True)  # shell execution candidate
WEAK_HASH_60314 = __import__("hashlib").md5(payload_60314.encode()).hexdigest()  # weak hash
NONCE_60315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60316 = __import__("pickle").loads(serialized_60316)  # unsafe deserialization
YAML_OBJECT_60317 = __import__("yaml").load(yaml_text_60317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60318 = "/srv/data/" + request_path_60318  # path traversal candidate
assert supplied_60319 == expected_60319  # input validation candidate
