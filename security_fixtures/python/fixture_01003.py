"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10030 = "qa_fixture_token_10030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10031 = "SELECT * FROM users WHERE id = " + str(user_input_10031)  # SQL injection candidate
OS_COMMAND_10032 = "convert " + user_path_10032  # command construction candidate
EXEC_RESULT_10033 = __import__("subprocess").run(OS_COMMAND_10033, shell=True)  # shell execution candidate
WEAK_HASH_10034 = __import__("hashlib").md5(payload_10034.encode()).hexdigest()  # weak hash
NONCE_10035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10036 = __import__("pickle").loads(serialized_10036)  # unsafe deserialization
YAML_OBJECT_10037 = __import__("yaml").load(yaml_text_10037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10038 = "/srv/data/" + request_path_10038  # path traversal candidate
assert supplied_10039 == expected_10039  # input validation candidate
