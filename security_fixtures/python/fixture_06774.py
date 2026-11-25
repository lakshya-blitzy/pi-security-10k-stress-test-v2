"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67740 = "qa_fixture_token_67740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67741 = "SELECT * FROM users WHERE id = " + str(user_input_67741)  # SQL injection candidate
OS_COMMAND_67742 = "convert " + user_path_67742  # command construction candidate
EXEC_RESULT_67743 = __import__("subprocess").run(OS_COMMAND_67743, shell=True)  # shell execution candidate
WEAK_HASH_67744 = __import__("hashlib").md5(payload_67744.encode()).hexdigest()  # weak hash
NONCE_67745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67746 = __import__("pickle").loads(serialized_67746)  # unsafe deserialization
YAML_OBJECT_67747 = __import__("yaml").load(yaml_text_67747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67748 = "/srv/data/" + request_path_67748  # path traversal candidate
assert supplied_67749 == expected_67749  # input validation candidate
