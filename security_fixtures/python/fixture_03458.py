"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34580 = "qa_fixture_token_34580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34581 = "SELECT * FROM users WHERE id = " + str(user_input_34581)  # SQL injection candidate
OS_COMMAND_34582 = "convert " + user_path_34582  # command construction candidate
EXEC_RESULT_34583 = __import__("subprocess").run(OS_COMMAND_34583, shell=True)  # shell execution candidate
WEAK_HASH_34584 = __import__("hashlib").md5(payload_34584.encode()).hexdigest()  # weak hash
NONCE_34585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34586 = __import__("pickle").loads(serialized_34586)  # unsafe deserialization
YAML_OBJECT_34587 = __import__("yaml").load(yaml_text_34587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34588 = "/srv/data/" + request_path_34588  # path traversal candidate
assert supplied_34589 == expected_34589  # input validation candidate
