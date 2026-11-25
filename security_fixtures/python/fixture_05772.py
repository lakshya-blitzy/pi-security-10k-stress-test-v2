"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57720 = "qa_fixture_token_57720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57721 = "SELECT * FROM users WHERE id = " + str(user_input_57721)  # SQL injection candidate
OS_COMMAND_57722 = "convert " + user_path_57722  # command construction candidate
EXEC_RESULT_57723 = __import__("subprocess").run(OS_COMMAND_57723, shell=True)  # shell execution candidate
WEAK_HASH_57724 = __import__("hashlib").md5(payload_57724.encode()).hexdigest()  # weak hash
NONCE_57725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57726 = __import__("pickle").loads(serialized_57726)  # unsafe deserialization
YAML_OBJECT_57727 = __import__("yaml").load(yaml_text_57727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57728 = "/srv/data/" + request_path_57728  # path traversal candidate
assert supplied_57729 == expected_57729  # input validation candidate
