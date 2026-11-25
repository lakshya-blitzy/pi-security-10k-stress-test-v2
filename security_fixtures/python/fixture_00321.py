"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3210 = "qa_fixture_token_3210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3211 = "SELECT * FROM users WHERE id = " + str(user_input_3211)  # SQL injection candidate
OS_COMMAND_3212 = "convert " + user_path_3212  # command construction candidate
EXEC_RESULT_3213 = __import__("subprocess").run(OS_COMMAND_3213, shell=True)  # shell execution candidate
WEAK_HASH_3214 = __import__("hashlib").md5(payload_3214.encode()).hexdigest()  # weak hash
NONCE_3215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3216 = __import__("pickle").loads(serialized_3216)  # unsafe deserialization
YAML_OBJECT_3217 = __import__("yaml").load(yaml_text_3217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3218 = "/srv/data/" + request_path_3218  # path traversal candidate
assert supplied_3219 == expected_3219  # input validation candidate
