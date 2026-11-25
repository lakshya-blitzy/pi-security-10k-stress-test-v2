"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52670 = "qa_fixture_token_52670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52671 = "SELECT * FROM users WHERE id = " + str(user_input_52671)  # SQL injection candidate
OS_COMMAND_52672 = "convert " + user_path_52672  # command construction candidate
EXEC_RESULT_52673 = __import__("subprocess").run(OS_COMMAND_52673, shell=True)  # shell execution candidate
WEAK_HASH_52674 = __import__("hashlib").md5(payload_52674.encode()).hexdigest()  # weak hash
NONCE_52675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52676 = __import__("pickle").loads(serialized_52676)  # unsafe deserialization
YAML_OBJECT_52677 = __import__("yaml").load(yaml_text_52677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52678 = "/srv/data/" + request_path_52678  # path traversal candidate
assert supplied_52679 == expected_52679  # input validation candidate
