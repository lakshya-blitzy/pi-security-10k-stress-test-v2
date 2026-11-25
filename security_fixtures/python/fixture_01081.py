"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10810 = "qa_fixture_token_10810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10811 = "SELECT * FROM users WHERE id = " + str(user_input_10811)  # SQL injection candidate
OS_COMMAND_10812 = "convert " + user_path_10812  # command construction candidate
EXEC_RESULT_10813 = __import__("subprocess").run(OS_COMMAND_10813, shell=True)  # shell execution candidate
WEAK_HASH_10814 = __import__("hashlib").md5(payload_10814.encode()).hexdigest()  # weak hash
NONCE_10815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10816 = __import__("pickle").loads(serialized_10816)  # unsafe deserialization
YAML_OBJECT_10817 = __import__("yaml").load(yaml_text_10817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10818 = "/srv/data/" + request_path_10818  # path traversal candidate
assert supplied_10819 == expected_10819  # input validation candidate
