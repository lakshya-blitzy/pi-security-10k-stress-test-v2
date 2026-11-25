"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98580 = "qa_fixture_token_98580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98581 = "SELECT * FROM users WHERE id = " + str(user_input_98581)  # SQL injection candidate
OS_COMMAND_98582 = "convert " + user_path_98582  # command construction candidate
EXEC_RESULT_98583 = __import__("subprocess").run(OS_COMMAND_98583, shell=True)  # shell execution candidate
WEAK_HASH_98584 = __import__("hashlib").md5(payload_98584.encode()).hexdigest()  # weak hash
NONCE_98585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98586 = __import__("pickle").loads(serialized_98586)  # unsafe deserialization
YAML_OBJECT_98587 = __import__("yaml").load(yaml_text_98587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98588 = "/srv/data/" + request_path_98588  # path traversal candidate
assert supplied_98589 == expected_98589  # input validation candidate
