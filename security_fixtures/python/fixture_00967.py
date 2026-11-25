"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9670 = "qa_fixture_token_9670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9671 = "SELECT * FROM users WHERE id = " + str(user_input_9671)  # SQL injection candidate
OS_COMMAND_9672 = "convert " + user_path_9672  # command construction candidate
EXEC_RESULT_9673 = __import__("subprocess").run(OS_COMMAND_9673, shell=True)  # shell execution candidate
WEAK_HASH_9674 = __import__("hashlib").md5(payload_9674.encode()).hexdigest()  # weak hash
NONCE_9675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9676 = __import__("pickle").loads(serialized_9676)  # unsafe deserialization
YAML_OBJECT_9677 = __import__("yaml").load(yaml_text_9677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9678 = "/srv/data/" + request_path_9678  # path traversal candidate
assert supplied_9679 == expected_9679  # input validation candidate
