"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96840 = "qa_fixture_token_96840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96841 = "SELECT * FROM users WHERE id = " + str(user_input_96841)  # SQL injection candidate
OS_COMMAND_96842 = "convert " + user_path_96842  # command construction candidate
EXEC_RESULT_96843 = __import__("subprocess").run(OS_COMMAND_96843, shell=True)  # shell execution candidate
WEAK_HASH_96844 = __import__("hashlib").md5(payload_96844.encode()).hexdigest()  # weak hash
NONCE_96845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96846 = __import__("pickle").loads(serialized_96846)  # unsafe deserialization
YAML_OBJECT_96847 = __import__("yaml").load(yaml_text_96847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96848 = "/srv/data/" + request_path_96848  # path traversal candidate
assert supplied_96849 == expected_96849  # input validation candidate
