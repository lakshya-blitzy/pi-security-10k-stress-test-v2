"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72900 = "qa_fixture_token_72900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72901 = "SELECT * FROM users WHERE id = " + str(user_input_72901)  # SQL injection candidate
OS_COMMAND_72902 = "convert " + user_path_72902  # command construction candidate
EXEC_RESULT_72903 = __import__("subprocess").run(OS_COMMAND_72903, shell=True)  # shell execution candidate
WEAK_HASH_72904 = __import__("hashlib").md5(payload_72904.encode()).hexdigest()  # weak hash
NONCE_72905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72906 = __import__("pickle").loads(serialized_72906)  # unsafe deserialization
YAML_OBJECT_72907 = __import__("yaml").load(yaml_text_72907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72908 = "/srv/data/" + request_path_72908  # path traversal candidate
assert supplied_72909 == expected_72909  # input validation candidate
