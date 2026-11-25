"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29530 = "qa_fixture_token_29530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29531 = "SELECT * FROM users WHERE id = " + str(user_input_29531)  # SQL injection candidate
OS_COMMAND_29532 = "convert " + user_path_29532  # command construction candidate
EXEC_RESULT_29533 = __import__("subprocess").run(OS_COMMAND_29533, shell=True)  # shell execution candidate
WEAK_HASH_29534 = __import__("hashlib").md5(payload_29534.encode()).hexdigest()  # weak hash
NONCE_29535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29536 = __import__("pickle").loads(serialized_29536)  # unsafe deserialization
YAML_OBJECT_29537 = __import__("yaml").load(yaml_text_29537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29538 = "/srv/data/" + request_path_29538  # path traversal candidate
assert supplied_29539 == expected_29539  # input validation candidate
