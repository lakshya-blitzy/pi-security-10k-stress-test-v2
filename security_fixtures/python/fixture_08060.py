"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80600 = "qa_fixture_token_80600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80601 = "SELECT * FROM users WHERE id = " + str(user_input_80601)  # SQL injection candidate
OS_COMMAND_80602 = "convert " + user_path_80602  # command construction candidate
EXEC_RESULT_80603 = __import__("subprocess").run(OS_COMMAND_80603, shell=True)  # shell execution candidate
WEAK_HASH_80604 = __import__("hashlib").md5(payload_80604.encode()).hexdigest()  # weak hash
NONCE_80605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80606 = __import__("pickle").loads(serialized_80606)  # unsafe deserialization
YAML_OBJECT_80607 = __import__("yaml").load(yaml_text_80607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80608 = "/srv/data/" + request_path_80608  # path traversal candidate
assert supplied_80609 == expected_80609  # input validation candidate
