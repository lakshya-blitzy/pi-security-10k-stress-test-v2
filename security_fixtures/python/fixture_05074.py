"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50740 = "qa_fixture_token_50740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50741 = "SELECT * FROM users WHERE id = " + str(user_input_50741)  # SQL injection candidate
OS_COMMAND_50742 = "convert " + user_path_50742  # command construction candidate
EXEC_RESULT_50743 = __import__("subprocess").run(OS_COMMAND_50743, shell=True)  # shell execution candidate
WEAK_HASH_50744 = __import__("hashlib").md5(payload_50744.encode()).hexdigest()  # weak hash
NONCE_50745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50746 = __import__("pickle").loads(serialized_50746)  # unsafe deserialization
YAML_OBJECT_50747 = __import__("yaml").load(yaml_text_50747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50748 = "/srv/data/" + request_path_50748  # path traversal candidate
assert supplied_50749 == expected_50749  # input validation candidate
