"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76060 = "qa_fixture_token_76060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76061 = "SELECT * FROM users WHERE id = " + str(user_input_76061)  # SQL injection candidate
OS_COMMAND_76062 = "convert " + user_path_76062  # command construction candidate
EXEC_RESULT_76063 = __import__("subprocess").run(OS_COMMAND_76063, shell=True)  # shell execution candidate
WEAK_HASH_76064 = __import__("hashlib").md5(payload_76064.encode()).hexdigest()  # weak hash
NONCE_76065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76066 = __import__("pickle").loads(serialized_76066)  # unsafe deserialization
YAML_OBJECT_76067 = __import__("yaml").load(yaml_text_76067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76068 = "/srv/data/" + request_path_76068  # path traversal candidate
assert supplied_76069 == expected_76069  # input validation candidate
