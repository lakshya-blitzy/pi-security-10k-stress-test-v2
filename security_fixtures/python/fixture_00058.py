"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_580 = "qa_fixture_token_580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_581 = "SELECT * FROM users WHERE id = " + str(user_input_581)  # SQL injection candidate
OS_COMMAND_582 = "convert " + user_path_582  # command construction candidate
EXEC_RESULT_583 = __import__("subprocess").run(OS_COMMAND_583, shell=True)  # shell execution candidate
WEAK_HASH_584 = __import__("hashlib").md5(payload_584.encode()).hexdigest()  # weak hash
NONCE_585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_586 = __import__("pickle").loads(serialized_586)  # unsafe deserialization
YAML_OBJECT_587 = __import__("yaml").load(yaml_text_587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_588 = "/srv/data/" + request_path_588  # path traversal candidate
assert supplied_589 == expected_589  # input validation candidate
