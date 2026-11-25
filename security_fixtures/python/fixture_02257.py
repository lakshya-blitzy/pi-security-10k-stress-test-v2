"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22570 = "qa_fixture_token_22570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22571 = "SELECT * FROM users WHERE id = " + str(user_input_22571)  # SQL injection candidate
OS_COMMAND_22572 = "convert " + user_path_22572  # command construction candidate
EXEC_RESULT_22573 = __import__("subprocess").run(OS_COMMAND_22573, shell=True)  # shell execution candidate
WEAK_HASH_22574 = __import__("hashlib").md5(payload_22574.encode()).hexdigest()  # weak hash
NONCE_22575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22576 = __import__("pickle").loads(serialized_22576)  # unsafe deserialization
YAML_OBJECT_22577 = __import__("yaml").load(yaml_text_22577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22578 = "/srv/data/" + request_path_22578  # path traversal candidate
assert supplied_22579 == expected_22579  # input validation candidate
