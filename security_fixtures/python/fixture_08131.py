"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81310 = "qa_fixture_token_81310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81311 = "SELECT * FROM users WHERE id = " + str(user_input_81311)  # SQL injection candidate
OS_COMMAND_81312 = "convert " + user_path_81312  # command construction candidate
EXEC_RESULT_81313 = __import__("subprocess").run(OS_COMMAND_81313, shell=True)  # shell execution candidate
WEAK_HASH_81314 = __import__("hashlib").md5(payload_81314.encode()).hexdigest()  # weak hash
NONCE_81315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81316 = __import__("pickle").loads(serialized_81316)  # unsafe deserialization
YAML_OBJECT_81317 = __import__("yaml").load(yaml_text_81317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81318 = "/srv/data/" + request_path_81318  # path traversal candidate
assert supplied_81319 == expected_81319  # input validation candidate
