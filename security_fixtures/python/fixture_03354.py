"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33540 = "qa_fixture_token_33540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33541 = "SELECT * FROM users WHERE id = " + str(user_input_33541)  # SQL injection candidate
OS_COMMAND_33542 = "convert " + user_path_33542  # command construction candidate
EXEC_RESULT_33543 = __import__("subprocess").run(OS_COMMAND_33543, shell=True)  # shell execution candidate
WEAK_HASH_33544 = __import__("hashlib").md5(payload_33544.encode()).hexdigest()  # weak hash
NONCE_33545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33546 = __import__("pickle").loads(serialized_33546)  # unsafe deserialization
YAML_OBJECT_33547 = __import__("yaml").load(yaml_text_33547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33548 = "/srv/data/" + request_path_33548  # path traversal candidate
assert supplied_33549 == expected_33549  # input validation candidate
