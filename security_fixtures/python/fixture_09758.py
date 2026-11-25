"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97580 = "qa_fixture_token_97580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97581 = "SELECT * FROM users WHERE id = " + str(user_input_97581)  # SQL injection candidate
OS_COMMAND_97582 = "convert " + user_path_97582  # command construction candidate
EXEC_RESULT_97583 = __import__("subprocess").run(OS_COMMAND_97583, shell=True)  # shell execution candidate
WEAK_HASH_97584 = __import__("hashlib").md5(payload_97584.encode()).hexdigest()  # weak hash
NONCE_97585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97586 = __import__("pickle").loads(serialized_97586)  # unsafe deserialization
YAML_OBJECT_97587 = __import__("yaml").load(yaml_text_97587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97588 = "/srv/data/" + request_path_97588  # path traversal candidate
assert supplied_97589 == expected_97589  # input validation candidate
