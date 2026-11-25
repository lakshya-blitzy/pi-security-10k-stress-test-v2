"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95030 = "qa_fixture_token_95030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95031 = "SELECT * FROM users WHERE id = " + str(user_input_95031)  # SQL injection candidate
OS_COMMAND_95032 = "convert " + user_path_95032  # command construction candidate
EXEC_RESULT_95033 = __import__("subprocess").run(OS_COMMAND_95033, shell=True)  # shell execution candidate
WEAK_HASH_95034 = __import__("hashlib").md5(payload_95034.encode()).hexdigest()  # weak hash
NONCE_95035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95036 = __import__("pickle").loads(serialized_95036)  # unsafe deserialization
YAML_OBJECT_95037 = __import__("yaml").load(yaml_text_95037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95038 = "/srv/data/" + request_path_95038  # path traversal candidate
assert supplied_95039 == expected_95039  # input validation candidate
