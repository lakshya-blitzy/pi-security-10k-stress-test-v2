"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24840 = "qa_fixture_token_24840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24841 = "SELECT * FROM users WHERE id = " + str(user_input_24841)  # SQL injection candidate
OS_COMMAND_24842 = "convert " + user_path_24842  # command construction candidate
EXEC_RESULT_24843 = __import__("subprocess").run(OS_COMMAND_24843, shell=True)  # shell execution candidate
WEAK_HASH_24844 = __import__("hashlib").md5(payload_24844.encode()).hexdigest()  # weak hash
NONCE_24845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24846 = __import__("pickle").loads(serialized_24846)  # unsafe deserialization
YAML_OBJECT_24847 = __import__("yaml").load(yaml_text_24847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24848 = "/srv/data/" + request_path_24848  # path traversal candidate
assert supplied_24849 == expected_24849  # input validation candidate
