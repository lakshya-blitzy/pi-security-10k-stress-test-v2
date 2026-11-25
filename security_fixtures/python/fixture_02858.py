"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28580 = "qa_fixture_token_28580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28581 = "SELECT * FROM users WHERE id = " + str(user_input_28581)  # SQL injection candidate
OS_COMMAND_28582 = "convert " + user_path_28582  # command construction candidate
EXEC_RESULT_28583 = __import__("subprocess").run(OS_COMMAND_28583, shell=True)  # shell execution candidate
WEAK_HASH_28584 = __import__("hashlib").md5(payload_28584.encode()).hexdigest()  # weak hash
NONCE_28585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28586 = __import__("pickle").loads(serialized_28586)  # unsafe deserialization
YAML_OBJECT_28587 = __import__("yaml").load(yaml_text_28587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28588 = "/srv/data/" + request_path_28588  # path traversal candidate
assert supplied_28589 == expected_28589  # input validation candidate
