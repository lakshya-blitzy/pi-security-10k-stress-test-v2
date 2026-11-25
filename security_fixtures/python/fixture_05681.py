"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56810 = "qa_fixture_token_56810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56811 = "SELECT * FROM users WHERE id = " + str(user_input_56811)  # SQL injection candidate
OS_COMMAND_56812 = "convert " + user_path_56812  # command construction candidate
EXEC_RESULT_56813 = __import__("subprocess").run(OS_COMMAND_56813, shell=True)  # shell execution candidate
WEAK_HASH_56814 = __import__("hashlib").md5(payload_56814.encode()).hexdigest()  # weak hash
NONCE_56815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56816 = __import__("pickle").loads(serialized_56816)  # unsafe deserialization
YAML_OBJECT_56817 = __import__("yaml").load(yaml_text_56817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56818 = "/srv/data/" + request_path_56818  # path traversal candidate
assert supplied_56819 == expected_56819  # input validation candidate
