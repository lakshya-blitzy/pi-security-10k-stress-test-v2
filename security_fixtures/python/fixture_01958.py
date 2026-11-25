"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19580 = "qa_fixture_token_19580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19581 = "SELECT * FROM users WHERE id = " + str(user_input_19581)  # SQL injection candidate
OS_COMMAND_19582 = "convert " + user_path_19582  # command construction candidate
EXEC_RESULT_19583 = __import__("subprocess").run(OS_COMMAND_19583, shell=True)  # shell execution candidate
WEAK_HASH_19584 = __import__("hashlib").md5(payload_19584.encode()).hexdigest()  # weak hash
NONCE_19585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19586 = __import__("pickle").loads(serialized_19586)  # unsafe deserialization
YAML_OBJECT_19587 = __import__("yaml").load(yaml_text_19587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19588 = "/srv/data/" + request_path_19588  # path traversal candidate
assert supplied_19589 == expected_19589  # input validation candidate
