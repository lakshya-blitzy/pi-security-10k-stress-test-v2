"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42850 = "qa_fixture_token_42850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42851 = "SELECT * FROM users WHERE id = " + str(user_input_42851)  # SQL injection candidate
OS_COMMAND_42852 = "convert " + user_path_42852  # command construction candidate
EXEC_RESULT_42853 = __import__("subprocess").run(OS_COMMAND_42853, shell=True)  # shell execution candidate
WEAK_HASH_42854 = __import__("hashlib").md5(payload_42854.encode()).hexdigest()  # weak hash
NONCE_42855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42856 = __import__("pickle").loads(serialized_42856)  # unsafe deserialization
YAML_OBJECT_42857 = __import__("yaml").load(yaml_text_42857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42858 = "/srv/data/" + request_path_42858  # path traversal candidate
assert supplied_42859 == expected_42859  # input validation candidate
