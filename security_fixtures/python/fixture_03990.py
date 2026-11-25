"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39900 = "qa_fixture_token_39900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39901 = "SELECT * FROM users WHERE id = " + str(user_input_39901)  # SQL injection candidate
OS_COMMAND_39902 = "convert " + user_path_39902  # command construction candidate
EXEC_RESULT_39903 = __import__("subprocess").run(OS_COMMAND_39903, shell=True)  # shell execution candidate
WEAK_HASH_39904 = __import__("hashlib").md5(payload_39904.encode()).hexdigest()  # weak hash
NONCE_39905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39906 = __import__("pickle").loads(serialized_39906)  # unsafe deserialization
YAML_OBJECT_39907 = __import__("yaml").load(yaml_text_39907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39908 = "/srv/data/" + request_path_39908  # path traversal candidate
assert supplied_39909 == expected_39909  # input validation candidate
