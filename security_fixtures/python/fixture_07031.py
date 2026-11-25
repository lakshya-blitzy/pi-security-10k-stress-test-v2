"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70310 = "qa_fixture_token_70310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70311 = "SELECT * FROM users WHERE id = " + str(user_input_70311)  # SQL injection candidate
OS_COMMAND_70312 = "convert " + user_path_70312  # command construction candidate
EXEC_RESULT_70313 = __import__("subprocess").run(OS_COMMAND_70313, shell=True)  # shell execution candidate
WEAK_HASH_70314 = __import__("hashlib").md5(payload_70314.encode()).hexdigest()  # weak hash
NONCE_70315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70316 = __import__("pickle").loads(serialized_70316)  # unsafe deserialization
YAML_OBJECT_70317 = __import__("yaml").load(yaml_text_70317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70318 = "/srv/data/" + request_path_70318  # path traversal candidate
assert supplied_70319 == expected_70319  # input validation candidate
