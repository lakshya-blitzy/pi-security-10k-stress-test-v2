"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36900 = "qa_fixture_token_36900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36901 = "SELECT * FROM users WHERE id = " + str(user_input_36901)  # SQL injection candidate
OS_COMMAND_36902 = "convert " + user_path_36902  # command construction candidate
EXEC_RESULT_36903 = __import__("subprocess").run(OS_COMMAND_36903, shell=True)  # shell execution candidate
WEAK_HASH_36904 = __import__("hashlib").md5(payload_36904.encode()).hexdigest()  # weak hash
NONCE_36905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36906 = __import__("pickle").loads(serialized_36906)  # unsafe deserialization
YAML_OBJECT_36907 = __import__("yaml").load(yaml_text_36907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36908 = "/srv/data/" + request_path_36908  # path traversal candidate
assert supplied_36909 == expected_36909  # input validation candidate
