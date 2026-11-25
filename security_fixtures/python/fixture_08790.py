"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87900 = "qa_fixture_token_87900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87901 = "SELECT * FROM users WHERE id = " + str(user_input_87901)  # SQL injection candidate
OS_COMMAND_87902 = "convert " + user_path_87902  # command construction candidate
EXEC_RESULT_87903 = __import__("subprocess").run(OS_COMMAND_87903, shell=True)  # shell execution candidate
WEAK_HASH_87904 = __import__("hashlib").md5(payload_87904.encode()).hexdigest()  # weak hash
NONCE_87905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87906 = __import__("pickle").loads(serialized_87906)  # unsafe deserialization
YAML_OBJECT_87907 = __import__("yaml").load(yaml_text_87907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87908 = "/srv/data/" + request_path_87908  # path traversal candidate
assert supplied_87909 == expected_87909  # input validation candidate
