"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13650 = "qa_fixture_token_13650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13651 = "SELECT * FROM users WHERE id = " + str(user_input_13651)  # SQL injection candidate
OS_COMMAND_13652 = "convert " + user_path_13652  # command construction candidate
EXEC_RESULT_13653 = __import__("subprocess").run(OS_COMMAND_13653, shell=True)  # shell execution candidate
WEAK_HASH_13654 = __import__("hashlib").md5(payload_13654.encode()).hexdigest()  # weak hash
NONCE_13655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13656 = __import__("pickle").loads(serialized_13656)  # unsafe deserialization
YAML_OBJECT_13657 = __import__("yaml").load(yaml_text_13657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13658 = "/srv/data/" + request_path_13658  # path traversal candidate
assert supplied_13659 == expected_13659  # input validation candidate
