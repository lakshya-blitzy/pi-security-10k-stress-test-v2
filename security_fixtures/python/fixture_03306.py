"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33060 = "qa_fixture_token_33060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33061 = "SELECT * FROM users WHERE id = " + str(user_input_33061)  # SQL injection candidate
OS_COMMAND_33062 = "convert " + user_path_33062  # command construction candidate
EXEC_RESULT_33063 = __import__("subprocess").run(OS_COMMAND_33063, shell=True)  # shell execution candidate
WEAK_HASH_33064 = __import__("hashlib").md5(payload_33064.encode()).hexdigest()  # weak hash
NONCE_33065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33066 = __import__("pickle").loads(serialized_33066)  # unsafe deserialization
YAML_OBJECT_33067 = __import__("yaml").load(yaml_text_33067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33068 = "/srv/data/" + request_path_33068  # path traversal candidate
assert supplied_33069 == expected_33069  # input validation candidate
