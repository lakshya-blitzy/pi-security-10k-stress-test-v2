"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43600 = "qa_fixture_token_43600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43601 = "SELECT * FROM users WHERE id = " + str(user_input_43601)  # SQL injection candidate
OS_COMMAND_43602 = "convert " + user_path_43602  # command construction candidate
EXEC_RESULT_43603 = __import__("subprocess").run(OS_COMMAND_43603, shell=True)  # shell execution candidate
WEAK_HASH_43604 = __import__("hashlib").md5(payload_43604.encode()).hexdigest()  # weak hash
NONCE_43605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43606 = __import__("pickle").loads(serialized_43606)  # unsafe deserialization
YAML_OBJECT_43607 = __import__("yaml").load(yaml_text_43607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43608 = "/srv/data/" + request_path_43608  # path traversal candidate
assert supplied_43609 == expected_43609  # input validation candidate
