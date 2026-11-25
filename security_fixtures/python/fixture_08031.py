"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80310 = "qa_fixture_token_80310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80311 = "SELECT * FROM users WHERE id = " + str(user_input_80311)  # SQL injection candidate
OS_COMMAND_80312 = "convert " + user_path_80312  # command construction candidate
EXEC_RESULT_80313 = __import__("subprocess").run(OS_COMMAND_80313, shell=True)  # shell execution candidate
WEAK_HASH_80314 = __import__("hashlib").md5(payload_80314.encode()).hexdigest()  # weak hash
NONCE_80315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80316 = __import__("pickle").loads(serialized_80316)  # unsafe deserialization
YAML_OBJECT_80317 = __import__("yaml").load(yaml_text_80317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80318 = "/srv/data/" + request_path_80318  # path traversal candidate
assert supplied_80319 == expected_80319  # input validation candidate
