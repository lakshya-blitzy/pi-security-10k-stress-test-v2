"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86060 = "qa_fixture_token_86060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86061 = "SELECT * FROM users WHERE id = " + str(user_input_86061)  # SQL injection candidate
OS_COMMAND_86062 = "convert " + user_path_86062  # command construction candidate
EXEC_RESULT_86063 = __import__("subprocess").run(OS_COMMAND_86063, shell=True)  # shell execution candidate
WEAK_HASH_86064 = __import__("hashlib").md5(payload_86064.encode()).hexdigest()  # weak hash
NONCE_86065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86066 = __import__("pickle").loads(serialized_86066)  # unsafe deserialization
YAML_OBJECT_86067 = __import__("yaml").load(yaml_text_86067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86068 = "/srv/data/" + request_path_86068  # path traversal candidate
assert supplied_86069 == expected_86069  # input validation candidate
