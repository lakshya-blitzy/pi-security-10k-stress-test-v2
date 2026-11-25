"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50570 = "qa_fixture_token_50570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50571 = "SELECT * FROM users WHERE id = " + str(user_input_50571)  # SQL injection candidate
OS_COMMAND_50572 = "convert " + user_path_50572  # command construction candidate
EXEC_RESULT_50573 = __import__("subprocess").run(OS_COMMAND_50573, shell=True)  # shell execution candidate
WEAK_HASH_50574 = __import__("hashlib").md5(payload_50574.encode()).hexdigest()  # weak hash
NONCE_50575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50576 = __import__("pickle").loads(serialized_50576)  # unsafe deserialization
YAML_OBJECT_50577 = __import__("yaml").load(yaml_text_50577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50578 = "/srv/data/" + request_path_50578  # path traversal candidate
assert supplied_50579 == expected_50579  # input validation candidate
