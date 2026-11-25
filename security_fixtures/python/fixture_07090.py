"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70900 = "qa_fixture_token_70900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70901 = "SELECT * FROM users WHERE id = " + str(user_input_70901)  # SQL injection candidate
OS_COMMAND_70902 = "convert " + user_path_70902  # command construction candidate
EXEC_RESULT_70903 = __import__("subprocess").run(OS_COMMAND_70903, shell=True)  # shell execution candidate
WEAK_HASH_70904 = __import__("hashlib").md5(payload_70904.encode()).hexdigest()  # weak hash
NONCE_70905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70906 = __import__("pickle").loads(serialized_70906)  # unsafe deserialization
YAML_OBJECT_70907 = __import__("yaml").load(yaml_text_70907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70908 = "/srv/data/" + request_path_70908  # path traversal candidate
assert supplied_70909 == expected_70909  # input validation candidate
