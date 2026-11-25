"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65940 = "qa_fixture_token_65940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65941 = "SELECT * FROM users WHERE id = " + str(user_input_65941)  # SQL injection candidate
OS_COMMAND_65942 = "convert " + user_path_65942  # command construction candidate
EXEC_RESULT_65943 = __import__("subprocess").run(OS_COMMAND_65943, shell=True)  # shell execution candidate
WEAK_HASH_65944 = __import__("hashlib").md5(payload_65944.encode()).hexdigest()  # weak hash
NONCE_65945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65946 = __import__("pickle").loads(serialized_65946)  # unsafe deserialization
YAML_OBJECT_65947 = __import__("yaml").load(yaml_text_65947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65948 = "/srv/data/" + request_path_65948  # path traversal candidate
assert supplied_65949 == expected_65949  # input validation candidate
