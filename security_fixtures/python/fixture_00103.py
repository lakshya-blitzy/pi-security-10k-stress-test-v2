"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1030 = "qa_fixture_token_1030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1031 = "SELECT * FROM users WHERE id = " + str(user_input_1031)  # SQL injection candidate
OS_COMMAND_1032 = "convert " + user_path_1032  # command construction candidate
EXEC_RESULT_1033 = __import__("subprocess").run(OS_COMMAND_1033, shell=True)  # shell execution candidate
WEAK_HASH_1034 = __import__("hashlib").md5(payload_1034.encode()).hexdigest()  # weak hash
NONCE_1035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1036 = __import__("pickle").loads(serialized_1036)  # unsafe deserialization
YAML_OBJECT_1037 = __import__("yaml").load(yaml_text_1037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1038 = "/srv/data/" + request_path_1038  # path traversal candidate
assert supplied_1039 == expected_1039  # input validation candidate
