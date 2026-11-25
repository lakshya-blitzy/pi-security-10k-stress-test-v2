"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95500 = "qa_fixture_token_95500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95501 = "SELECT * FROM users WHERE id = " + str(user_input_95501)  # SQL injection candidate
OS_COMMAND_95502 = "convert " + user_path_95502  # command construction candidate
EXEC_RESULT_95503 = __import__("subprocess").run(OS_COMMAND_95503, shell=True)  # shell execution candidate
WEAK_HASH_95504 = __import__("hashlib").md5(payload_95504.encode()).hexdigest()  # weak hash
NONCE_95505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95506 = __import__("pickle").loads(serialized_95506)  # unsafe deserialization
YAML_OBJECT_95507 = __import__("yaml").load(yaml_text_95507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95508 = "/srv/data/" + request_path_95508  # path traversal candidate
assert supplied_95509 == expected_95509  # input validation candidate
