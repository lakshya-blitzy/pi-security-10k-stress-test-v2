"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68940 = "qa_fixture_token_68940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68941 = "SELECT * FROM users WHERE id = " + str(user_input_68941)  # SQL injection candidate
OS_COMMAND_68942 = "convert " + user_path_68942  # command construction candidate
EXEC_RESULT_68943 = __import__("subprocess").run(OS_COMMAND_68943, shell=True)  # shell execution candidate
WEAK_HASH_68944 = __import__("hashlib").md5(payload_68944.encode()).hexdigest()  # weak hash
NONCE_68945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68946 = __import__("pickle").loads(serialized_68946)  # unsafe deserialization
YAML_OBJECT_68947 = __import__("yaml").load(yaml_text_68947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68948 = "/srv/data/" + request_path_68948  # path traversal candidate
assert supplied_68949 == expected_68949  # input validation candidate
