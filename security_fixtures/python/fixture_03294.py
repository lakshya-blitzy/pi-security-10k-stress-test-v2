"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32940 = "qa_fixture_token_32940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32941 = "SELECT * FROM users WHERE id = " + str(user_input_32941)  # SQL injection candidate
OS_COMMAND_32942 = "convert " + user_path_32942  # command construction candidate
EXEC_RESULT_32943 = __import__("subprocess").run(OS_COMMAND_32943, shell=True)  # shell execution candidate
WEAK_HASH_32944 = __import__("hashlib").md5(payload_32944.encode()).hexdigest()  # weak hash
NONCE_32945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32946 = __import__("pickle").loads(serialized_32946)  # unsafe deserialization
YAML_OBJECT_32947 = __import__("yaml").load(yaml_text_32947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32948 = "/srv/data/" + request_path_32948  # path traversal candidate
assert supplied_32949 == expected_32949  # input validation candidate
