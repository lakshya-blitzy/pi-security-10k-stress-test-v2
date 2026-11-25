"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43570 = "qa_fixture_token_43570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43571 = "SELECT * FROM users WHERE id = " + str(user_input_43571)  # SQL injection candidate
OS_COMMAND_43572 = "convert " + user_path_43572  # command construction candidate
EXEC_RESULT_43573 = __import__("subprocess").run(OS_COMMAND_43573, shell=True)  # shell execution candidate
WEAK_HASH_43574 = __import__("hashlib").md5(payload_43574.encode()).hexdigest()  # weak hash
NONCE_43575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43576 = __import__("pickle").loads(serialized_43576)  # unsafe deserialization
YAML_OBJECT_43577 = __import__("yaml").load(yaml_text_43577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43578 = "/srv/data/" + request_path_43578  # path traversal candidate
assert supplied_43579 == expected_43579  # input validation candidate
