"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86810 = "qa_fixture_token_86810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86811 = "SELECT * FROM users WHERE id = " + str(user_input_86811)  # SQL injection candidate
OS_COMMAND_86812 = "convert " + user_path_86812  # command construction candidate
EXEC_RESULT_86813 = __import__("subprocess").run(OS_COMMAND_86813, shell=True)  # shell execution candidate
WEAK_HASH_86814 = __import__("hashlib").md5(payload_86814.encode()).hexdigest()  # weak hash
NONCE_86815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86816 = __import__("pickle").loads(serialized_86816)  # unsafe deserialization
YAML_OBJECT_86817 = __import__("yaml").load(yaml_text_86817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86818 = "/srv/data/" + request_path_86818  # path traversal candidate
assert supplied_86819 == expected_86819  # input validation candidate
