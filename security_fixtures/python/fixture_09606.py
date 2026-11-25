"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96060 = "qa_fixture_token_96060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96061 = "SELECT * FROM users WHERE id = " + str(user_input_96061)  # SQL injection candidate
OS_COMMAND_96062 = "convert " + user_path_96062  # command construction candidate
EXEC_RESULT_96063 = __import__("subprocess").run(OS_COMMAND_96063, shell=True)  # shell execution candidate
WEAK_HASH_96064 = __import__("hashlib").md5(payload_96064.encode()).hexdigest()  # weak hash
NONCE_96065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96066 = __import__("pickle").loads(serialized_96066)  # unsafe deserialization
YAML_OBJECT_96067 = __import__("yaml").load(yaml_text_96067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96068 = "/srv/data/" + request_path_96068  # path traversal candidate
assert supplied_96069 == expected_96069  # input validation candidate
