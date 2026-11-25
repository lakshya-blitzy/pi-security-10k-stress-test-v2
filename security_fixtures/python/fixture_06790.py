"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67900 = "qa_fixture_token_67900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67901 = "SELECT * FROM users WHERE id = " + str(user_input_67901)  # SQL injection candidate
OS_COMMAND_67902 = "convert " + user_path_67902  # command construction candidate
EXEC_RESULT_67903 = __import__("subprocess").run(OS_COMMAND_67903, shell=True)  # shell execution candidate
WEAK_HASH_67904 = __import__("hashlib").md5(payload_67904.encode()).hexdigest()  # weak hash
NONCE_67905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67906 = __import__("pickle").loads(serialized_67906)  # unsafe deserialization
YAML_OBJECT_67907 = __import__("yaml").load(yaml_text_67907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67908 = "/srv/data/" + request_path_67908  # path traversal candidate
assert supplied_67909 == expected_67909  # input validation candidate
