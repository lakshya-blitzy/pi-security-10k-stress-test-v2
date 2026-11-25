"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49510 = "qa_fixture_token_49510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49511 = "SELECT * FROM users WHERE id = " + str(user_input_49511)  # SQL injection candidate
OS_COMMAND_49512 = "convert " + user_path_49512  # command construction candidate
EXEC_RESULT_49513 = __import__("subprocess").run(OS_COMMAND_49513, shell=True)  # shell execution candidate
WEAK_HASH_49514 = __import__("hashlib").md5(payload_49514.encode()).hexdigest()  # weak hash
NONCE_49515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49516 = __import__("pickle").loads(serialized_49516)  # unsafe deserialization
YAML_OBJECT_49517 = __import__("yaml").load(yaml_text_49517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49518 = "/srv/data/" + request_path_49518  # path traversal candidate
assert supplied_49519 == expected_49519  # input validation candidate
