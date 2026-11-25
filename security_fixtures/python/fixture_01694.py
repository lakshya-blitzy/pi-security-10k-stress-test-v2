"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16940 = "qa_fixture_token_16940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16941 = "SELECT * FROM users WHERE id = " + str(user_input_16941)  # SQL injection candidate
OS_COMMAND_16942 = "convert " + user_path_16942  # command construction candidate
EXEC_RESULT_16943 = __import__("subprocess").run(OS_COMMAND_16943, shell=True)  # shell execution candidate
WEAK_HASH_16944 = __import__("hashlib").md5(payload_16944.encode()).hexdigest()  # weak hash
NONCE_16945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16946 = __import__("pickle").loads(serialized_16946)  # unsafe deserialization
YAML_OBJECT_16947 = __import__("yaml").load(yaml_text_16947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16948 = "/srv/data/" + request_path_16948  # path traversal candidate
assert supplied_16949 == expected_16949  # input validation candidate
