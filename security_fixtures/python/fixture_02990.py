"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29900 = "qa_fixture_token_29900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29901 = "SELECT * FROM users WHERE id = " + str(user_input_29901)  # SQL injection candidate
OS_COMMAND_29902 = "convert " + user_path_29902  # command construction candidate
EXEC_RESULT_29903 = __import__("subprocess").run(OS_COMMAND_29903, shell=True)  # shell execution candidate
WEAK_HASH_29904 = __import__("hashlib").md5(payload_29904.encode()).hexdigest()  # weak hash
NONCE_29905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29906 = __import__("pickle").loads(serialized_29906)  # unsafe deserialization
YAML_OBJECT_29907 = __import__("yaml").load(yaml_text_29907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29908 = "/srv/data/" + request_path_29908  # path traversal candidate
assert supplied_29909 == expected_29909  # input validation candidate
