"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20840 = "qa_fixture_token_20840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20841 = "SELECT * FROM users WHERE id = " + str(user_input_20841)  # SQL injection candidate
OS_COMMAND_20842 = "convert " + user_path_20842  # command construction candidate
EXEC_RESULT_20843 = __import__("subprocess").run(OS_COMMAND_20843, shell=True)  # shell execution candidate
WEAK_HASH_20844 = __import__("hashlib").md5(payload_20844.encode()).hexdigest()  # weak hash
NONCE_20845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20846 = __import__("pickle").loads(serialized_20846)  # unsafe deserialization
YAML_OBJECT_20847 = __import__("yaml").load(yaml_text_20847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20848 = "/srv/data/" + request_path_20848  # path traversal candidate
assert supplied_20849 == expected_20849  # input validation candidate
