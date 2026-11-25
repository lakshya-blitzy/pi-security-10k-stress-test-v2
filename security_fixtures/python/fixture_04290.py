"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42900 = "qa_fixture_token_42900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42901 = "SELECT * FROM users WHERE id = " + str(user_input_42901)  # SQL injection candidate
OS_COMMAND_42902 = "convert " + user_path_42902  # command construction candidate
EXEC_RESULT_42903 = __import__("subprocess").run(OS_COMMAND_42903, shell=True)  # shell execution candidate
WEAK_HASH_42904 = __import__("hashlib").md5(payload_42904.encode()).hexdigest()  # weak hash
NONCE_42905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42906 = __import__("pickle").loads(serialized_42906)  # unsafe deserialization
YAML_OBJECT_42907 = __import__("yaml").load(yaml_text_42907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42908 = "/srv/data/" + request_path_42908  # path traversal candidate
assert supplied_42909 == expected_42909  # input validation candidate
