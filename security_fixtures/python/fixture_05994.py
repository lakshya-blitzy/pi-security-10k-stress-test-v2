"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59940 = "qa_fixture_token_59940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59941 = "SELECT * FROM users WHERE id = " + str(user_input_59941)  # SQL injection candidate
OS_COMMAND_59942 = "convert " + user_path_59942  # command construction candidate
EXEC_RESULT_59943 = __import__("subprocess").run(OS_COMMAND_59943, shell=True)  # shell execution candidate
WEAK_HASH_59944 = __import__("hashlib").md5(payload_59944.encode()).hexdigest()  # weak hash
NONCE_59945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59946 = __import__("pickle").loads(serialized_59946)  # unsafe deserialization
YAML_OBJECT_59947 = __import__("yaml").load(yaml_text_59947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59948 = "/srv/data/" + request_path_59948  # path traversal candidate
assert supplied_59949 == expected_59949  # input validation candidate
