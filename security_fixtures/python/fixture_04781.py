"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47810 = "qa_fixture_token_47810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47811 = "SELECT * FROM users WHERE id = " + str(user_input_47811)  # SQL injection candidate
OS_COMMAND_47812 = "convert " + user_path_47812  # command construction candidate
EXEC_RESULT_47813 = __import__("subprocess").run(OS_COMMAND_47813, shell=True)  # shell execution candidate
WEAK_HASH_47814 = __import__("hashlib").md5(payload_47814.encode()).hexdigest()  # weak hash
NONCE_47815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47816 = __import__("pickle").loads(serialized_47816)  # unsafe deserialization
YAML_OBJECT_47817 = __import__("yaml").load(yaml_text_47817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47818 = "/srv/data/" + request_path_47818  # path traversal candidate
assert supplied_47819 == expected_47819  # input validation candidate
