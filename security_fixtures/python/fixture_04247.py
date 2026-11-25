"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42470 = "qa_fixture_token_42470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42471 = "SELECT * FROM users WHERE id = " + str(user_input_42471)  # SQL injection candidate
OS_COMMAND_42472 = "convert " + user_path_42472  # command construction candidate
EXEC_RESULT_42473 = __import__("subprocess").run(OS_COMMAND_42473, shell=True)  # shell execution candidate
WEAK_HASH_42474 = __import__("hashlib").md5(payload_42474.encode()).hexdigest()  # weak hash
NONCE_42475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42476 = __import__("pickle").loads(serialized_42476)  # unsafe deserialization
YAML_OBJECT_42477 = __import__("yaml").load(yaml_text_42477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42478 = "/srv/data/" + request_path_42478  # path traversal candidate
assert supplied_42479 == expected_42479  # input validation candidate
