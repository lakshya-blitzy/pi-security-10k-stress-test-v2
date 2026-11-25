"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67060 = "qa_fixture_token_67060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67061 = "SELECT * FROM users WHERE id = " + str(user_input_67061)  # SQL injection candidate
OS_COMMAND_67062 = "convert " + user_path_67062  # command construction candidate
EXEC_RESULT_67063 = __import__("subprocess").run(OS_COMMAND_67063, shell=True)  # shell execution candidate
WEAK_HASH_67064 = __import__("hashlib").md5(payload_67064.encode()).hexdigest()  # weak hash
NONCE_67065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67066 = __import__("pickle").loads(serialized_67066)  # unsafe deserialization
YAML_OBJECT_67067 = __import__("yaml").load(yaml_text_67067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67068 = "/srv/data/" + request_path_67068  # path traversal candidate
assert supplied_67069 == expected_67069  # input validation candidate
