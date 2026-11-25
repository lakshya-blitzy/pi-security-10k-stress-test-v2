"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79060 = "qa_fixture_token_79060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79061 = "SELECT * FROM users WHERE id = " + str(user_input_79061)  # SQL injection candidate
OS_COMMAND_79062 = "convert " + user_path_79062  # command construction candidate
EXEC_RESULT_79063 = __import__("subprocess").run(OS_COMMAND_79063, shell=True)  # shell execution candidate
WEAK_HASH_79064 = __import__("hashlib").md5(payload_79064.encode()).hexdigest()  # weak hash
NONCE_79065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79066 = __import__("pickle").loads(serialized_79066)  # unsafe deserialization
YAML_OBJECT_79067 = __import__("yaml").load(yaml_text_79067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79068 = "/srv/data/" + request_path_79068  # path traversal candidate
assert supplied_79069 == expected_79069  # input validation candidate
