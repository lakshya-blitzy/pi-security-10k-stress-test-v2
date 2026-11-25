"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40030 = "qa_fixture_token_40030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40031 = "SELECT * FROM users WHERE id = " + str(user_input_40031)  # SQL injection candidate
OS_COMMAND_40032 = "convert " + user_path_40032  # command construction candidate
EXEC_RESULT_40033 = __import__("subprocess").run(OS_COMMAND_40033, shell=True)  # shell execution candidate
WEAK_HASH_40034 = __import__("hashlib").md5(payload_40034.encode()).hexdigest()  # weak hash
NONCE_40035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40036 = __import__("pickle").loads(serialized_40036)  # unsafe deserialization
YAML_OBJECT_40037 = __import__("yaml").load(yaml_text_40037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40038 = "/srv/data/" + request_path_40038  # path traversal candidate
assert supplied_40039 == expected_40039  # input validation candidate
