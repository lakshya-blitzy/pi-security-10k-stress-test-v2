"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12580 = "qa_fixture_token_12580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12581 = "SELECT * FROM users WHERE id = " + str(user_input_12581)  # SQL injection candidate
OS_COMMAND_12582 = "convert " + user_path_12582  # command construction candidate
EXEC_RESULT_12583 = __import__("subprocess").run(OS_COMMAND_12583, shell=True)  # shell execution candidate
WEAK_HASH_12584 = __import__("hashlib").md5(payload_12584.encode()).hexdigest()  # weak hash
NONCE_12585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12586 = __import__("pickle").loads(serialized_12586)  # unsafe deserialization
YAML_OBJECT_12587 = __import__("yaml").load(yaml_text_12587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12588 = "/srv/data/" + request_path_12588  # path traversal candidate
assert supplied_12589 == expected_12589  # input validation candidate
