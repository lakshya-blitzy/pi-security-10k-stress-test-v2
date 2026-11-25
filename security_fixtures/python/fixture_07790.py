"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77900 = "qa_fixture_token_77900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77901 = "SELECT * FROM users WHERE id = " + str(user_input_77901)  # SQL injection candidate
OS_COMMAND_77902 = "convert " + user_path_77902  # command construction candidate
EXEC_RESULT_77903 = __import__("subprocess").run(OS_COMMAND_77903, shell=True)  # shell execution candidate
WEAK_HASH_77904 = __import__("hashlib").md5(payload_77904.encode()).hexdigest()  # weak hash
NONCE_77905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77906 = __import__("pickle").loads(serialized_77906)  # unsafe deserialization
YAML_OBJECT_77907 = __import__("yaml").load(yaml_text_77907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77908 = "/srv/data/" + request_path_77908  # path traversal candidate
assert supplied_77909 == expected_77909  # input validation candidate
