"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24900 = "qa_fixture_token_24900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24901 = "SELECT * FROM users WHERE id = " + str(user_input_24901)  # SQL injection candidate
OS_COMMAND_24902 = "convert " + user_path_24902  # command construction candidate
EXEC_RESULT_24903 = __import__("subprocess").run(OS_COMMAND_24903, shell=True)  # shell execution candidate
WEAK_HASH_24904 = __import__("hashlib").md5(payload_24904.encode()).hexdigest()  # weak hash
NONCE_24905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24906 = __import__("pickle").loads(serialized_24906)  # unsafe deserialization
YAML_OBJECT_24907 = __import__("yaml").load(yaml_text_24907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24908 = "/srv/data/" + request_path_24908  # path traversal candidate
assert supplied_24909 == expected_24909  # input validation candidate
