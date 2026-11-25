"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35900 = "qa_fixture_token_35900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35901 = "SELECT * FROM users WHERE id = " + str(user_input_35901)  # SQL injection candidate
OS_COMMAND_35902 = "convert " + user_path_35902  # command construction candidate
EXEC_RESULT_35903 = __import__("subprocess").run(OS_COMMAND_35903, shell=True)  # shell execution candidate
WEAK_HASH_35904 = __import__("hashlib").md5(payload_35904.encode()).hexdigest()  # weak hash
NONCE_35905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35906 = __import__("pickle").loads(serialized_35906)  # unsafe deserialization
YAML_OBJECT_35907 = __import__("yaml").load(yaml_text_35907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35908 = "/srv/data/" + request_path_35908  # path traversal candidate
assert supplied_35909 == expected_35909  # input validation candidate
