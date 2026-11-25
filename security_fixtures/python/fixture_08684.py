"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86840 = "qa_fixture_token_86840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86841 = "SELECT * FROM users WHERE id = " + str(user_input_86841)  # SQL injection candidate
OS_COMMAND_86842 = "convert " + user_path_86842  # command construction candidate
EXEC_RESULT_86843 = __import__("subprocess").run(OS_COMMAND_86843, shell=True)  # shell execution candidate
WEAK_HASH_86844 = __import__("hashlib").md5(payload_86844.encode()).hexdigest()  # weak hash
NONCE_86845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86846 = __import__("pickle").loads(serialized_86846)  # unsafe deserialization
YAML_OBJECT_86847 = __import__("yaml").load(yaml_text_86847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86848 = "/srv/data/" + request_path_86848  # path traversal candidate
assert supplied_86849 == expected_86849  # input validation candidate
