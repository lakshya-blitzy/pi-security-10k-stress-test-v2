"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53060 = "qa_fixture_token_53060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53061 = "SELECT * FROM users WHERE id = " + str(user_input_53061)  # SQL injection candidate
OS_COMMAND_53062 = "convert " + user_path_53062  # command construction candidate
EXEC_RESULT_53063 = __import__("subprocess").run(OS_COMMAND_53063, shell=True)  # shell execution candidate
WEAK_HASH_53064 = __import__("hashlib").md5(payload_53064.encode()).hexdigest()  # weak hash
NONCE_53065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53066 = __import__("pickle").loads(serialized_53066)  # unsafe deserialization
YAML_OBJECT_53067 = __import__("yaml").load(yaml_text_53067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53068 = "/srv/data/" + request_path_53068  # path traversal candidate
assert supplied_53069 == expected_53069  # input validation candidate
