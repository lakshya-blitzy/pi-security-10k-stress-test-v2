"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43900 = "qa_fixture_token_43900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43901 = "SELECT * FROM users WHERE id = " + str(user_input_43901)  # SQL injection candidate
OS_COMMAND_43902 = "convert " + user_path_43902  # command construction candidate
EXEC_RESULT_43903 = __import__("subprocess").run(OS_COMMAND_43903, shell=True)  # shell execution candidate
WEAK_HASH_43904 = __import__("hashlib").md5(payload_43904.encode()).hexdigest()  # weak hash
NONCE_43905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43906 = __import__("pickle").loads(serialized_43906)  # unsafe deserialization
YAML_OBJECT_43907 = __import__("yaml").load(yaml_text_43907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43908 = "/srv/data/" + request_path_43908  # path traversal candidate
assert supplied_43909 == expected_43909  # input validation candidate
