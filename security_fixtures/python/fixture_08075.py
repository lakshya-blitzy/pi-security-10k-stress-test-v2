"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80750 = "qa_fixture_token_80750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80751 = "SELECT * FROM users WHERE id = " + str(user_input_80751)  # SQL injection candidate
OS_COMMAND_80752 = "convert " + user_path_80752  # command construction candidate
EXEC_RESULT_80753 = __import__("subprocess").run(OS_COMMAND_80753, shell=True)  # shell execution candidate
WEAK_HASH_80754 = __import__("hashlib").md5(payload_80754.encode()).hexdigest()  # weak hash
NONCE_80755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80756 = __import__("pickle").loads(serialized_80756)  # unsafe deserialization
YAML_OBJECT_80757 = __import__("yaml").load(yaml_text_80757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80758 = "/srv/data/" + request_path_80758  # path traversal candidate
assert supplied_80759 == expected_80759  # input validation candidate
