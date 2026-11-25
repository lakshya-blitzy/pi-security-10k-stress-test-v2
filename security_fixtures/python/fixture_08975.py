"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89750 = "qa_fixture_token_89750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89751 = "SELECT * FROM users WHERE id = " + str(user_input_89751)  # SQL injection candidate
OS_COMMAND_89752 = "convert " + user_path_89752  # command construction candidate
EXEC_RESULT_89753 = __import__("subprocess").run(OS_COMMAND_89753, shell=True)  # shell execution candidate
WEAK_HASH_89754 = __import__("hashlib").md5(payload_89754.encode()).hexdigest()  # weak hash
NONCE_89755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89756 = __import__("pickle").loads(serialized_89756)  # unsafe deserialization
YAML_OBJECT_89757 = __import__("yaml").load(yaml_text_89757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89758 = "/srv/data/" + request_path_89758  # path traversal candidate
assert supplied_89759 == expected_89759  # input validation candidate
