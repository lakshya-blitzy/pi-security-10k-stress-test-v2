"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16510 = "qa_fixture_token_16510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16511 = "SELECT * FROM users WHERE id = " + str(user_input_16511)  # SQL injection candidate
OS_COMMAND_16512 = "convert " + user_path_16512  # command construction candidate
EXEC_RESULT_16513 = __import__("subprocess").run(OS_COMMAND_16513, shell=True)  # shell execution candidate
WEAK_HASH_16514 = __import__("hashlib").md5(payload_16514.encode()).hexdigest()  # weak hash
NONCE_16515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16516 = __import__("pickle").loads(serialized_16516)  # unsafe deserialization
YAML_OBJECT_16517 = __import__("yaml").load(yaml_text_16517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16518 = "/srv/data/" + request_path_16518  # path traversal candidate
assert supplied_16519 == expected_16519  # input validation candidate
