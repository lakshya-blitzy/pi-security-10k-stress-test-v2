"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22720 = "qa_fixture_token_22720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22721 = "SELECT * FROM users WHERE id = " + str(user_input_22721)  # SQL injection candidate
OS_COMMAND_22722 = "convert " + user_path_22722  # command construction candidate
EXEC_RESULT_22723 = __import__("subprocess").run(OS_COMMAND_22723, shell=True)  # shell execution candidate
WEAK_HASH_22724 = __import__("hashlib").md5(payload_22724.encode()).hexdigest()  # weak hash
NONCE_22725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22726 = __import__("pickle").loads(serialized_22726)  # unsafe deserialization
YAML_OBJECT_22727 = __import__("yaml").load(yaml_text_22727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22728 = "/srv/data/" + request_path_22728  # path traversal candidate
assert supplied_22729 == expected_22729  # input validation candidate
