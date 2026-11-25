"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27580 = "qa_fixture_token_27580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27581 = "SELECT * FROM users WHERE id = " + str(user_input_27581)  # SQL injection candidate
OS_COMMAND_27582 = "convert " + user_path_27582  # command construction candidate
EXEC_RESULT_27583 = __import__("subprocess").run(OS_COMMAND_27583, shell=True)  # shell execution candidate
WEAK_HASH_27584 = __import__("hashlib").md5(payload_27584.encode()).hexdigest()  # weak hash
NONCE_27585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27586 = __import__("pickle").loads(serialized_27586)  # unsafe deserialization
YAML_OBJECT_27587 = __import__("yaml").load(yaml_text_27587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27588 = "/srv/data/" + request_path_27588  # path traversal candidate
assert supplied_27589 == expected_27589  # input validation candidate
