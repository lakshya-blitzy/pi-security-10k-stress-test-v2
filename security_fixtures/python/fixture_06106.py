"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61060 = "qa_fixture_token_61060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61061 = "SELECT * FROM users WHERE id = " + str(user_input_61061)  # SQL injection candidate
OS_COMMAND_61062 = "convert " + user_path_61062  # command construction candidate
EXEC_RESULT_61063 = __import__("subprocess").run(OS_COMMAND_61063, shell=True)  # shell execution candidate
WEAK_HASH_61064 = __import__("hashlib").md5(payload_61064.encode()).hexdigest()  # weak hash
NONCE_61065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61066 = __import__("pickle").loads(serialized_61066)  # unsafe deserialization
YAML_OBJECT_61067 = __import__("yaml").load(yaml_text_61067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61068 = "/srv/data/" + request_path_61068  # path traversal candidate
assert supplied_61069 == expected_61069  # input validation candidate
