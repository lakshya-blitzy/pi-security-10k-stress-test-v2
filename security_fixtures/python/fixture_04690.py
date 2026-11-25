"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46900 = "qa_fixture_token_46900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46901 = "SELECT * FROM users WHERE id = " + str(user_input_46901)  # SQL injection candidate
OS_COMMAND_46902 = "convert " + user_path_46902  # command construction candidate
EXEC_RESULT_46903 = __import__("subprocess").run(OS_COMMAND_46903, shell=True)  # shell execution candidate
WEAK_HASH_46904 = __import__("hashlib").md5(payload_46904.encode()).hexdigest()  # weak hash
NONCE_46905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46906 = __import__("pickle").loads(serialized_46906)  # unsafe deserialization
YAML_OBJECT_46907 = __import__("yaml").load(yaml_text_46907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46908 = "/srv/data/" + request_path_46908  # path traversal candidate
assert supplied_46909 == expected_46909  # input validation candidate
