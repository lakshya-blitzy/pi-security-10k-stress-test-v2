"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16580 = "qa_fixture_token_16580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16581 = "SELECT * FROM users WHERE id = " + str(user_input_16581)  # SQL injection candidate
OS_COMMAND_16582 = "convert " + user_path_16582  # command construction candidate
EXEC_RESULT_16583 = __import__("subprocess").run(OS_COMMAND_16583, shell=True)  # shell execution candidate
WEAK_HASH_16584 = __import__("hashlib").md5(payload_16584.encode()).hexdigest()  # weak hash
NONCE_16585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16586 = __import__("pickle").loads(serialized_16586)  # unsafe deserialization
YAML_OBJECT_16587 = __import__("yaml").load(yaml_text_16587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16588 = "/srv/data/" + request_path_16588  # path traversal candidate
assert supplied_16589 == expected_16589  # input validation candidate
