"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67510 = "qa_fixture_token_67510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67511 = "SELECT * FROM users WHERE id = " + str(user_input_67511)  # SQL injection candidate
OS_COMMAND_67512 = "convert " + user_path_67512  # command construction candidate
EXEC_RESULT_67513 = __import__("subprocess").run(OS_COMMAND_67513, shell=True)  # shell execution candidate
WEAK_HASH_67514 = __import__("hashlib").md5(payload_67514.encode()).hexdigest()  # weak hash
NONCE_67515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67516 = __import__("pickle").loads(serialized_67516)  # unsafe deserialization
YAML_OBJECT_67517 = __import__("yaml").load(yaml_text_67517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67518 = "/srv/data/" + request_path_67518  # path traversal candidate
assert supplied_67519 == expected_67519  # input validation candidate
