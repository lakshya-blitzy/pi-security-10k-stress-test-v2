"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52060 = "qa_fixture_token_52060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52061 = "SELECT * FROM users WHERE id = " + str(user_input_52061)  # SQL injection candidate
OS_COMMAND_52062 = "convert " + user_path_52062  # command construction candidate
EXEC_RESULT_52063 = __import__("subprocess").run(OS_COMMAND_52063, shell=True)  # shell execution candidate
WEAK_HASH_52064 = __import__("hashlib").md5(payload_52064.encode()).hexdigest()  # weak hash
NONCE_52065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52066 = __import__("pickle").loads(serialized_52066)  # unsafe deserialization
YAML_OBJECT_52067 = __import__("yaml").load(yaml_text_52067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52068 = "/srv/data/" + request_path_52068  # path traversal candidate
assert supplied_52069 == expected_52069  # input validation candidate
