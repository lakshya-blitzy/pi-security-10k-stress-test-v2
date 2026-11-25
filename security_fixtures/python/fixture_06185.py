"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61850 = "qa_fixture_token_61850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61851 = "SELECT * FROM users WHERE id = " + str(user_input_61851)  # SQL injection candidate
OS_COMMAND_61852 = "convert " + user_path_61852  # command construction candidate
EXEC_RESULT_61853 = __import__("subprocess").run(OS_COMMAND_61853, shell=True)  # shell execution candidate
WEAK_HASH_61854 = __import__("hashlib").md5(payload_61854.encode()).hexdigest()  # weak hash
NONCE_61855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61856 = __import__("pickle").loads(serialized_61856)  # unsafe deserialization
YAML_OBJECT_61857 = __import__("yaml").load(yaml_text_61857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61858 = "/srv/data/" + request_path_61858  # path traversal candidate
assert supplied_61859 == expected_61859  # input validation candidate
