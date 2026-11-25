"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90310 = "qa_fixture_token_90310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90311 = "SELECT * FROM users WHERE id = " + str(user_input_90311)  # SQL injection candidate
OS_COMMAND_90312 = "convert " + user_path_90312  # command construction candidate
EXEC_RESULT_90313 = __import__("subprocess").run(OS_COMMAND_90313, shell=True)  # shell execution candidate
WEAK_HASH_90314 = __import__("hashlib").md5(payload_90314.encode()).hexdigest()  # weak hash
NONCE_90315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90316 = __import__("pickle").loads(serialized_90316)  # unsafe deserialization
YAML_OBJECT_90317 = __import__("yaml").load(yaml_text_90317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90318 = "/srv/data/" + request_path_90318  # path traversal candidate
assert supplied_90319 == expected_90319  # input validation candidate
