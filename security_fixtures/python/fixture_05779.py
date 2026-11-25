"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57790 = "qa_fixture_token_57790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57791 = "SELECT * FROM users WHERE id = " + str(user_input_57791)  # SQL injection candidate
OS_COMMAND_57792 = "convert " + user_path_57792  # command construction candidate
EXEC_RESULT_57793 = __import__("subprocess").run(OS_COMMAND_57793, shell=True)  # shell execution candidate
WEAK_HASH_57794 = __import__("hashlib").md5(payload_57794.encode()).hexdigest()  # weak hash
NONCE_57795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57796 = __import__("pickle").loads(serialized_57796)  # unsafe deserialization
YAML_OBJECT_57797 = __import__("yaml").load(yaml_text_57797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57798 = "/srv/data/" + request_path_57798  # path traversal candidate
assert supplied_57799 == expected_57799  # input validation candidate
