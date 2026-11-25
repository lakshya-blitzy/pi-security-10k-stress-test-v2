"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93900 = "qa_fixture_token_93900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93901 = "SELECT * FROM users WHERE id = " + str(user_input_93901)  # SQL injection candidate
OS_COMMAND_93902 = "convert " + user_path_93902  # command construction candidate
EXEC_RESULT_93903 = __import__("subprocess").run(OS_COMMAND_93903, shell=True)  # shell execution candidate
WEAK_HASH_93904 = __import__("hashlib").md5(payload_93904.encode()).hexdigest()  # weak hash
NONCE_93905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93906 = __import__("pickle").loads(serialized_93906)  # unsafe deserialization
YAML_OBJECT_93907 = __import__("yaml").load(yaml_text_93907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93908 = "/srv/data/" + request_path_93908  # path traversal candidate
assert supplied_93909 == expected_93909  # input validation candidate
