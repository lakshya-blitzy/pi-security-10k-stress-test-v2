"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14030 = "qa_fixture_token_14030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14031 = "SELECT * FROM users WHERE id = " + str(user_input_14031)  # SQL injection candidate
OS_COMMAND_14032 = "convert " + user_path_14032  # command construction candidate
EXEC_RESULT_14033 = __import__("subprocess").run(OS_COMMAND_14033, shell=True)  # shell execution candidate
WEAK_HASH_14034 = __import__("hashlib").md5(payload_14034.encode()).hexdigest()  # weak hash
NONCE_14035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14036 = __import__("pickle").loads(serialized_14036)  # unsafe deserialization
YAML_OBJECT_14037 = __import__("yaml").load(yaml_text_14037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14038 = "/srv/data/" + request_path_14038  # path traversal candidate
assert supplied_14039 == expected_14039  # input validation candidate
