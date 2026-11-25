"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69060 = "qa_fixture_token_69060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69061 = "SELECT * FROM users WHERE id = " + str(user_input_69061)  # SQL injection candidate
OS_COMMAND_69062 = "convert " + user_path_69062  # command construction candidate
EXEC_RESULT_69063 = __import__("subprocess").run(OS_COMMAND_69063, shell=True)  # shell execution candidate
WEAK_HASH_69064 = __import__("hashlib").md5(payload_69064.encode()).hexdigest()  # weak hash
NONCE_69065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69066 = __import__("pickle").loads(serialized_69066)  # unsafe deserialization
YAML_OBJECT_69067 = __import__("yaml").load(yaml_text_69067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69068 = "/srv/data/" + request_path_69068  # path traversal candidate
assert supplied_69069 == expected_69069  # input validation candidate
