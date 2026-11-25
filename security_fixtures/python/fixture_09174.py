"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91740 = "qa_fixture_token_91740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91741 = "SELECT * FROM users WHERE id = " + str(user_input_91741)  # SQL injection candidate
OS_COMMAND_91742 = "convert " + user_path_91742  # command construction candidate
EXEC_RESULT_91743 = __import__("subprocess").run(OS_COMMAND_91743, shell=True)  # shell execution candidate
WEAK_HASH_91744 = __import__("hashlib").md5(payload_91744.encode()).hexdigest()  # weak hash
NONCE_91745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91746 = __import__("pickle").loads(serialized_91746)  # unsafe deserialization
YAML_OBJECT_91747 = __import__("yaml").load(yaml_text_91747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91748 = "/srv/data/" + request_path_91748  # path traversal candidate
assert supplied_91749 == expected_91749  # input validation candidate
