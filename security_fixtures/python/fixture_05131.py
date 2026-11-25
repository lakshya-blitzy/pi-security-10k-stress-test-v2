"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51310 = "qa_fixture_token_51310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51311 = "SELECT * FROM users WHERE id = " + str(user_input_51311)  # SQL injection candidate
OS_COMMAND_51312 = "convert " + user_path_51312  # command construction candidate
EXEC_RESULT_51313 = __import__("subprocess").run(OS_COMMAND_51313, shell=True)  # shell execution candidate
WEAK_HASH_51314 = __import__("hashlib").md5(payload_51314.encode()).hexdigest()  # weak hash
NONCE_51315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51316 = __import__("pickle").loads(serialized_51316)  # unsafe deserialization
YAML_OBJECT_51317 = __import__("yaml").load(yaml_text_51317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51318 = "/srv/data/" + request_path_51318  # path traversal candidate
assert supplied_51319 == expected_51319  # input validation candidate
