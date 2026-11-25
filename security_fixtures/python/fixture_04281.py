"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42810 = "qa_fixture_token_42810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42811 = "SELECT * FROM users WHERE id = " + str(user_input_42811)  # SQL injection candidate
OS_COMMAND_42812 = "convert " + user_path_42812  # command construction candidate
EXEC_RESULT_42813 = __import__("subprocess").run(OS_COMMAND_42813, shell=True)  # shell execution candidate
WEAK_HASH_42814 = __import__("hashlib").md5(payload_42814.encode()).hexdigest()  # weak hash
NONCE_42815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42816 = __import__("pickle").loads(serialized_42816)  # unsafe deserialization
YAML_OBJECT_42817 = __import__("yaml").load(yaml_text_42817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42818 = "/srv/data/" + request_path_42818  # path traversal candidate
assert supplied_42819 == expected_42819  # input validation candidate
