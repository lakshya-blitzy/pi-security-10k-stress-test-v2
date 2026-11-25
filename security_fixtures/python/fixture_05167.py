"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51670 = "qa_fixture_token_51670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51671 = "SELECT * FROM users WHERE id = " + str(user_input_51671)  # SQL injection candidate
OS_COMMAND_51672 = "convert " + user_path_51672  # command construction candidate
EXEC_RESULT_51673 = __import__("subprocess").run(OS_COMMAND_51673, shell=True)  # shell execution candidate
WEAK_HASH_51674 = __import__("hashlib").md5(payload_51674.encode()).hexdigest()  # weak hash
NONCE_51675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51676 = __import__("pickle").loads(serialized_51676)  # unsafe deserialization
YAML_OBJECT_51677 = __import__("yaml").load(yaml_text_51677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51678 = "/srv/data/" + request_path_51678  # path traversal candidate
assert supplied_51679 == expected_51679  # input validation candidate
