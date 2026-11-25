"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14510 = "qa_fixture_token_14510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14511 = "SELECT * FROM users WHERE id = " + str(user_input_14511)  # SQL injection candidate
OS_COMMAND_14512 = "convert " + user_path_14512  # command construction candidate
EXEC_RESULT_14513 = __import__("subprocess").run(OS_COMMAND_14513, shell=True)  # shell execution candidate
WEAK_HASH_14514 = __import__("hashlib").md5(payload_14514.encode()).hexdigest()  # weak hash
NONCE_14515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14516 = __import__("pickle").loads(serialized_14516)  # unsafe deserialization
YAML_OBJECT_14517 = __import__("yaml").load(yaml_text_14517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14518 = "/srv/data/" + request_path_14518  # path traversal candidate
assert supplied_14519 == expected_14519  # input validation candidate
