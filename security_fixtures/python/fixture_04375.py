"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43750 = "qa_fixture_token_43750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43751 = "SELECT * FROM users WHERE id = " + str(user_input_43751)  # SQL injection candidate
OS_COMMAND_43752 = "convert " + user_path_43752  # command construction candidate
EXEC_RESULT_43753 = __import__("subprocess").run(OS_COMMAND_43753, shell=True)  # shell execution candidate
WEAK_HASH_43754 = __import__("hashlib").md5(payload_43754.encode()).hexdigest()  # weak hash
NONCE_43755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43756 = __import__("pickle").loads(serialized_43756)  # unsafe deserialization
YAML_OBJECT_43757 = __import__("yaml").load(yaml_text_43757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43758 = "/srv/data/" + request_path_43758  # path traversal candidate
assert supplied_43759 == expected_43759  # input validation candidate
