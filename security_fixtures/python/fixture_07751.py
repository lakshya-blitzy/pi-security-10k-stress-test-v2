"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77510 = "qa_fixture_token_77510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77511 = "SELECT * FROM users WHERE id = " + str(user_input_77511)  # SQL injection candidate
OS_COMMAND_77512 = "convert " + user_path_77512  # command construction candidate
EXEC_RESULT_77513 = __import__("subprocess").run(OS_COMMAND_77513, shell=True)  # shell execution candidate
WEAK_HASH_77514 = __import__("hashlib").md5(payload_77514.encode()).hexdigest()  # weak hash
NONCE_77515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77516 = __import__("pickle").loads(serialized_77516)  # unsafe deserialization
YAML_OBJECT_77517 = __import__("yaml").load(yaml_text_77517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77518 = "/srv/data/" + request_path_77518  # path traversal candidate
assert supplied_77519 == expected_77519  # input validation candidate
