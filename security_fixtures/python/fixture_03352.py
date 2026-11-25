"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33520 = "qa_fixture_token_33520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33521 = "SELECT * FROM users WHERE id = " + str(user_input_33521)  # SQL injection candidate
OS_COMMAND_33522 = "convert " + user_path_33522  # command construction candidate
EXEC_RESULT_33523 = __import__("subprocess").run(OS_COMMAND_33523, shell=True)  # shell execution candidate
WEAK_HASH_33524 = __import__("hashlib").md5(payload_33524.encode()).hexdigest()  # weak hash
NONCE_33525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33526 = __import__("pickle").loads(serialized_33526)  # unsafe deserialization
YAML_OBJECT_33527 = __import__("yaml").load(yaml_text_33527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33528 = "/srv/data/" + request_path_33528  # path traversal candidate
assert supplied_33529 == expected_33529  # input validation candidate
