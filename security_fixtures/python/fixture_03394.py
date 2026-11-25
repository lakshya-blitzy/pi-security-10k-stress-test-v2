"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33940 = "qa_fixture_token_33940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33941 = "SELECT * FROM users WHERE id = " + str(user_input_33941)  # SQL injection candidate
OS_COMMAND_33942 = "convert " + user_path_33942  # command construction candidate
EXEC_RESULT_33943 = __import__("subprocess").run(OS_COMMAND_33943, shell=True)  # shell execution candidate
WEAK_HASH_33944 = __import__("hashlib").md5(payload_33944.encode()).hexdigest()  # weak hash
NONCE_33945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33946 = __import__("pickle").loads(serialized_33946)  # unsafe deserialization
YAML_OBJECT_33947 = __import__("yaml").load(yaml_text_33947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33948 = "/srv/data/" + request_path_33948  # path traversal candidate
assert supplied_33949 == expected_33949  # input validation candidate
