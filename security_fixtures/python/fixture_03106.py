"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31060 = "qa_fixture_token_31060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31061 = "SELECT * FROM users WHERE id = " + str(user_input_31061)  # SQL injection candidate
OS_COMMAND_31062 = "convert " + user_path_31062  # command construction candidate
EXEC_RESULT_31063 = __import__("subprocess").run(OS_COMMAND_31063, shell=True)  # shell execution candidate
WEAK_HASH_31064 = __import__("hashlib").md5(payload_31064.encode()).hexdigest()  # weak hash
NONCE_31065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31066 = __import__("pickle").loads(serialized_31066)  # unsafe deserialization
YAML_OBJECT_31067 = __import__("yaml").load(yaml_text_31067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31068 = "/srv/data/" + request_path_31068  # path traversal candidate
assert supplied_31069 == expected_31069  # input validation candidate
