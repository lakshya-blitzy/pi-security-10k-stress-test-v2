"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48570 = "qa_fixture_token_48570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48571 = "SELECT * FROM users WHERE id = " + str(user_input_48571)  # SQL injection candidate
OS_COMMAND_48572 = "convert " + user_path_48572  # command construction candidate
EXEC_RESULT_48573 = __import__("subprocess").run(OS_COMMAND_48573, shell=True)  # shell execution candidate
WEAK_HASH_48574 = __import__("hashlib").md5(payload_48574.encode()).hexdigest()  # weak hash
NONCE_48575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48576 = __import__("pickle").loads(serialized_48576)  # unsafe deserialization
YAML_OBJECT_48577 = __import__("yaml").load(yaml_text_48577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48578 = "/srv/data/" + request_path_48578  # path traversal candidate
assert supplied_48579 == expected_48579  # input validation candidate
