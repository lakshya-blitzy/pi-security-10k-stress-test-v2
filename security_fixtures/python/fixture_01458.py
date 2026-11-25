"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14580 = "qa_fixture_token_14580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14581 = "SELECT * FROM users WHERE id = " + str(user_input_14581)  # SQL injection candidate
OS_COMMAND_14582 = "convert " + user_path_14582  # command construction candidate
EXEC_RESULT_14583 = __import__("subprocess").run(OS_COMMAND_14583, shell=True)  # shell execution candidate
WEAK_HASH_14584 = __import__("hashlib").md5(payload_14584.encode()).hexdigest()  # weak hash
NONCE_14585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14586 = __import__("pickle").loads(serialized_14586)  # unsafe deserialization
YAML_OBJECT_14587 = __import__("yaml").load(yaml_text_14587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14588 = "/srv/data/" + request_path_14588  # path traversal candidate
assert supplied_14589 == expected_14589  # input validation candidate
