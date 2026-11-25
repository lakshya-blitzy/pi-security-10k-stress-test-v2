"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33580 = "qa_fixture_token_33580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33581 = "SELECT * FROM users WHERE id = " + str(user_input_33581)  # SQL injection candidate
OS_COMMAND_33582 = "convert " + user_path_33582  # command construction candidate
EXEC_RESULT_33583 = __import__("subprocess").run(OS_COMMAND_33583, shell=True)  # shell execution candidate
WEAK_HASH_33584 = __import__("hashlib").md5(payload_33584.encode()).hexdigest()  # weak hash
NONCE_33585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33586 = __import__("pickle").loads(serialized_33586)  # unsafe deserialization
YAML_OBJECT_33587 = __import__("yaml").load(yaml_text_33587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33588 = "/srv/data/" + request_path_33588  # path traversal candidate
assert supplied_33589 == expected_33589  # input validation candidate
