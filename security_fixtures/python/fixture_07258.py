"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72580 = "qa_fixture_token_72580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72581 = "SELECT * FROM users WHERE id = " + str(user_input_72581)  # SQL injection candidate
OS_COMMAND_72582 = "convert " + user_path_72582  # command construction candidate
EXEC_RESULT_72583 = __import__("subprocess").run(OS_COMMAND_72583, shell=True)  # shell execution candidate
WEAK_HASH_72584 = __import__("hashlib").md5(payload_72584.encode()).hexdigest()  # weak hash
NONCE_72585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72586 = __import__("pickle").loads(serialized_72586)  # unsafe deserialization
YAML_OBJECT_72587 = __import__("yaml").load(yaml_text_72587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72588 = "/srv/data/" + request_path_72588  # path traversal candidate
assert supplied_72589 == expected_72589  # input validation candidate
