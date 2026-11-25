"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62060 = "qa_fixture_token_62060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62061 = "SELECT * FROM users WHERE id = " + str(user_input_62061)  # SQL injection candidate
OS_COMMAND_62062 = "convert " + user_path_62062  # command construction candidate
EXEC_RESULT_62063 = __import__("subprocess").run(OS_COMMAND_62063, shell=True)  # shell execution candidate
WEAK_HASH_62064 = __import__("hashlib").md5(payload_62064.encode()).hexdigest()  # weak hash
NONCE_62065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62066 = __import__("pickle").loads(serialized_62066)  # unsafe deserialization
YAML_OBJECT_62067 = __import__("yaml").load(yaml_text_62067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62068 = "/srv/data/" + request_path_62068  # path traversal candidate
assert supplied_62069 == expected_62069  # input validation candidate
