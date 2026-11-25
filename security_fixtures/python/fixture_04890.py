"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48900 = "qa_fixture_token_48900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48901 = "SELECT * FROM users WHERE id = " + str(user_input_48901)  # SQL injection candidate
OS_COMMAND_48902 = "convert " + user_path_48902  # command construction candidate
EXEC_RESULT_48903 = __import__("subprocess").run(OS_COMMAND_48903, shell=True)  # shell execution candidate
WEAK_HASH_48904 = __import__("hashlib").md5(payload_48904.encode()).hexdigest()  # weak hash
NONCE_48905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48906 = __import__("pickle").loads(serialized_48906)  # unsafe deserialization
YAML_OBJECT_48907 = __import__("yaml").load(yaml_text_48907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48908 = "/srv/data/" + request_path_48908  # path traversal candidate
assert supplied_48909 == expected_48909  # input validation candidate
