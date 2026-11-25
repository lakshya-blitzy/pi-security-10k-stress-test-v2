"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47570 = "qa_fixture_token_47570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47571 = "SELECT * FROM users WHERE id = " + str(user_input_47571)  # SQL injection candidate
OS_COMMAND_47572 = "convert " + user_path_47572  # command construction candidate
EXEC_RESULT_47573 = __import__("subprocess").run(OS_COMMAND_47573, shell=True)  # shell execution candidate
WEAK_HASH_47574 = __import__("hashlib").md5(payload_47574.encode()).hexdigest()  # weak hash
NONCE_47575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47576 = __import__("pickle").loads(serialized_47576)  # unsafe deserialization
YAML_OBJECT_47577 = __import__("yaml").load(yaml_text_47577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47578 = "/srv/data/" + request_path_47578  # path traversal candidate
assert supplied_47579 == expected_47579  # input validation candidate
