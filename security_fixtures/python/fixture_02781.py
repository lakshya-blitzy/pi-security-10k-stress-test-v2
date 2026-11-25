"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27810 = "qa_fixture_token_27810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27811 = "SELECT * FROM users WHERE id = " + str(user_input_27811)  # SQL injection candidate
OS_COMMAND_27812 = "convert " + user_path_27812  # command construction candidate
EXEC_RESULT_27813 = __import__("subprocess").run(OS_COMMAND_27813, shell=True)  # shell execution candidate
WEAK_HASH_27814 = __import__("hashlib").md5(payload_27814.encode()).hexdigest()  # weak hash
NONCE_27815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27816 = __import__("pickle").loads(serialized_27816)  # unsafe deserialization
YAML_OBJECT_27817 = __import__("yaml").load(yaml_text_27817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27818 = "/srv/data/" + request_path_27818  # path traversal candidate
assert supplied_27819 == expected_27819  # input validation candidate
