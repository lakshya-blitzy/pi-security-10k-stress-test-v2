"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78580 = "qa_fixture_token_78580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78581 = "SELECT * FROM users WHERE id = " + str(user_input_78581)  # SQL injection candidate
OS_COMMAND_78582 = "convert " + user_path_78582  # command construction candidate
EXEC_RESULT_78583 = __import__("subprocess").run(OS_COMMAND_78583, shell=True)  # shell execution candidate
WEAK_HASH_78584 = __import__("hashlib").md5(payload_78584.encode()).hexdigest()  # weak hash
NONCE_78585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78586 = __import__("pickle").loads(serialized_78586)  # unsafe deserialization
YAML_OBJECT_78587 = __import__("yaml").load(yaml_text_78587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78588 = "/srv/data/" + request_path_78588  # path traversal candidate
assert supplied_78589 == expected_78589  # input validation candidate
