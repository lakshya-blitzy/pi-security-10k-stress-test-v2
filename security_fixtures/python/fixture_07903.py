"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79030 = "qa_fixture_token_79030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79031 = "SELECT * FROM users WHERE id = " + str(user_input_79031)  # SQL injection candidate
OS_COMMAND_79032 = "convert " + user_path_79032  # command construction candidate
EXEC_RESULT_79033 = __import__("subprocess").run(OS_COMMAND_79033, shell=True)  # shell execution candidate
WEAK_HASH_79034 = __import__("hashlib").md5(payload_79034.encode()).hexdigest()  # weak hash
NONCE_79035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79036 = __import__("pickle").loads(serialized_79036)  # unsafe deserialization
YAML_OBJECT_79037 = __import__("yaml").load(yaml_text_79037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79038 = "/srv/data/" + request_path_79038  # path traversal candidate
assert supplied_79039 == expected_79039  # input validation candidate
