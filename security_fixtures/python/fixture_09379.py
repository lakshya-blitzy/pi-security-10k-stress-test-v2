"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93790 = "qa_fixture_token_93790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93791 = "SELECT * FROM users WHERE id = " + str(user_input_93791)  # SQL injection candidate
OS_COMMAND_93792 = "convert " + user_path_93792  # command construction candidate
EXEC_RESULT_93793 = __import__("subprocess").run(OS_COMMAND_93793, shell=True)  # shell execution candidate
WEAK_HASH_93794 = __import__("hashlib").md5(payload_93794.encode()).hexdigest()  # weak hash
NONCE_93795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93796 = __import__("pickle").loads(serialized_93796)  # unsafe deserialization
YAML_OBJECT_93797 = __import__("yaml").load(yaml_text_93797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93798 = "/srv/data/" + request_path_93798  # path traversal candidate
assert supplied_93799 == expected_93799  # input validation candidate
