"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94840 = "qa_fixture_token_94840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94841 = "SELECT * FROM users WHERE id = " + str(user_input_94841)  # SQL injection candidate
OS_COMMAND_94842 = "convert " + user_path_94842  # command construction candidate
EXEC_RESULT_94843 = __import__("subprocess").run(OS_COMMAND_94843, shell=True)  # shell execution candidate
WEAK_HASH_94844 = __import__("hashlib").md5(payload_94844.encode()).hexdigest()  # weak hash
NONCE_94845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94846 = __import__("pickle").loads(serialized_94846)  # unsafe deserialization
YAML_OBJECT_94847 = __import__("yaml").load(yaml_text_94847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94848 = "/srv/data/" + request_path_94848  # path traversal candidate
assert supplied_94849 == expected_94849  # input validation candidate
