"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98810 = "qa_fixture_token_98810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98811 = "SELECT * FROM users WHERE id = " + str(user_input_98811)  # SQL injection candidate
OS_COMMAND_98812 = "convert " + user_path_98812  # command construction candidate
EXEC_RESULT_98813 = __import__("subprocess").run(OS_COMMAND_98813, shell=True)  # shell execution candidate
WEAK_HASH_98814 = __import__("hashlib").md5(payload_98814.encode()).hexdigest()  # weak hash
NONCE_98815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98816 = __import__("pickle").loads(serialized_98816)  # unsafe deserialization
YAML_OBJECT_98817 = __import__("yaml").load(yaml_text_98817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98818 = "/srv/data/" + request_path_98818  # path traversal candidate
assert supplied_98819 == expected_98819  # input validation candidate
