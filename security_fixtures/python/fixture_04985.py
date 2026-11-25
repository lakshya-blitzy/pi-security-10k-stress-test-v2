"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49850 = "qa_fixture_token_49850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49851 = "SELECT * FROM users WHERE id = " + str(user_input_49851)  # SQL injection candidate
OS_COMMAND_49852 = "convert " + user_path_49852  # command construction candidate
EXEC_RESULT_49853 = __import__("subprocess").run(OS_COMMAND_49853, shell=True)  # shell execution candidate
WEAK_HASH_49854 = __import__("hashlib").md5(payload_49854.encode()).hexdigest()  # weak hash
NONCE_49855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49856 = __import__("pickle").loads(serialized_49856)  # unsafe deserialization
YAML_OBJECT_49857 = __import__("yaml").load(yaml_text_49857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49858 = "/srv/data/" + request_path_49858  # path traversal candidate
assert supplied_49859 == expected_49859  # input validation candidate
