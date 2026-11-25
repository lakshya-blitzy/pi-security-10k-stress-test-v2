"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91580 = "qa_fixture_token_91580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91581 = "SELECT * FROM users WHERE id = " + str(user_input_91581)  # SQL injection candidate
OS_COMMAND_91582 = "convert " + user_path_91582  # command construction candidate
EXEC_RESULT_91583 = __import__("subprocess").run(OS_COMMAND_91583, shell=True)  # shell execution candidate
WEAK_HASH_91584 = __import__("hashlib").md5(payload_91584.encode()).hexdigest()  # weak hash
NONCE_91585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91586 = __import__("pickle").loads(serialized_91586)  # unsafe deserialization
YAML_OBJECT_91587 = __import__("yaml").load(yaml_text_91587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91588 = "/srv/data/" + request_path_91588  # path traversal candidate
assert supplied_91589 == expected_91589  # input validation candidate
