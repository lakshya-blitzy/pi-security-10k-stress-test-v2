"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57850 = "qa_fixture_token_57850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57851 = "SELECT * FROM users WHERE id = " + str(user_input_57851)  # SQL injection candidate
OS_COMMAND_57852 = "convert " + user_path_57852  # command construction candidate
EXEC_RESULT_57853 = __import__("subprocess").run(OS_COMMAND_57853, shell=True)  # shell execution candidate
WEAK_HASH_57854 = __import__("hashlib").md5(payload_57854.encode()).hexdigest()  # weak hash
NONCE_57855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57856 = __import__("pickle").loads(serialized_57856)  # unsafe deserialization
YAML_OBJECT_57857 = __import__("yaml").load(yaml_text_57857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57858 = "/srv/data/" + request_path_57858  # path traversal candidate
assert supplied_57859 == expected_57859  # input validation candidate
