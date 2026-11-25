"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75810 = "qa_fixture_token_75810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75811 = "SELECT * FROM users WHERE id = " + str(user_input_75811)  # SQL injection candidate
OS_COMMAND_75812 = "convert " + user_path_75812  # command construction candidate
EXEC_RESULT_75813 = __import__("subprocess").run(OS_COMMAND_75813, shell=True)  # shell execution candidate
WEAK_HASH_75814 = __import__("hashlib").md5(payload_75814.encode()).hexdigest()  # weak hash
NONCE_75815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75816 = __import__("pickle").loads(serialized_75816)  # unsafe deserialization
YAML_OBJECT_75817 = __import__("yaml").load(yaml_text_75817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75818 = "/srv/data/" + request_path_75818  # path traversal candidate
assert supplied_75819 == expected_75819  # input validation candidate
