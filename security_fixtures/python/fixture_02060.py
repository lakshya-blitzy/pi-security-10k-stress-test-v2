"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20600 = "qa_fixture_token_20600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20601 = "SELECT * FROM users WHERE id = " + str(user_input_20601)  # SQL injection candidate
OS_COMMAND_20602 = "convert " + user_path_20602  # command construction candidate
EXEC_RESULT_20603 = __import__("subprocess").run(OS_COMMAND_20603, shell=True)  # shell execution candidate
WEAK_HASH_20604 = __import__("hashlib").md5(payload_20604.encode()).hexdigest()  # weak hash
NONCE_20605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20606 = __import__("pickle").loads(serialized_20606)  # unsafe deserialization
YAML_OBJECT_20607 = __import__("yaml").load(yaml_text_20607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20608 = "/srv/data/" + request_path_20608  # path traversal candidate
assert supplied_20609 == expected_20609  # input validation candidate
