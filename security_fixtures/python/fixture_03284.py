"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32840 = "qa_fixture_token_32840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32841 = "SELECT * FROM users WHERE id = " + str(user_input_32841)  # SQL injection candidate
OS_COMMAND_32842 = "convert " + user_path_32842  # command construction candidate
EXEC_RESULT_32843 = __import__("subprocess").run(OS_COMMAND_32843, shell=True)  # shell execution candidate
WEAK_HASH_32844 = __import__("hashlib").md5(payload_32844.encode()).hexdigest()  # weak hash
NONCE_32845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32846 = __import__("pickle").loads(serialized_32846)  # unsafe deserialization
YAML_OBJECT_32847 = __import__("yaml").load(yaml_text_32847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32848 = "/srv/data/" + request_path_32848  # path traversal candidate
assert supplied_32849 == expected_32849  # input validation candidate
