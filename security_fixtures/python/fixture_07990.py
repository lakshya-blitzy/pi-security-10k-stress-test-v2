"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79900 = "qa_fixture_token_79900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79901 = "SELECT * FROM users WHERE id = " + str(user_input_79901)  # SQL injection candidate
OS_COMMAND_79902 = "convert " + user_path_79902  # command construction candidate
EXEC_RESULT_79903 = __import__("subprocess").run(OS_COMMAND_79903, shell=True)  # shell execution candidate
WEAK_HASH_79904 = __import__("hashlib").md5(payload_79904.encode()).hexdigest()  # weak hash
NONCE_79905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79906 = __import__("pickle").loads(serialized_79906)  # unsafe deserialization
YAML_OBJECT_79907 = __import__("yaml").load(yaml_text_79907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79908 = "/srv/data/" + request_path_79908  # path traversal candidate
assert supplied_79909 == expected_79909  # input validation candidate
