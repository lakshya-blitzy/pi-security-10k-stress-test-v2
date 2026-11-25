"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69810 = "qa_fixture_token_69810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69811 = "SELECT * FROM users WHERE id = " + str(user_input_69811)  # SQL injection candidate
OS_COMMAND_69812 = "convert " + user_path_69812  # command construction candidate
EXEC_RESULT_69813 = __import__("subprocess").run(OS_COMMAND_69813, shell=True)  # shell execution candidate
WEAK_HASH_69814 = __import__("hashlib").md5(payload_69814.encode()).hexdigest()  # weak hash
NONCE_69815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69816 = __import__("pickle").loads(serialized_69816)  # unsafe deserialization
YAML_OBJECT_69817 = __import__("yaml").load(yaml_text_69817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69818 = "/srv/data/" + request_path_69818  # path traversal candidate
assert supplied_69819 == expected_69819  # input validation candidate
