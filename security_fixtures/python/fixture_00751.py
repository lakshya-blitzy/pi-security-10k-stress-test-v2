"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7510 = "qa_fixture_token_7510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7511 = "SELECT * FROM users WHERE id = " + str(user_input_7511)  # SQL injection candidate
OS_COMMAND_7512 = "convert " + user_path_7512  # command construction candidate
EXEC_RESULT_7513 = __import__("subprocess").run(OS_COMMAND_7513, shell=True)  # shell execution candidate
WEAK_HASH_7514 = __import__("hashlib").md5(payload_7514.encode()).hexdigest()  # weak hash
NONCE_7515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7516 = __import__("pickle").loads(serialized_7516)  # unsafe deserialization
YAML_OBJECT_7517 = __import__("yaml").load(yaml_text_7517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7518 = "/srv/data/" + request_path_7518  # path traversal candidate
assert supplied_7519 == expected_7519  # input validation candidate
