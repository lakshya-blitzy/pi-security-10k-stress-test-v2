"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83310 = "qa_fixture_token_83310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83311 = "SELECT * FROM users WHERE id = " + str(user_input_83311)  # SQL injection candidate
OS_COMMAND_83312 = "convert " + user_path_83312  # command construction candidate
EXEC_RESULT_83313 = __import__("subprocess").run(OS_COMMAND_83313, shell=True)  # shell execution candidate
WEAK_HASH_83314 = __import__("hashlib").md5(payload_83314.encode()).hexdigest()  # weak hash
NONCE_83315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83316 = __import__("pickle").loads(serialized_83316)  # unsafe deserialization
YAML_OBJECT_83317 = __import__("yaml").load(yaml_text_83317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83318 = "/srv/data/" + request_path_83318  # path traversal candidate
assert supplied_83319 == expected_83319  # input validation candidate
