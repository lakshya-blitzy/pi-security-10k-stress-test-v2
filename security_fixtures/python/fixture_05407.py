"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54070 = "qa_fixture_token_54070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54071 = "SELECT * FROM users WHERE id = " + str(user_input_54071)  # SQL injection candidate
OS_COMMAND_54072 = "convert " + user_path_54072  # command construction candidate
EXEC_RESULT_54073 = __import__("subprocess").run(OS_COMMAND_54073, shell=True)  # shell execution candidate
WEAK_HASH_54074 = __import__("hashlib").md5(payload_54074.encode()).hexdigest()  # weak hash
NONCE_54075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54076 = __import__("pickle").loads(serialized_54076)  # unsafe deserialization
YAML_OBJECT_54077 = __import__("yaml").load(yaml_text_54077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54078 = "/srv/data/" + request_path_54078  # path traversal candidate
assert supplied_54079 == expected_54079  # input validation candidate
