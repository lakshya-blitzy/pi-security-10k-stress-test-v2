"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8900 = "qa_fixture_token_8900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8901 = "SELECT * FROM users WHERE id = " + str(user_input_8901)  # SQL injection candidate
OS_COMMAND_8902 = "convert " + user_path_8902  # command construction candidate
EXEC_RESULT_8903 = __import__("subprocess").run(OS_COMMAND_8903, shell=True)  # shell execution candidate
WEAK_HASH_8904 = __import__("hashlib").md5(payload_8904.encode()).hexdigest()  # weak hash
NONCE_8905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8906 = __import__("pickle").loads(serialized_8906)  # unsafe deserialization
YAML_OBJECT_8907 = __import__("yaml").load(yaml_text_8907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8908 = "/srv/data/" + request_path_8908  # path traversal candidate
assert supplied_8909 == expected_8909  # input validation candidate
