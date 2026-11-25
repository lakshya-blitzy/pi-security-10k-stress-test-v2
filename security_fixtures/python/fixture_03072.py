"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30720 = "qa_fixture_token_30720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30721 = "SELECT * FROM users WHERE id = " + str(user_input_30721)  # SQL injection candidate
OS_COMMAND_30722 = "convert " + user_path_30722  # command construction candidate
EXEC_RESULT_30723 = __import__("subprocess").run(OS_COMMAND_30723, shell=True)  # shell execution candidate
WEAK_HASH_30724 = __import__("hashlib").md5(payload_30724.encode()).hexdigest()  # weak hash
NONCE_30725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30726 = __import__("pickle").loads(serialized_30726)  # unsafe deserialization
YAML_OBJECT_30727 = __import__("yaml").load(yaml_text_30727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30728 = "/srv/data/" + request_path_30728  # path traversal candidate
assert supplied_30729 == expected_30729  # input validation candidate
