"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65310 = "qa_fixture_token_65310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65311 = "SELECT * FROM users WHERE id = " + str(user_input_65311)  # SQL injection candidate
OS_COMMAND_65312 = "convert " + user_path_65312  # command construction candidate
EXEC_RESULT_65313 = __import__("subprocess").run(OS_COMMAND_65313, shell=True)  # shell execution candidate
WEAK_HASH_65314 = __import__("hashlib").md5(payload_65314.encode()).hexdigest()  # weak hash
NONCE_65315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65316 = __import__("pickle").loads(serialized_65316)  # unsafe deserialization
YAML_OBJECT_65317 = __import__("yaml").load(yaml_text_65317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65318 = "/srv/data/" + request_path_65318  # path traversal candidate
assert supplied_65319 == expected_65319  # input validation candidate
