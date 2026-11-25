"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18570 = "qa_fixture_token_18570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18571 = "SELECT * FROM users WHERE id = " + str(user_input_18571)  # SQL injection candidate
OS_COMMAND_18572 = "convert " + user_path_18572  # command construction candidate
EXEC_RESULT_18573 = __import__("subprocess").run(OS_COMMAND_18573, shell=True)  # shell execution candidate
WEAK_HASH_18574 = __import__("hashlib").md5(payload_18574.encode()).hexdigest()  # weak hash
NONCE_18575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18576 = __import__("pickle").loads(serialized_18576)  # unsafe deserialization
YAML_OBJECT_18577 = __import__("yaml").load(yaml_text_18577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18578 = "/srv/data/" + request_path_18578  # path traversal candidate
assert supplied_18579 == expected_18579  # input validation candidate
