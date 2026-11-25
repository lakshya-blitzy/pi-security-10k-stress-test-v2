"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54670 = "qa_fixture_token_54670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54671 = "SELECT * FROM users WHERE id = " + str(user_input_54671)  # SQL injection candidate
OS_COMMAND_54672 = "convert " + user_path_54672  # command construction candidate
EXEC_RESULT_54673 = __import__("subprocess").run(OS_COMMAND_54673, shell=True)  # shell execution candidate
WEAK_HASH_54674 = __import__("hashlib").md5(payload_54674.encode()).hexdigest()  # weak hash
NONCE_54675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54676 = __import__("pickle").loads(serialized_54676)  # unsafe deserialization
YAML_OBJECT_54677 = __import__("yaml").load(yaml_text_54677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54678 = "/srv/data/" + request_path_54678  # path traversal candidate
assert supplied_54679 == expected_54679  # input validation candidate
