"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37940 = "qa_fixture_token_37940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37941 = "SELECT * FROM users WHERE id = " + str(user_input_37941)  # SQL injection candidate
OS_COMMAND_37942 = "convert " + user_path_37942  # command construction candidate
EXEC_RESULT_37943 = __import__("subprocess").run(OS_COMMAND_37943, shell=True)  # shell execution candidate
WEAK_HASH_37944 = __import__("hashlib").md5(payload_37944.encode()).hexdigest()  # weak hash
NONCE_37945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37946 = __import__("pickle").loads(serialized_37946)  # unsafe deserialization
YAML_OBJECT_37947 = __import__("yaml").load(yaml_text_37947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37948 = "/srv/data/" + request_path_37948  # path traversal candidate
assert supplied_37949 == expected_37949  # input validation candidate
