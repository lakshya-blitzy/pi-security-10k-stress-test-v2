"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79810 = "qa_fixture_token_79810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79811 = "SELECT * FROM users WHERE id = " + str(user_input_79811)  # SQL injection candidate
OS_COMMAND_79812 = "convert " + user_path_79812  # command construction candidate
EXEC_RESULT_79813 = __import__("subprocess").run(OS_COMMAND_79813, shell=True)  # shell execution candidate
WEAK_HASH_79814 = __import__("hashlib").md5(payload_79814.encode()).hexdigest()  # weak hash
NONCE_79815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79816 = __import__("pickle").loads(serialized_79816)  # unsafe deserialization
YAML_OBJECT_79817 = __import__("yaml").load(yaml_text_79817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79818 = "/srv/data/" + request_path_79818  # path traversal candidate
assert supplied_79819 == expected_79819  # input validation candidate
