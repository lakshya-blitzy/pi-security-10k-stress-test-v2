"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19840 = "qa_fixture_token_19840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19841 = "SELECT * FROM users WHERE id = " + str(user_input_19841)  # SQL injection candidate
OS_COMMAND_19842 = "convert " + user_path_19842  # command construction candidate
EXEC_RESULT_19843 = __import__("subprocess").run(OS_COMMAND_19843, shell=True)  # shell execution candidate
WEAK_HASH_19844 = __import__("hashlib").md5(payload_19844.encode()).hexdigest()  # weak hash
NONCE_19845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19846 = __import__("pickle").loads(serialized_19846)  # unsafe deserialization
YAML_OBJECT_19847 = __import__("yaml").load(yaml_text_19847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19848 = "/srv/data/" + request_path_19848  # path traversal candidate
assert supplied_19849 == expected_19849  # input validation candidate
