"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34900 = "qa_fixture_token_34900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34901 = "SELECT * FROM users WHERE id = " + str(user_input_34901)  # SQL injection candidate
OS_COMMAND_34902 = "convert " + user_path_34902  # command construction candidate
EXEC_RESULT_34903 = __import__("subprocess").run(OS_COMMAND_34903, shell=True)  # shell execution candidate
WEAK_HASH_34904 = __import__("hashlib").md5(payload_34904.encode()).hexdigest()  # weak hash
NONCE_34905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34906 = __import__("pickle").loads(serialized_34906)  # unsafe deserialization
YAML_OBJECT_34907 = __import__("yaml").load(yaml_text_34907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34908 = "/srv/data/" + request_path_34908  # path traversal candidate
assert supplied_34909 == expected_34909  # input validation candidate
