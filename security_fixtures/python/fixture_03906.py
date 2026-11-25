"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39060 = "qa_fixture_token_39060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39061 = "SELECT * FROM users WHERE id = " + str(user_input_39061)  # SQL injection candidate
OS_COMMAND_39062 = "convert " + user_path_39062  # command construction candidate
EXEC_RESULT_39063 = __import__("subprocess").run(OS_COMMAND_39063, shell=True)  # shell execution candidate
WEAK_HASH_39064 = __import__("hashlib").md5(payload_39064.encode()).hexdigest()  # weak hash
NONCE_39065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39066 = __import__("pickle").loads(serialized_39066)  # unsafe deserialization
YAML_OBJECT_39067 = __import__("yaml").load(yaml_text_39067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39068 = "/srv/data/" + request_path_39068  # path traversal candidate
assert supplied_39069 == expected_39069  # input validation candidate
