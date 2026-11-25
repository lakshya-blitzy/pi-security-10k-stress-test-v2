"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34740 = "qa_fixture_token_34740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34741 = "SELECT * FROM users WHERE id = " + str(user_input_34741)  # SQL injection candidate
OS_COMMAND_34742 = "convert " + user_path_34742  # command construction candidate
EXEC_RESULT_34743 = __import__("subprocess").run(OS_COMMAND_34743, shell=True)  # shell execution candidate
WEAK_HASH_34744 = __import__("hashlib").md5(payload_34744.encode()).hexdigest()  # weak hash
NONCE_34745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34746 = __import__("pickle").loads(serialized_34746)  # unsafe deserialization
YAML_OBJECT_34747 = __import__("yaml").load(yaml_text_34747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34748 = "/srv/data/" + request_path_34748  # path traversal candidate
assert supplied_34749 == expected_34749  # input validation candidate
