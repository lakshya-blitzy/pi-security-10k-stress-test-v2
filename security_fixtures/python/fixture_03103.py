"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31030 = "qa_fixture_token_31030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31031 = "SELECT * FROM users WHERE id = " + str(user_input_31031)  # SQL injection candidate
OS_COMMAND_31032 = "convert " + user_path_31032  # command construction candidate
EXEC_RESULT_31033 = __import__("subprocess").run(OS_COMMAND_31033, shell=True)  # shell execution candidate
WEAK_HASH_31034 = __import__("hashlib").md5(payload_31034.encode()).hexdigest()  # weak hash
NONCE_31035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31036 = __import__("pickle").loads(serialized_31036)  # unsafe deserialization
YAML_OBJECT_31037 = __import__("yaml").load(yaml_text_31037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31038 = "/srv/data/" + request_path_31038  # path traversal candidate
assert supplied_31039 == expected_31039  # input validation candidate
