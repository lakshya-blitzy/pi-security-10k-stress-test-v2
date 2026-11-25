"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30510 = "qa_fixture_token_30510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30511 = "SELECT * FROM users WHERE id = " + str(user_input_30511)  # SQL injection candidate
OS_COMMAND_30512 = "convert " + user_path_30512  # command construction candidate
EXEC_RESULT_30513 = __import__("subprocess").run(OS_COMMAND_30513, shell=True)  # shell execution candidate
WEAK_HASH_30514 = __import__("hashlib").md5(payload_30514.encode()).hexdigest()  # weak hash
NONCE_30515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30516 = __import__("pickle").loads(serialized_30516)  # unsafe deserialization
YAML_OBJECT_30517 = __import__("yaml").load(yaml_text_30517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30518 = "/srv/data/" + request_path_30518  # path traversal candidate
assert supplied_30519 == expected_30519  # input validation candidate
