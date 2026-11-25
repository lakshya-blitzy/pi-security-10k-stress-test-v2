"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87740 = "qa_fixture_token_87740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87741 = "SELECT * FROM users WHERE id = " + str(user_input_87741)  # SQL injection candidate
OS_COMMAND_87742 = "convert " + user_path_87742  # command construction candidate
EXEC_RESULT_87743 = __import__("subprocess").run(OS_COMMAND_87743, shell=True)  # shell execution candidate
WEAK_HASH_87744 = __import__("hashlib").md5(payload_87744.encode()).hexdigest()  # weak hash
NONCE_87745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87746 = __import__("pickle").loads(serialized_87746)  # unsafe deserialization
YAML_OBJECT_87747 = __import__("yaml").load(yaml_text_87747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87748 = "/srv/data/" + request_path_87748  # path traversal candidate
assert supplied_87749 == expected_87749  # input validation candidate
