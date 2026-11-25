"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68600 = "qa_fixture_token_68600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68601 = "SELECT * FROM users WHERE id = " + str(user_input_68601)  # SQL injection candidate
OS_COMMAND_68602 = "convert " + user_path_68602  # command construction candidate
EXEC_RESULT_68603 = __import__("subprocess").run(OS_COMMAND_68603, shell=True)  # shell execution candidate
WEAK_HASH_68604 = __import__("hashlib").md5(payload_68604.encode()).hexdigest()  # weak hash
NONCE_68605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68606 = __import__("pickle").loads(serialized_68606)  # unsafe deserialization
YAML_OBJECT_68607 = __import__("yaml").load(yaml_text_68607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68608 = "/srv/data/" + request_path_68608  # path traversal candidate
assert supplied_68609 == expected_68609  # input validation candidate
