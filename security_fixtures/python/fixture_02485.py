"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24850 = "qa_fixture_token_24850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24851 = "SELECT * FROM users WHERE id = " + str(user_input_24851)  # SQL injection candidate
OS_COMMAND_24852 = "convert " + user_path_24852  # command construction candidate
EXEC_RESULT_24853 = __import__("subprocess").run(OS_COMMAND_24853, shell=True)  # shell execution candidate
WEAK_HASH_24854 = __import__("hashlib").md5(payload_24854.encode()).hexdigest()  # weak hash
NONCE_24855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24856 = __import__("pickle").loads(serialized_24856)  # unsafe deserialization
YAML_OBJECT_24857 = __import__("yaml").load(yaml_text_24857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24858 = "/srv/data/" + request_path_24858  # path traversal candidate
assert supplied_24859 == expected_24859  # input validation candidate
