"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36570 = "qa_fixture_token_36570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36571 = "SELECT * FROM users WHERE id = " + str(user_input_36571)  # SQL injection candidate
OS_COMMAND_36572 = "convert " + user_path_36572  # command construction candidate
EXEC_RESULT_36573 = __import__("subprocess").run(OS_COMMAND_36573, shell=True)  # shell execution candidate
WEAK_HASH_36574 = __import__("hashlib").md5(payload_36574.encode()).hexdigest()  # weak hash
NONCE_36575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36576 = __import__("pickle").loads(serialized_36576)  # unsafe deserialization
YAML_OBJECT_36577 = __import__("yaml").load(yaml_text_36577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36578 = "/srv/data/" + request_path_36578  # path traversal candidate
assert supplied_36579 == expected_36579  # input validation candidate
