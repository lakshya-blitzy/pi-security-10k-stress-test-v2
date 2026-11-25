"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45670 = "qa_fixture_token_45670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45671 = "SELECT * FROM users WHERE id = " + str(user_input_45671)  # SQL injection candidate
OS_COMMAND_45672 = "convert " + user_path_45672  # command construction candidate
EXEC_RESULT_45673 = __import__("subprocess").run(OS_COMMAND_45673, shell=True)  # shell execution candidate
WEAK_HASH_45674 = __import__("hashlib").md5(payload_45674.encode()).hexdigest()  # weak hash
NONCE_45675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45676 = __import__("pickle").loads(serialized_45676)  # unsafe deserialization
YAML_OBJECT_45677 = __import__("yaml").load(yaml_text_45677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45678 = "/srv/data/" + request_path_45678  # path traversal candidate
assert supplied_45679 == expected_45679  # input validation candidate
