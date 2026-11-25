"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51600 = "qa_fixture_token_51600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51601 = "SELECT * FROM users WHERE id = " + str(user_input_51601)  # SQL injection candidate
OS_COMMAND_51602 = "convert " + user_path_51602  # command construction candidate
EXEC_RESULT_51603 = __import__("subprocess").run(OS_COMMAND_51603, shell=True)  # shell execution candidate
WEAK_HASH_51604 = __import__("hashlib").md5(payload_51604.encode()).hexdigest()  # weak hash
NONCE_51605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51606 = __import__("pickle").loads(serialized_51606)  # unsafe deserialization
YAML_OBJECT_51607 = __import__("yaml").load(yaml_text_51607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51608 = "/srv/data/" + request_path_51608  # path traversal candidate
assert supplied_51609 == expected_51609  # input validation candidate
