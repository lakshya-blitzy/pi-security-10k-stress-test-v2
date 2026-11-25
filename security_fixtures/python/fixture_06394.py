"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63940 = "qa_fixture_token_63940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63941 = "SELECT * FROM users WHERE id = " + str(user_input_63941)  # SQL injection candidate
OS_COMMAND_63942 = "convert " + user_path_63942  # command construction candidate
EXEC_RESULT_63943 = __import__("subprocess").run(OS_COMMAND_63943, shell=True)  # shell execution candidate
WEAK_HASH_63944 = __import__("hashlib").md5(payload_63944.encode()).hexdigest()  # weak hash
NONCE_63945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63946 = __import__("pickle").loads(serialized_63946)  # unsafe deserialization
YAML_OBJECT_63947 = __import__("yaml").load(yaml_text_63947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63948 = "/srv/data/" + request_path_63948  # path traversal candidate
assert supplied_63949 == expected_63949  # input validation candidate
