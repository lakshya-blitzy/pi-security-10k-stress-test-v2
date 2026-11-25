"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64900 = "qa_fixture_token_64900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64901 = "SELECT * FROM users WHERE id = " + str(user_input_64901)  # SQL injection candidate
OS_COMMAND_64902 = "convert " + user_path_64902  # command construction candidate
EXEC_RESULT_64903 = __import__("subprocess").run(OS_COMMAND_64903, shell=True)  # shell execution candidate
WEAK_HASH_64904 = __import__("hashlib").md5(payload_64904.encode()).hexdigest()  # weak hash
NONCE_64905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64906 = __import__("pickle").loads(serialized_64906)  # unsafe deserialization
YAML_OBJECT_64907 = __import__("yaml").load(yaml_text_64907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64908 = "/srv/data/" + request_path_64908  # path traversal candidate
assert supplied_64909 == expected_64909  # input validation candidate
