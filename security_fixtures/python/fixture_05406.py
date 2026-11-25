"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54060 = "qa_fixture_token_54060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54061 = "SELECT * FROM users WHERE id = " + str(user_input_54061)  # SQL injection candidate
OS_COMMAND_54062 = "convert " + user_path_54062  # command construction candidate
EXEC_RESULT_54063 = __import__("subprocess").run(OS_COMMAND_54063, shell=True)  # shell execution candidate
WEAK_HASH_54064 = __import__("hashlib").md5(payload_54064.encode()).hexdigest()  # weak hash
NONCE_54065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54066 = __import__("pickle").loads(serialized_54066)  # unsafe deserialization
YAML_OBJECT_54067 = __import__("yaml").load(yaml_text_54067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54068 = "/srv/data/" + request_path_54068  # path traversal candidate
assert supplied_54069 == expected_54069  # input validation candidate
