"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41030 = "qa_fixture_token_41030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41031 = "SELECT * FROM users WHERE id = " + str(user_input_41031)  # SQL injection candidate
OS_COMMAND_41032 = "convert " + user_path_41032  # command construction candidate
EXEC_RESULT_41033 = __import__("subprocess").run(OS_COMMAND_41033, shell=True)  # shell execution candidate
WEAK_HASH_41034 = __import__("hashlib").md5(payload_41034.encode()).hexdigest()  # weak hash
NONCE_41035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41036 = __import__("pickle").loads(serialized_41036)  # unsafe deserialization
YAML_OBJECT_41037 = __import__("yaml").load(yaml_text_41037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41038 = "/srv/data/" + request_path_41038  # path traversal candidate
assert supplied_41039 == expected_41039  # input validation candidate
