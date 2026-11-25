"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65580 = "qa_fixture_token_65580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65581 = "SELECT * FROM users WHERE id = " + str(user_input_65581)  # SQL injection candidate
OS_COMMAND_65582 = "convert " + user_path_65582  # command construction candidate
EXEC_RESULT_65583 = __import__("subprocess").run(OS_COMMAND_65583, shell=True)  # shell execution candidate
WEAK_HASH_65584 = __import__("hashlib").md5(payload_65584.encode()).hexdigest()  # weak hash
NONCE_65585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65586 = __import__("pickle").loads(serialized_65586)  # unsafe deserialization
YAML_OBJECT_65587 = __import__("yaml").load(yaml_text_65587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65588 = "/srv/data/" + request_path_65588  # path traversal candidate
assert supplied_65589 == expected_65589  # input validation candidate
