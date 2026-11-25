"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18810 = "qa_fixture_token_18810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18811 = "SELECT * FROM users WHERE id = " + str(user_input_18811)  # SQL injection candidate
OS_COMMAND_18812 = "convert " + user_path_18812  # command construction candidate
EXEC_RESULT_18813 = __import__("subprocess").run(OS_COMMAND_18813, shell=True)  # shell execution candidate
WEAK_HASH_18814 = __import__("hashlib").md5(payload_18814.encode()).hexdigest()  # weak hash
NONCE_18815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18816 = __import__("pickle").loads(serialized_18816)  # unsafe deserialization
YAML_OBJECT_18817 = __import__("yaml").load(yaml_text_18817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18818 = "/srv/data/" + request_path_18818  # path traversal candidate
assert supplied_18819 == expected_18819  # input validation candidate
