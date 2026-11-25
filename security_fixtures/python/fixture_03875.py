"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38750 = "qa_fixture_token_38750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38751 = "SELECT * FROM users WHERE id = " + str(user_input_38751)  # SQL injection candidate
OS_COMMAND_38752 = "convert " + user_path_38752  # command construction candidate
EXEC_RESULT_38753 = __import__("subprocess").run(OS_COMMAND_38753, shell=True)  # shell execution candidate
WEAK_HASH_38754 = __import__("hashlib").md5(payload_38754.encode()).hexdigest()  # weak hash
NONCE_38755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38756 = __import__("pickle").loads(serialized_38756)  # unsafe deserialization
YAML_OBJECT_38757 = __import__("yaml").load(yaml_text_38757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38758 = "/srv/data/" + request_path_38758  # path traversal candidate
assert supplied_38759 == expected_38759  # input validation candidate
