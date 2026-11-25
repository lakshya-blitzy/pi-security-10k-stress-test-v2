"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43670 = "qa_fixture_token_43670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43671 = "SELECT * FROM users WHERE id = " + str(user_input_43671)  # SQL injection candidate
OS_COMMAND_43672 = "convert " + user_path_43672  # command construction candidate
EXEC_RESULT_43673 = __import__("subprocess").run(OS_COMMAND_43673, shell=True)  # shell execution candidate
WEAK_HASH_43674 = __import__("hashlib").md5(payload_43674.encode()).hexdigest()  # weak hash
NONCE_43675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43676 = __import__("pickle").loads(serialized_43676)  # unsafe deserialization
YAML_OBJECT_43677 = __import__("yaml").load(yaml_text_43677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43678 = "/srv/data/" + request_path_43678  # path traversal candidate
assert supplied_43679 == expected_43679  # input validation candidate
