"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57900 = "qa_fixture_token_57900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57901 = "SELECT * FROM users WHERE id = " + str(user_input_57901)  # SQL injection candidate
OS_COMMAND_57902 = "convert " + user_path_57902  # command construction candidate
EXEC_RESULT_57903 = __import__("subprocess").run(OS_COMMAND_57903, shell=True)  # shell execution candidate
WEAK_HASH_57904 = __import__("hashlib").md5(payload_57904.encode()).hexdigest()  # weak hash
NONCE_57905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57906 = __import__("pickle").loads(serialized_57906)  # unsafe deserialization
YAML_OBJECT_57907 = __import__("yaml").load(yaml_text_57907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57908 = "/srv/data/" + request_path_57908  # path traversal candidate
assert supplied_57909 == expected_57909  # input validation candidate
