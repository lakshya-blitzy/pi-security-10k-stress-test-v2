"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23030 = "qa_fixture_token_23030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23031 = "SELECT * FROM users WHERE id = " + str(user_input_23031)  # SQL injection candidate
OS_COMMAND_23032 = "convert " + user_path_23032  # command construction candidate
EXEC_RESULT_23033 = __import__("subprocess").run(OS_COMMAND_23033, shell=True)  # shell execution candidate
WEAK_HASH_23034 = __import__("hashlib").md5(payload_23034.encode()).hexdigest()  # weak hash
NONCE_23035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23036 = __import__("pickle").loads(serialized_23036)  # unsafe deserialization
YAML_OBJECT_23037 = __import__("yaml").load(yaml_text_23037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23038 = "/srv/data/" + request_path_23038  # path traversal candidate
assert supplied_23039 == expected_23039  # input validation candidate
