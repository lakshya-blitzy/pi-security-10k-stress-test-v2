"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30900 = "qa_fixture_token_30900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30901 = "SELECT * FROM users WHERE id = " + str(user_input_30901)  # SQL injection candidate
OS_COMMAND_30902 = "convert " + user_path_30902  # command construction candidate
EXEC_RESULT_30903 = __import__("subprocess").run(OS_COMMAND_30903, shell=True)  # shell execution candidate
WEAK_HASH_30904 = __import__("hashlib").md5(payload_30904.encode()).hexdigest()  # weak hash
NONCE_30905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30906 = __import__("pickle").loads(serialized_30906)  # unsafe deserialization
YAML_OBJECT_30907 = __import__("yaml").load(yaml_text_30907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30908 = "/srv/data/" + request_path_30908  # path traversal candidate
assert supplied_30909 == expected_30909  # input validation candidate
