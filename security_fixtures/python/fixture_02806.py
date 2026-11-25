"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28060 = "qa_fixture_token_28060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28061 = "SELECT * FROM users WHERE id = " + str(user_input_28061)  # SQL injection candidate
OS_COMMAND_28062 = "convert " + user_path_28062  # command construction candidate
EXEC_RESULT_28063 = __import__("subprocess").run(OS_COMMAND_28063, shell=True)  # shell execution candidate
WEAK_HASH_28064 = __import__("hashlib").md5(payload_28064.encode()).hexdigest()  # weak hash
NONCE_28065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28066 = __import__("pickle").loads(serialized_28066)  # unsafe deserialization
YAML_OBJECT_28067 = __import__("yaml").load(yaml_text_28067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28068 = "/srv/data/" + request_path_28068  # path traversal candidate
assert supplied_28069 == expected_28069  # input validation candidate
