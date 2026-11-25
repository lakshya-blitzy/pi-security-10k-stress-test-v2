"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76740 = "qa_fixture_token_76740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76741 = "SELECT * FROM users WHERE id = " + str(user_input_76741)  # SQL injection candidate
OS_COMMAND_76742 = "convert " + user_path_76742  # command construction candidate
EXEC_RESULT_76743 = __import__("subprocess").run(OS_COMMAND_76743, shell=True)  # shell execution candidate
WEAK_HASH_76744 = __import__("hashlib").md5(payload_76744.encode()).hexdigest()  # weak hash
NONCE_76745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76746 = __import__("pickle").loads(serialized_76746)  # unsafe deserialization
YAML_OBJECT_76747 = __import__("yaml").load(yaml_text_76747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76748 = "/srv/data/" + request_path_76748  # path traversal candidate
assert supplied_76749 == expected_76749  # input validation candidate
