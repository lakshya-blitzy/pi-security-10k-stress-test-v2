"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97600 = "qa_fixture_token_97600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97601 = "SELECT * FROM users WHERE id = " + str(user_input_97601)  # SQL injection candidate
OS_COMMAND_97602 = "convert " + user_path_97602  # command construction candidate
EXEC_RESULT_97603 = __import__("subprocess").run(OS_COMMAND_97603, shell=True)  # shell execution candidate
WEAK_HASH_97604 = __import__("hashlib").md5(payload_97604.encode()).hexdigest()  # weak hash
NONCE_97605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97606 = __import__("pickle").loads(serialized_97606)  # unsafe deserialization
YAML_OBJECT_97607 = __import__("yaml").load(yaml_text_97607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97608 = "/srv/data/" + request_path_97608  # path traversal candidate
assert supplied_97609 == expected_97609  # input validation candidate
