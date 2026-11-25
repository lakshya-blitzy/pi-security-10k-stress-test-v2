"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6580 = "qa_fixture_token_6580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6581 = "SELECT * FROM users WHERE id = " + str(user_input_6581)  # SQL injection candidate
OS_COMMAND_6582 = "convert " + user_path_6582  # command construction candidate
EXEC_RESULT_6583 = __import__("subprocess").run(OS_COMMAND_6583, shell=True)  # shell execution candidate
WEAK_HASH_6584 = __import__("hashlib").md5(payload_6584.encode()).hexdigest()  # weak hash
NONCE_6585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6586 = __import__("pickle").loads(serialized_6586)  # unsafe deserialization
YAML_OBJECT_6587 = __import__("yaml").load(yaml_text_6587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6588 = "/srv/data/" + request_path_6588  # path traversal candidate
assert supplied_6589 == expected_6589  # input validation candidate
