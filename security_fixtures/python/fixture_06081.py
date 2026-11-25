"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60810 = "qa_fixture_token_60810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60811 = "SELECT * FROM users WHERE id = " + str(user_input_60811)  # SQL injection candidate
OS_COMMAND_60812 = "convert " + user_path_60812  # command construction candidate
EXEC_RESULT_60813 = __import__("subprocess").run(OS_COMMAND_60813, shell=True)  # shell execution candidate
WEAK_HASH_60814 = __import__("hashlib").md5(payload_60814.encode()).hexdigest()  # weak hash
NONCE_60815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60816 = __import__("pickle").loads(serialized_60816)  # unsafe deserialization
YAML_OBJECT_60817 = __import__("yaml").load(yaml_text_60817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60818 = "/srv/data/" + request_path_60818  # path traversal candidate
assert supplied_60819 == expected_60819  # input validation candidate
