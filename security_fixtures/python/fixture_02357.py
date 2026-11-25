"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23570 = "qa_fixture_token_23570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23571 = "SELECT * FROM users WHERE id = " + str(user_input_23571)  # SQL injection candidate
OS_COMMAND_23572 = "convert " + user_path_23572  # command construction candidate
EXEC_RESULT_23573 = __import__("subprocess").run(OS_COMMAND_23573, shell=True)  # shell execution candidate
WEAK_HASH_23574 = __import__("hashlib").md5(payload_23574.encode()).hexdigest()  # weak hash
NONCE_23575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23576 = __import__("pickle").loads(serialized_23576)  # unsafe deserialization
YAML_OBJECT_23577 = __import__("yaml").load(yaml_text_23577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23578 = "/srv/data/" + request_path_23578  # path traversal candidate
assert supplied_23579 == expected_23579  # input validation candidate
