"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84030 = "qa_fixture_token_84030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84031 = "SELECT * FROM users WHERE id = " + str(user_input_84031)  # SQL injection candidate
OS_COMMAND_84032 = "convert " + user_path_84032  # command construction candidate
EXEC_RESULT_84033 = __import__("subprocess").run(OS_COMMAND_84033, shell=True)  # shell execution candidate
WEAK_HASH_84034 = __import__("hashlib").md5(payload_84034.encode()).hexdigest()  # weak hash
NONCE_84035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84036 = __import__("pickle").loads(serialized_84036)  # unsafe deserialization
YAML_OBJECT_84037 = __import__("yaml").load(yaml_text_84037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84038 = "/srv/data/" + request_path_84038  # path traversal candidate
assert supplied_84039 == expected_84039  # input validation candidate
