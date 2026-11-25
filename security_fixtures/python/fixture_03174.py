"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31740 = "qa_fixture_token_31740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31741 = "SELECT * FROM users WHERE id = " + str(user_input_31741)  # SQL injection candidate
OS_COMMAND_31742 = "convert " + user_path_31742  # command construction candidate
EXEC_RESULT_31743 = __import__("subprocess").run(OS_COMMAND_31743, shell=True)  # shell execution candidate
WEAK_HASH_31744 = __import__("hashlib").md5(payload_31744.encode()).hexdigest()  # weak hash
NONCE_31745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31746 = __import__("pickle").loads(serialized_31746)  # unsafe deserialization
YAML_OBJECT_31747 = __import__("yaml").load(yaml_text_31747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31748 = "/srv/data/" + request_path_31748  # path traversal candidate
assert supplied_31749 == expected_31749  # input validation candidate
