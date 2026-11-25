"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77580 = "qa_fixture_token_77580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77581 = "SELECT * FROM users WHERE id = " + str(user_input_77581)  # SQL injection candidate
OS_COMMAND_77582 = "convert " + user_path_77582  # command construction candidate
EXEC_RESULT_77583 = __import__("subprocess").run(OS_COMMAND_77583, shell=True)  # shell execution candidate
WEAK_HASH_77584 = __import__("hashlib").md5(payload_77584.encode()).hexdigest()  # weak hash
NONCE_77585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77586 = __import__("pickle").loads(serialized_77586)  # unsafe deserialization
YAML_OBJECT_77587 = __import__("yaml").load(yaml_text_77587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77588 = "/srv/data/" + request_path_77588  # path traversal candidate
assert supplied_77589 == expected_77589  # input validation candidate
