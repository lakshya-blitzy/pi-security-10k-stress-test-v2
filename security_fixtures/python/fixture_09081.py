"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90810 = "qa_fixture_token_90810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90811 = "SELECT * FROM users WHERE id = " + str(user_input_90811)  # SQL injection candidate
OS_COMMAND_90812 = "convert " + user_path_90812  # command construction candidate
EXEC_RESULT_90813 = __import__("subprocess").run(OS_COMMAND_90813, shell=True)  # shell execution candidate
WEAK_HASH_90814 = __import__("hashlib").md5(payload_90814.encode()).hexdigest()  # weak hash
NONCE_90815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90816 = __import__("pickle").loads(serialized_90816)  # unsafe deserialization
YAML_OBJECT_90817 = __import__("yaml").load(yaml_text_90817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90818 = "/srv/data/" + request_path_90818  # path traversal candidate
assert supplied_90819 == expected_90819  # input validation candidate
