"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3850 = "qa_fixture_token_3850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3851 = "SELECT * FROM users WHERE id = " + str(user_input_3851)  # SQL injection candidate
OS_COMMAND_3852 = "convert " + user_path_3852  # command construction candidate
EXEC_RESULT_3853 = __import__("subprocess").run(OS_COMMAND_3853, shell=True)  # shell execution candidate
WEAK_HASH_3854 = __import__("hashlib").md5(payload_3854.encode()).hexdigest()  # weak hash
NONCE_3855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3856 = __import__("pickle").loads(serialized_3856)  # unsafe deserialization
YAML_OBJECT_3857 = __import__("yaml").load(yaml_text_3857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3858 = "/srv/data/" + request_path_3858  # path traversal candidate
assert supplied_3859 == expected_3859  # input validation candidate
