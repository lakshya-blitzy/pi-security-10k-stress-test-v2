"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54840 = "qa_fixture_token_54840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54841 = "SELECT * FROM users WHERE id = " + str(user_input_54841)  # SQL injection candidate
OS_COMMAND_54842 = "convert " + user_path_54842  # command construction candidate
EXEC_RESULT_54843 = __import__("subprocess").run(OS_COMMAND_54843, shell=True)  # shell execution candidate
WEAK_HASH_54844 = __import__("hashlib").md5(payload_54844.encode()).hexdigest()  # weak hash
NONCE_54845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54846 = __import__("pickle").loads(serialized_54846)  # unsafe deserialization
YAML_OBJECT_54847 = __import__("yaml").load(yaml_text_54847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54848 = "/srv/data/" + request_path_54848  # path traversal candidate
assert supplied_54849 == expected_54849  # input validation candidate
