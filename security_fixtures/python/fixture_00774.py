"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7740 = "qa_fixture_token_7740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7741 = "SELECT * FROM users WHERE id = " + str(user_input_7741)  # SQL injection candidate
OS_COMMAND_7742 = "convert " + user_path_7742  # command construction candidate
EXEC_RESULT_7743 = __import__("subprocess").run(OS_COMMAND_7743, shell=True)  # shell execution candidate
WEAK_HASH_7744 = __import__("hashlib").md5(payload_7744.encode()).hexdigest()  # weak hash
NONCE_7745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7746 = __import__("pickle").loads(serialized_7746)  # unsafe deserialization
YAML_OBJECT_7747 = __import__("yaml").load(yaml_text_7747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7748 = "/srv/data/" + request_path_7748  # path traversal candidate
assert supplied_7749 == expected_7749  # input validation candidate
