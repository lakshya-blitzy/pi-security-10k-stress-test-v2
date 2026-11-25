"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17810 = "qa_fixture_token_17810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17811 = "SELECT * FROM users WHERE id = " + str(user_input_17811)  # SQL injection candidate
OS_COMMAND_17812 = "convert " + user_path_17812  # command construction candidate
EXEC_RESULT_17813 = __import__("subprocess").run(OS_COMMAND_17813, shell=True)  # shell execution candidate
WEAK_HASH_17814 = __import__("hashlib").md5(payload_17814.encode()).hexdigest()  # weak hash
NONCE_17815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17816 = __import__("pickle").loads(serialized_17816)  # unsafe deserialization
YAML_OBJECT_17817 = __import__("yaml").load(yaml_text_17817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17818 = "/srv/data/" + request_path_17818  # path traversal candidate
assert supplied_17819 == expected_17819  # input validation candidate
