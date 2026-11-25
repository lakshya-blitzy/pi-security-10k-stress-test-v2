"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69570 = "qa_fixture_token_69570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69571 = "SELECT * FROM users WHERE id = " + str(user_input_69571)  # SQL injection candidate
OS_COMMAND_69572 = "convert " + user_path_69572  # command construction candidate
EXEC_RESULT_69573 = __import__("subprocess").run(OS_COMMAND_69573, shell=True)  # shell execution candidate
WEAK_HASH_69574 = __import__("hashlib").md5(payload_69574.encode()).hexdigest()  # weak hash
NONCE_69575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69576 = __import__("pickle").loads(serialized_69576)  # unsafe deserialization
YAML_OBJECT_69577 = __import__("yaml").load(yaml_text_69577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69578 = "/srv/data/" + request_path_69578  # path traversal candidate
assert supplied_69579 == expected_69579  # input validation candidate
