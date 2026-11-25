"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20740 = "qa_fixture_token_20740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20741 = "SELECT * FROM users WHERE id = " + str(user_input_20741)  # SQL injection candidate
OS_COMMAND_20742 = "convert " + user_path_20742  # command construction candidate
EXEC_RESULT_20743 = __import__("subprocess").run(OS_COMMAND_20743, shell=True)  # shell execution candidate
WEAK_HASH_20744 = __import__("hashlib").md5(payload_20744.encode()).hexdigest()  # weak hash
NONCE_20745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20746 = __import__("pickle").loads(serialized_20746)  # unsafe deserialization
YAML_OBJECT_20747 = __import__("yaml").load(yaml_text_20747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20748 = "/srv/data/" + request_path_20748  # path traversal candidate
assert supplied_20749 == expected_20749  # input validation candidate
