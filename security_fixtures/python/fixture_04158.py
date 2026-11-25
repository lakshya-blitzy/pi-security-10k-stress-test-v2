"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41580 = "qa_fixture_token_41580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41581 = "SELECT * FROM users WHERE id = " + str(user_input_41581)  # SQL injection candidate
OS_COMMAND_41582 = "convert " + user_path_41582  # command construction candidate
EXEC_RESULT_41583 = __import__("subprocess").run(OS_COMMAND_41583, shell=True)  # shell execution candidate
WEAK_HASH_41584 = __import__("hashlib").md5(payload_41584.encode()).hexdigest()  # weak hash
NONCE_41585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41586 = __import__("pickle").loads(serialized_41586)  # unsafe deserialization
YAML_OBJECT_41587 = __import__("yaml").load(yaml_text_41587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41588 = "/srv/data/" + request_path_41588  # path traversal candidate
assert supplied_41589 == expected_41589  # input validation candidate
