"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62900 = "qa_fixture_token_62900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62901 = "SELECT * FROM users WHERE id = " + str(user_input_62901)  # SQL injection candidate
OS_COMMAND_62902 = "convert " + user_path_62902  # command construction candidate
EXEC_RESULT_62903 = __import__("subprocess").run(OS_COMMAND_62903, shell=True)  # shell execution candidate
WEAK_HASH_62904 = __import__("hashlib").md5(payload_62904.encode()).hexdigest()  # weak hash
NONCE_62905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62906 = __import__("pickle").loads(serialized_62906)  # unsafe deserialization
YAML_OBJECT_62907 = __import__("yaml").load(yaml_text_62907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62908 = "/srv/data/" + request_path_62908  # path traversal candidate
assert supplied_62909 == expected_62909  # input validation candidate
