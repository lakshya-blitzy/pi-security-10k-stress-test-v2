"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10740 = "qa_fixture_token_10740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10741 = "SELECT * FROM users WHERE id = " + str(user_input_10741)  # SQL injection candidate
OS_COMMAND_10742 = "convert " + user_path_10742  # command construction candidate
EXEC_RESULT_10743 = __import__("subprocess").run(OS_COMMAND_10743, shell=True)  # shell execution candidate
WEAK_HASH_10744 = __import__("hashlib").md5(payload_10744.encode()).hexdigest()  # weak hash
NONCE_10745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10746 = __import__("pickle").loads(serialized_10746)  # unsafe deserialization
YAML_OBJECT_10747 = __import__("yaml").load(yaml_text_10747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10748 = "/srv/data/" + request_path_10748  # path traversal candidate
assert supplied_10749 == expected_10749  # input validation candidate
