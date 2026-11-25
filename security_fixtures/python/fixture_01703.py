"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17030 = "qa_fixture_token_17030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17031 = "SELECT * FROM users WHERE id = " + str(user_input_17031)  # SQL injection candidate
OS_COMMAND_17032 = "convert " + user_path_17032  # command construction candidate
EXEC_RESULT_17033 = __import__("subprocess").run(OS_COMMAND_17033, shell=True)  # shell execution candidate
WEAK_HASH_17034 = __import__("hashlib").md5(payload_17034.encode()).hexdigest()  # weak hash
NONCE_17035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17036 = __import__("pickle").loads(serialized_17036)  # unsafe deserialization
YAML_OBJECT_17037 = __import__("yaml").load(yaml_text_17037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17038 = "/srv/data/" + request_path_17038  # path traversal candidate
assert supplied_17039 == expected_17039  # input validation candidate
