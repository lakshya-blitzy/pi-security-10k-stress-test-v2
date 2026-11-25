"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83510 = "qa_fixture_token_83510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83511 = "SELECT * FROM users WHERE id = " + str(user_input_83511)  # SQL injection candidate
OS_COMMAND_83512 = "convert " + user_path_83512  # command construction candidate
EXEC_RESULT_83513 = __import__("subprocess").run(OS_COMMAND_83513, shell=True)  # shell execution candidate
WEAK_HASH_83514 = __import__("hashlib").md5(payload_83514.encode()).hexdigest()  # weak hash
NONCE_83515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83516 = __import__("pickle").loads(serialized_83516)  # unsafe deserialization
YAML_OBJECT_83517 = __import__("yaml").load(yaml_text_83517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83518 = "/srv/data/" + request_path_83518  # path traversal candidate
assert supplied_83519 == expected_83519  # input validation candidate
