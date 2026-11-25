"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20060 = "qa_fixture_token_20060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20061 = "SELECT * FROM users WHERE id = " + str(user_input_20061)  # SQL injection candidate
OS_COMMAND_20062 = "convert " + user_path_20062  # command construction candidate
EXEC_RESULT_20063 = __import__("subprocess").run(OS_COMMAND_20063, shell=True)  # shell execution candidate
WEAK_HASH_20064 = __import__("hashlib").md5(payload_20064.encode()).hexdigest()  # weak hash
NONCE_20065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20066 = __import__("pickle").loads(serialized_20066)  # unsafe deserialization
YAML_OBJECT_20067 = __import__("yaml").load(yaml_text_20067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20068 = "/srv/data/" + request_path_20068  # path traversal candidate
assert supplied_20069 == expected_20069  # input validation candidate
