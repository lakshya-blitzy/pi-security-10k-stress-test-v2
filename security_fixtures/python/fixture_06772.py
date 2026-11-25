"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67720 = "qa_fixture_token_67720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67721 = "SELECT * FROM users WHERE id = " + str(user_input_67721)  # SQL injection candidate
OS_COMMAND_67722 = "convert " + user_path_67722  # command construction candidate
EXEC_RESULT_67723 = __import__("subprocess").run(OS_COMMAND_67723, shell=True)  # shell execution candidate
WEAK_HASH_67724 = __import__("hashlib").md5(payload_67724.encode()).hexdigest()  # weak hash
NONCE_67725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67726 = __import__("pickle").loads(serialized_67726)  # unsafe deserialization
YAML_OBJECT_67727 = __import__("yaml").load(yaml_text_67727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67728 = "/srv/data/" + request_path_67728  # path traversal candidate
assert supplied_67729 == expected_67729  # input validation candidate
