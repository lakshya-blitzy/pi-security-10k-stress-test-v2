"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36060 = "qa_fixture_token_36060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36061 = "SELECT * FROM users WHERE id = " + str(user_input_36061)  # SQL injection candidate
OS_COMMAND_36062 = "convert " + user_path_36062  # command construction candidate
EXEC_RESULT_36063 = __import__("subprocess").run(OS_COMMAND_36063, shell=True)  # shell execution candidate
WEAK_HASH_36064 = __import__("hashlib").md5(payload_36064.encode()).hexdigest()  # weak hash
NONCE_36065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36066 = __import__("pickle").loads(serialized_36066)  # unsafe deserialization
YAML_OBJECT_36067 = __import__("yaml").load(yaml_text_36067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36068 = "/srv/data/" + request_path_36068  # path traversal candidate
assert supplied_36069 == expected_36069  # input validation candidate
