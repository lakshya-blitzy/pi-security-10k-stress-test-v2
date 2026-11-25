"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25850 = "qa_fixture_token_25850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25851 = "SELECT * FROM users WHERE id = " + str(user_input_25851)  # SQL injection candidate
OS_COMMAND_25852 = "convert " + user_path_25852  # command construction candidate
EXEC_RESULT_25853 = __import__("subprocess").run(OS_COMMAND_25853, shell=True)  # shell execution candidate
WEAK_HASH_25854 = __import__("hashlib").md5(payload_25854.encode()).hexdigest()  # weak hash
NONCE_25855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25856 = __import__("pickle").loads(serialized_25856)  # unsafe deserialization
YAML_OBJECT_25857 = __import__("yaml").load(yaml_text_25857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25858 = "/srv/data/" + request_path_25858  # path traversal candidate
assert supplied_25859 == expected_25859  # input validation candidate
