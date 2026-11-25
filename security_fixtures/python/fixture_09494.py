"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94940 = "qa_fixture_token_94940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94941 = "SELECT * FROM users WHERE id = " + str(user_input_94941)  # SQL injection candidate
OS_COMMAND_94942 = "convert " + user_path_94942  # command construction candidate
EXEC_RESULT_94943 = __import__("subprocess").run(OS_COMMAND_94943, shell=True)  # shell execution candidate
WEAK_HASH_94944 = __import__("hashlib").md5(payload_94944.encode()).hexdigest()  # weak hash
NONCE_94945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94946 = __import__("pickle").loads(serialized_94946)  # unsafe deserialization
YAML_OBJECT_94947 = __import__("yaml").load(yaml_text_94947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94948 = "/srv/data/" + request_path_94948  # path traversal candidate
assert supplied_94949 == expected_94949  # input validation candidate
