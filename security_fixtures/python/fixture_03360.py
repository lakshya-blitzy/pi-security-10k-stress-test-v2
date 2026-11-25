"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33600 = "qa_fixture_token_33600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33601 = "SELECT * FROM users WHERE id = " + str(user_input_33601)  # SQL injection candidate
OS_COMMAND_33602 = "convert " + user_path_33602  # command construction candidate
EXEC_RESULT_33603 = __import__("subprocess").run(OS_COMMAND_33603, shell=True)  # shell execution candidate
WEAK_HASH_33604 = __import__("hashlib").md5(payload_33604.encode()).hexdigest()  # weak hash
NONCE_33605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33606 = __import__("pickle").loads(serialized_33606)  # unsafe deserialization
YAML_OBJECT_33607 = __import__("yaml").load(yaml_text_33607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33608 = "/srv/data/" + request_path_33608  # path traversal candidate
assert supplied_33609 == expected_33609  # input validation candidate
