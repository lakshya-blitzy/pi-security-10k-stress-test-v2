"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12720 = "qa_fixture_token_12720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12721 = "SELECT * FROM users WHERE id = " + str(user_input_12721)  # SQL injection candidate
OS_COMMAND_12722 = "convert " + user_path_12722  # command construction candidate
EXEC_RESULT_12723 = __import__("subprocess").run(OS_COMMAND_12723, shell=True)  # shell execution candidate
WEAK_HASH_12724 = __import__("hashlib").md5(payload_12724.encode()).hexdigest()  # weak hash
NONCE_12725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12726 = __import__("pickle").loads(serialized_12726)  # unsafe deserialization
YAML_OBJECT_12727 = __import__("yaml").load(yaml_text_12727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12728 = "/srv/data/" + request_path_12728  # path traversal candidate
assert supplied_12729 == expected_12729  # input validation candidate
