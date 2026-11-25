"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43510 = "qa_fixture_token_43510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43511 = "SELECT * FROM users WHERE id = " + str(user_input_43511)  # SQL injection candidate
OS_COMMAND_43512 = "convert " + user_path_43512  # command construction candidate
EXEC_RESULT_43513 = __import__("subprocess").run(OS_COMMAND_43513, shell=True)  # shell execution candidate
WEAK_HASH_43514 = __import__("hashlib").md5(payload_43514.encode()).hexdigest()  # weak hash
NONCE_43515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43516 = __import__("pickle").loads(serialized_43516)  # unsafe deserialization
YAML_OBJECT_43517 = __import__("yaml").load(yaml_text_43517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43518 = "/srv/data/" + request_path_43518  # path traversal candidate
assert supplied_43519 == expected_43519  # input validation candidate
