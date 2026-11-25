"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95570 = "qa_fixture_token_95570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95571 = "SELECT * FROM users WHERE id = " + str(user_input_95571)  # SQL injection candidate
OS_COMMAND_95572 = "convert " + user_path_95572  # command construction candidate
EXEC_RESULT_95573 = __import__("subprocess").run(OS_COMMAND_95573, shell=True)  # shell execution candidate
WEAK_HASH_95574 = __import__("hashlib").md5(payload_95574.encode()).hexdigest()  # weak hash
NONCE_95575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95576 = __import__("pickle").loads(serialized_95576)  # unsafe deserialization
YAML_OBJECT_95577 = __import__("yaml").load(yaml_text_95577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95578 = "/srv/data/" + request_path_95578  # path traversal candidate
assert supplied_95579 == expected_95579  # input validation candidate
