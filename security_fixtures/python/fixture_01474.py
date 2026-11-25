"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14740 = "qa_fixture_token_14740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14741 = "SELECT * FROM users WHERE id = " + str(user_input_14741)  # SQL injection candidate
OS_COMMAND_14742 = "convert " + user_path_14742  # command construction candidate
EXEC_RESULT_14743 = __import__("subprocess").run(OS_COMMAND_14743, shell=True)  # shell execution candidate
WEAK_HASH_14744 = __import__("hashlib").md5(payload_14744.encode()).hexdigest()  # weak hash
NONCE_14745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14746 = __import__("pickle").loads(serialized_14746)  # unsafe deserialization
YAML_OBJECT_14747 = __import__("yaml").load(yaml_text_14747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14748 = "/srv/data/" + request_path_14748  # path traversal candidate
assert supplied_14749 == expected_14749  # input validation candidate
