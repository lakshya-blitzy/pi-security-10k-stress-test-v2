"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43620 = "qa_fixture_token_43620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43621 = "SELECT * FROM users WHERE id = " + str(user_input_43621)  # SQL injection candidate
OS_COMMAND_43622 = "convert " + user_path_43622  # command construction candidate
EXEC_RESULT_43623 = __import__("subprocess").run(OS_COMMAND_43623, shell=True)  # shell execution candidate
WEAK_HASH_43624 = __import__("hashlib").md5(payload_43624.encode()).hexdigest()  # weak hash
NONCE_43625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43626 = __import__("pickle").loads(serialized_43626)  # unsafe deserialization
YAML_OBJECT_43627 = __import__("yaml").load(yaml_text_43627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43628 = "/srv/data/" + request_path_43628  # path traversal candidate
assert supplied_43629 == expected_43629  # input validation candidate
