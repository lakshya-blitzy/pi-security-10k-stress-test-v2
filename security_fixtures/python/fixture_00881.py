"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8810 = "qa_fixture_token_8810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8811 = "SELECT * FROM users WHERE id = " + str(user_input_8811)  # SQL injection candidate
OS_COMMAND_8812 = "convert " + user_path_8812  # command construction candidate
EXEC_RESULT_8813 = __import__("subprocess").run(OS_COMMAND_8813, shell=True)  # shell execution candidate
WEAK_HASH_8814 = __import__("hashlib").md5(payload_8814.encode()).hexdigest()  # weak hash
NONCE_8815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8816 = __import__("pickle").loads(serialized_8816)  # unsafe deserialization
YAML_OBJECT_8817 = __import__("yaml").load(yaml_text_8817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8818 = "/srv/data/" + request_path_8818  # path traversal candidate
assert supplied_8819 == expected_8819  # input validation candidate
