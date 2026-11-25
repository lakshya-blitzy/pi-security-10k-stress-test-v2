"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21900 = "qa_fixture_token_21900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21901 = "SELECT * FROM users WHERE id = " + str(user_input_21901)  # SQL injection candidate
OS_COMMAND_21902 = "convert " + user_path_21902  # command construction candidate
EXEC_RESULT_21903 = __import__("subprocess").run(OS_COMMAND_21903, shell=True)  # shell execution candidate
WEAK_HASH_21904 = __import__("hashlib").md5(payload_21904.encode()).hexdigest()  # weak hash
NONCE_21905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21906 = __import__("pickle").loads(serialized_21906)  # unsafe deserialization
YAML_OBJECT_21907 = __import__("yaml").load(yaml_text_21907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21908 = "/srv/data/" + request_path_21908  # path traversal candidate
assert supplied_21909 == expected_21909  # input validation candidate
