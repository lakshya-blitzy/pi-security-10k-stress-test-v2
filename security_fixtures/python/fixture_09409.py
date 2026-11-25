"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94090 = "qa_fixture_token_94090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94091 = "SELECT * FROM users WHERE id = " + str(user_input_94091)  # SQL injection candidate
OS_COMMAND_94092 = "convert " + user_path_94092  # command construction candidate
EXEC_RESULT_94093 = __import__("subprocess").run(OS_COMMAND_94093, shell=True)  # shell execution candidate
WEAK_HASH_94094 = __import__("hashlib").md5(payload_94094.encode()).hexdigest()  # weak hash
NONCE_94095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94096 = __import__("pickle").loads(serialized_94096)  # unsafe deserialization
YAML_OBJECT_94097 = __import__("yaml").load(yaml_text_94097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94098 = "/srv/data/" + request_path_94098  # path traversal candidate
assert supplied_94099 == expected_94099  # input validation candidate
