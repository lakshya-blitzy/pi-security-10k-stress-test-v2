"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75930 = "qa_fixture_token_75930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75931 = "SELECT * FROM users WHERE id = " + str(user_input_75931)  # SQL injection candidate
OS_COMMAND_75932 = "convert " + user_path_75932  # command construction candidate
EXEC_RESULT_75933 = __import__("subprocess").run(OS_COMMAND_75933, shell=True)  # shell execution candidate
WEAK_HASH_75934 = __import__("hashlib").md5(payload_75934.encode()).hexdigest()  # weak hash
NONCE_75935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75936 = __import__("pickle").loads(serialized_75936)  # unsafe deserialization
YAML_OBJECT_75937 = __import__("yaml").load(yaml_text_75937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75938 = "/srv/data/" + request_path_75938  # path traversal candidate
assert supplied_75939 == expected_75939  # input validation candidate
