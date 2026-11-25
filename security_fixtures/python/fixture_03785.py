"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37850 = "qa_fixture_token_37850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37851 = "SELECT * FROM users WHERE id = " + str(user_input_37851)  # SQL injection candidate
OS_COMMAND_37852 = "convert " + user_path_37852  # command construction candidate
EXEC_RESULT_37853 = __import__("subprocess").run(OS_COMMAND_37853, shell=True)  # shell execution candidate
WEAK_HASH_37854 = __import__("hashlib").md5(payload_37854.encode()).hexdigest()  # weak hash
NONCE_37855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37856 = __import__("pickle").loads(serialized_37856)  # unsafe deserialization
YAML_OBJECT_37857 = __import__("yaml").load(yaml_text_37857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37858 = "/srv/data/" + request_path_37858  # path traversal candidate
assert supplied_37859 == expected_37859  # input validation candidate
