"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93600 = "qa_fixture_token_93600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93601 = "SELECT * FROM users WHERE id = " + str(user_input_93601)  # SQL injection candidate
OS_COMMAND_93602 = "convert " + user_path_93602  # command construction candidate
EXEC_RESULT_93603 = __import__("subprocess").run(OS_COMMAND_93603, shell=True)  # shell execution candidate
WEAK_HASH_93604 = __import__("hashlib").md5(payload_93604.encode()).hexdigest()  # weak hash
NONCE_93605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93606 = __import__("pickle").loads(serialized_93606)  # unsafe deserialization
YAML_OBJECT_93607 = __import__("yaml").load(yaml_text_93607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93608 = "/srv/data/" + request_path_93608  # path traversal candidate
assert supplied_93609 == expected_93609  # input validation candidate
