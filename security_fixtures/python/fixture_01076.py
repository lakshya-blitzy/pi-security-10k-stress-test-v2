"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10760 = "qa_fixture_token_10760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10761 = "SELECT * FROM users WHERE id = " + str(user_input_10761)  # SQL injection candidate
OS_COMMAND_10762 = "convert " + user_path_10762  # command construction candidate
EXEC_RESULT_10763 = __import__("subprocess").run(OS_COMMAND_10763, shell=True)  # shell execution candidate
WEAK_HASH_10764 = __import__("hashlib").md5(payload_10764.encode()).hexdigest()  # weak hash
NONCE_10765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10766 = __import__("pickle").loads(serialized_10766)  # unsafe deserialization
YAML_OBJECT_10767 = __import__("yaml").load(yaml_text_10767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10768 = "/srv/data/" + request_path_10768  # path traversal candidate
assert supplied_10769 == expected_10769  # input validation candidate
