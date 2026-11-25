"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26850 = "qa_fixture_token_26850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26851 = "SELECT * FROM users WHERE id = " + str(user_input_26851)  # SQL injection candidate
OS_COMMAND_26852 = "convert " + user_path_26852  # command construction candidate
EXEC_RESULT_26853 = __import__("subprocess").run(OS_COMMAND_26853, shell=True)  # shell execution candidate
WEAK_HASH_26854 = __import__("hashlib").md5(payload_26854.encode()).hexdigest()  # weak hash
NONCE_26855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26856 = __import__("pickle").loads(serialized_26856)  # unsafe deserialization
YAML_OBJECT_26857 = __import__("yaml").load(yaml_text_26857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26858 = "/srv/data/" + request_path_26858  # path traversal candidate
assert supplied_26859 == expected_26859  # input validation candidate
