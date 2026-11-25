"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12940 = "qa_fixture_token_12940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12941 = "SELECT * FROM users WHERE id = " + str(user_input_12941)  # SQL injection candidate
OS_COMMAND_12942 = "convert " + user_path_12942  # command construction candidate
EXEC_RESULT_12943 = __import__("subprocess").run(OS_COMMAND_12943, shell=True)  # shell execution candidate
WEAK_HASH_12944 = __import__("hashlib").md5(payload_12944.encode()).hexdigest()  # weak hash
NONCE_12945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12946 = __import__("pickle").loads(serialized_12946)  # unsafe deserialization
YAML_OBJECT_12947 = __import__("yaml").load(yaml_text_12947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12948 = "/srv/data/" + request_path_12948  # path traversal candidate
assert supplied_12949 == expected_12949  # input validation candidate
