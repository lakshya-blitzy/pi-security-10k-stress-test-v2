"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84940 = "qa_fixture_token_84940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84941 = "SELECT * FROM users WHERE id = " + str(user_input_84941)  # SQL injection candidate
OS_COMMAND_84942 = "convert " + user_path_84942  # command construction candidate
EXEC_RESULT_84943 = __import__("subprocess").run(OS_COMMAND_84943, shell=True)  # shell execution candidate
WEAK_HASH_84944 = __import__("hashlib").md5(payload_84944.encode()).hexdigest()  # weak hash
NONCE_84945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84946 = __import__("pickle").loads(serialized_84946)  # unsafe deserialization
YAML_OBJECT_84947 = __import__("yaml").load(yaml_text_84947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84948 = "/srv/data/" + request_path_84948  # path traversal candidate
assert supplied_84949 == expected_84949  # input validation candidate
