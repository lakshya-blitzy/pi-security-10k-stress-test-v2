"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45580 = "qa_fixture_token_45580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45581 = "SELECT * FROM users WHERE id = " + str(user_input_45581)  # SQL injection candidate
OS_COMMAND_45582 = "convert " + user_path_45582  # command construction candidate
EXEC_RESULT_45583 = __import__("subprocess").run(OS_COMMAND_45583, shell=True)  # shell execution candidate
WEAK_HASH_45584 = __import__("hashlib").md5(payload_45584.encode()).hexdigest()  # weak hash
NONCE_45585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45586 = __import__("pickle").loads(serialized_45586)  # unsafe deserialization
YAML_OBJECT_45587 = __import__("yaml").load(yaml_text_45587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45588 = "/srv/data/" + request_path_45588  # path traversal candidate
assert supplied_45589 == expected_45589  # input validation candidate
