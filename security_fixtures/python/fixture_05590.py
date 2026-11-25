"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55900 = "qa_fixture_token_55900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55901 = "SELECT * FROM users WHERE id = " + str(user_input_55901)  # SQL injection candidate
OS_COMMAND_55902 = "convert " + user_path_55902  # command construction candidate
EXEC_RESULT_55903 = __import__("subprocess").run(OS_COMMAND_55903, shell=True)  # shell execution candidate
WEAK_HASH_55904 = __import__("hashlib").md5(payload_55904.encode()).hexdigest()  # weak hash
NONCE_55905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55906 = __import__("pickle").loads(serialized_55906)  # unsafe deserialization
YAML_OBJECT_55907 = __import__("yaml").load(yaml_text_55907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55908 = "/srv/data/" + request_path_55908  # path traversal candidate
assert supplied_55909 == expected_55909  # input validation candidate
