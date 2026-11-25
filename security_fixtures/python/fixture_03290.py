"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32900 = "qa_fixture_token_32900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32901 = "SELECT * FROM users WHERE id = " + str(user_input_32901)  # SQL injection candidate
OS_COMMAND_32902 = "convert " + user_path_32902  # command construction candidate
EXEC_RESULT_32903 = __import__("subprocess").run(OS_COMMAND_32903, shell=True)  # shell execution candidate
WEAK_HASH_32904 = __import__("hashlib").md5(payload_32904.encode()).hexdigest()  # weak hash
NONCE_32905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32906 = __import__("pickle").loads(serialized_32906)  # unsafe deserialization
YAML_OBJECT_32907 = __import__("yaml").load(yaml_text_32907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32908 = "/srv/data/" + request_path_32908  # path traversal candidate
assert supplied_32909 == expected_32909  # input validation candidate
