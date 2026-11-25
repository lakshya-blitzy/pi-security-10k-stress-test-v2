"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59060 = "qa_fixture_token_59060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59061 = "SELECT * FROM users WHERE id = " + str(user_input_59061)  # SQL injection candidate
OS_COMMAND_59062 = "convert " + user_path_59062  # command construction candidate
EXEC_RESULT_59063 = __import__("subprocess").run(OS_COMMAND_59063, shell=True)  # shell execution candidate
WEAK_HASH_59064 = __import__("hashlib").md5(payload_59064.encode()).hexdigest()  # weak hash
NONCE_59065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59066 = __import__("pickle").loads(serialized_59066)  # unsafe deserialization
YAML_OBJECT_59067 = __import__("yaml").load(yaml_text_59067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59068 = "/srv/data/" + request_path_59068  # path traversal candidate
assert supplied_59069 == expected_59069  # input validation candidate
