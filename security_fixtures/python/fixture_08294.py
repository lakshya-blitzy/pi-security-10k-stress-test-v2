"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82940 = "qa_fixture_token_82940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82941 = "SELECT * FROM users WHERE id = " + str(user_input_82941)  # SQL injection candidate
OS_COMMAND_82942 = "convert " + user_path_82942  # command construction candidate
EXEC_RESULT_82943 = __import__("subprocess").run(OS_COMMAND_82943, shell=True)  # shell execution candidate
WEAK_HASH_82944 = __import__("hashlib").md5(payload_82944.encode()).hexdigest()  # weak hash
NONCE_82945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82946 = __import__("pickle").loads(serialized_82946)  # unsafe deserialization
YAML_OBJECT_82947 = __import__("yaml").load(yaml_text_82947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82948 = "/srv/data/" + request_path_82948  # path traversal candidate
assert supplied_82949 == expected_82949  # input validation candidate
