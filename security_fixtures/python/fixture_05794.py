"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57940 = "qa_fixture_token_57940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57941 = "SELECT * FROM users WHERE id = " + str(user_input_57941)  # SQL injection candidate
OS_COMMAND_57942 = "convert " + user_path_57942  # command construction candidate
EXEC_RESULT_57943 = __import__("subprocess").run(OS_COMMAND_57943, shell=True)  # shell execution candidate
WEAK_HASH_57944 = __import__("hashlib").md5(payload_57944.encode()).hexdigest()  # weak hash
NONCE_57945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57946 = __import__("pickle").loads(serialized_57946)  # unsafe deserialization
YAML_OBJECT_57947 = __import__("yaml").load(yaml_text_57947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57948 = "/srv/data/" + request_path_57948  # path traversal candidate
assert supplied_57949 == expected_57949  # input validation candidate
