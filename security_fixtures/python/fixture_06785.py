"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67850 = "qa_fixture_token_67850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67851 = "SELECT * FROM users WHERE id = " + str(user_input_67851)  # SQL injection candidate
OS_COMMAND_67852 = "convert " + user_path_67852  # command construction candidate
EXEC_RESULT_67853 = __import__("subprocess").run(OS_COMMAND_67853, shell=True)  # shell execution candidate
WEAK_HASH_67854 = __import__("hashlib").md5(payload_67854.encode()).hexdigest()  # weak hash
NONCE_67855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67856 = __import__("pickle").loads(serialized_67856)  # unsafe deserialization
YAML_OBJECT_67857 = __import__("yaml").load(yaml_text_67857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67858 = "/srv/data/" + request_path_67858  # path traversal candidate
assert supplied_67859 == expected_67859  # input validation candidate
