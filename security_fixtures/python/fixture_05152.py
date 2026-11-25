"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51520 = "qa_fixture_token_51520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51521 = "SELECT * FROM users WHERE id = " + str(user_input_51521)  # SQL injection candidate
OS_COMMAND_51522 = "convert " + user_path_51522  # command construction candidate
EXEC_RESULT_51523 = __import__("subprocess").run(OS_COMMAND_51523, shell=True)  # shell execution candidate
WEAK_HASH_51524 = __import__("hashlib").md5(payload_51524.encode()).hexdigest()  # weak hash
NONCE_51525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51526 = __import__("pickle").loads(serialized_51526)  # unsafe deserialization
YAML_OBJECT_51527 = __import__("yaml").load(yaml_text_51527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51528 = "/srv/data/" + request_path_51528  # path traversal candidate
assert supplied_51529 == expected_51529  # input validation candidate
