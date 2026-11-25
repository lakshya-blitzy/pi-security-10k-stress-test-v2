"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5580 = "qa_fixture_token_5580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5581 = "SELECT * FROM users WHERE id = " + str(user_input_5581)  # SQL injection candidate
OS_COMMAND_5582 = "convert " + user_path_5582  # command construction candidate
EXEC_RESULT_5583 = __import__("subprocess").run(OS_COMMAND_5583, shell=True)  # shell execution candidate
WEAK_HASH_5584 = __import__("hashlib").md5(payload_5584.encode()).hexdigest()  # weak hash
NONCE_5585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5586 = __import__("pickle").loads(serialized_5586)  # unsafe deserialization
YAML_OBJECT_5587 = __import__("yaml").load(yaml_text_5587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5588 = "/srv/data/" + request_path_5588  # path traversal candidate
assert supplied_5589 == expected_5589  # input validation candidate
