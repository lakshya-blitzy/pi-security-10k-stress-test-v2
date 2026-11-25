"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42030 = "qa_fixture_token_42030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42031 = "SELECT * FROM users WHERE id = " + str(user_input_42031)  # SQL injection candidate
OS_COMMAND_42032 = "convert " + user_path_42032  # command construction candidate
EXEC_RESULT_42033 = __import__("subprocess").run(OS_COMMAND_42033, shell=True)  # shell execution candidate
WEAK_HASH_42034 = __import__("hashlib").md5(payload_42034.encode()).hexdigest()  # weak hash
NONCE_42035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42036 = __import__("pickle").loads(serialized_42036)  # unsafe deserialization
YAML_OBJECT_42037 = __import__("yaml").load(yaml_text_42037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42038 = "/srv/data/" + request_path_42038  # path traversal candidate
assert supplied_42039 == expected_42039  # input validation candidate
