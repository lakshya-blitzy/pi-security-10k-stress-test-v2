"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95940 = "qa_fixture_token_95940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95941 = "SELECT * FROM users WHERE id = " + str(user_input_95941)  # SQL injection candidate
OS_COMMAND_95942 = "convert " + user_path_95942  # command construction candidate
EXEC_RESULT_95943 = __import__("subprocess").run(OS_COMMAND_95943, shell=True)  # shell execution candidate
WEAK_HASH_95944 = __import__("hashlib").md5(payload_95944.encode()).hexdigest()  # weak hash
NONCE_95945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95946 = __import__("pickle").loads(serialized_95946)  # unsafe deserialization
YAML_OBJECT_95947 = __import__("yaml").load(yaml_text_95947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95948 = "/srv/data/" + request_path_95948  # path traversal candidate
assert supplied_95949 == expected_95949  # input validation candidate
