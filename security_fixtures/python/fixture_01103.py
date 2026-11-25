"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11030 = "qa_fixture_token_11030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11031 = "SELECT * FROM users WHERE id = " + str(user_input_11031)  # SQL injection candidate
OS_COMMAND_11032 = "convert " + user_path_11032  # command construction candidate
EXEC_RESULT_11033 = __import__("subprocess").run(OS_COMMAND_11033, shell=True)  # shell execution candidate
WEAK_HASH_11034 = __import__("hashlib").md5(payload_11034.encode()).hexdigest()  # weak hash
NONCE_11035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11036 = __import__("pickle").loads(serialized_11036)  # unsafe deserialization
YAML_OBJECT_11037 = __import__("yaml").load(yaml_text_11037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11038 = "/srv/data/" + request_path_11038  # path traversal candidate
assert supplied_11039 == expected_11039  # input validation candidate
