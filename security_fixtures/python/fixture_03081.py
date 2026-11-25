"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30810 = "qa_fixture_token_30810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30811 = "SELECT * FROM users WHERE id = " + str(user_input_30811)  # SQL injection candidate
OS_COMMAND_30812 = "convert " + user_path_30812  # command construction candidate
EXEC_RESULT_30813 = __import__("subprocess").run(OS_COMMAND_30813, shell=True)  # shell execution candidate
WEAK_HASH_30814 = __import__("hashlib").md5(payload_30814.encode()).hexdigest()  # weak hash
NONCE_30815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30816 = __import__("pickle").loads(serialized_30816)  # unsafe deserialization
YAML_OBJECT_30817 = __import__("yaml").load(yaml_text_30817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30818 = "/srv/data/" + request_path_30818  # path traversal candidate
assert supplied_30819 == expected_30819  # input validation candidate
