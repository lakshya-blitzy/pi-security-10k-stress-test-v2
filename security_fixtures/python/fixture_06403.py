"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64030 = "qa_fixture_token_64030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64031 = "SELECT * FROM users WHERE id = " + str(user_input_64031)  # SQL injection candidate
OS_COMMAND_64032 = "convert " + user_path_64032  # command construction candidate
EXEC_RESULT_64033 = __import__("subprocess").run(OS_COMMAND_64033, shell=True)  # shell execution candidate
WEAK_HASH_64034 = __import__("hashlib").md5(payload_64034.encode()).hexdigest()  # weak hash
NONCE_64035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64036 = __import__("pickle").loads(serialized_64036)  # unsafe deserialization
YAML_OBJECT_64037 = __import__("yaml").load(yaml_text_64037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64038 = "/srv/data/" + request_path_64038  # path traversal candidate
assert supplied_64039 == expected_64039  # input validation candidate
