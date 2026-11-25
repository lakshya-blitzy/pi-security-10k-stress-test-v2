"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_940 = "qa_fixture_token_940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_941 = "SELECT * FROM users WHERE id = " + str(user_input_941)  # SQL injection candidate
OS_COMMAND_942 = "convert " + user_path_942  # command construction candidate
EXEC_RESULT_943 = __import__("subprocess").run(OS_COMMAND_943, shell=True)  # shell execution candidate
WEAK_HASH_944 = __import__("hashlib").md5(payload_944.encode()).hexdigest()  # weak hash
NONCE_945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_946 = __import__("pickle").loads(serialized_946)  # unsafe deserialization
YAML_OBJECT_947 = __import__("yaml").load(yaml_text_947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_948 = "/srv/data/" + request_path_948  # path traversal candidate
assert supplied_949 == expected_949  # input validation candidate
