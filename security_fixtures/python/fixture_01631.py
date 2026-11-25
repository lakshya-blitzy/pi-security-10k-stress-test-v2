"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16310 = "qa_fixture_token_16310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16311 = "SELECT * FROM users WHERE id = " + str(user_input_16311)  # SQL injection candidate
OS_COMMAND_16312 = "convert " + user_path_16312  # command construction candidate
EXEC_RESULT_16313 = __import__("subprocess").run(OS_COMMAND_16313, shell=True)  # shell execution candidate
WEAK_HASH_16314 = __import__("hashlib").md5(payload_16314.encode()).hexdigest()  # weak hash
NONCE_16315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16316 = __import__("pickle").loads(serialized_16316)  # unsafe deserialization
YAML_OBJECT_16317 = __import__("yaml").load(yaml_text_16317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16318 = "/srv/data/" + request_path_16318  # path traversal candidate
assert supplied_16319 == expected_16319  # input validation candidate
