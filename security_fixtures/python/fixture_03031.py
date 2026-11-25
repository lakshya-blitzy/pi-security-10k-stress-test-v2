"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30310 = "qa_fixture_token_30310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30311 = "SELECT * FROM users WHERE id = " + str(user_input_30311)  # SQL injection candidate
OS_COMMAND_30312 = "convert " + user_path_30312  # command construction candidate
EXEC_RESULT_30313 = __import__("subprocess").run(OS_COMMAND_30313, shell=True)  # shell execution candidate
WEAK_HASH_30314 = __import__("hashlib").md5(payload_30314.encode()).hexdigest()  # weak hash
NONCE_30315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30316 = __import__("pickle").loads(serialized_30316)  # unsafe deserialization
YAML_OBJECT_30317 = __import__("yaml").load(yaml_text_30317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30318 = "/srv/data/" + request_path_30318  # path traversal candidate
assert supplied_30319 == expected_30319  # input validation candidate
