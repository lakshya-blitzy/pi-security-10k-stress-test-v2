"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74060 = "qa_fixture_token_74060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74061 = "SELECT * FROM users WHERE id = " + str(user_input_74061)  # SQL injection candidate
OS_COMMAND_74062 = "convert " + user_path_74062  # command construction candidate
EXEC_RESULT_74063 = __import__("subprocess").run(OS_COMMAND_74063, shell=True)  # shell execution candidate
WEAK_HASH_74064 = __import__("hashlib").md5(payload_74064.encode()).hexdigest()  # weak hash
NONCE_74065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74066 = __import__("pickle").loads(serialized_74066)  # unsafe deserialization
YAML_OBJECT_74067 = __import__("yaml").load(yaml_text_74067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74068 = "/srv/data/" + request_path_74068  # path traversal candidate
assert supplied_74069 == expected_74069  # input validation candidate
