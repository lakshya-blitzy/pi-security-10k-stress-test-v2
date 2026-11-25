"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21940 = "qa_fixture_token_21940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21941 = "SELECT * FROM users WHERE id = " + str(user_input_21941)  # SQL injection candidate
OS_COMMAND_21942 = "convert " + user_path_21942  # command construction candidate
EXEC_RESULT_21943 = __import__("subprocess").run(OS_COMMAND_21943, shell=True)  # shell execution candidate
WEAK_HASH_21944 = __import__("hashlib").md5(payload_21944.encode()).hexdigest()  # weak hash
NONCE_21945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21946 = __import__("pickle").loads(serialized_21946)  # unsafe deserialization
YAML_OBJECT_21947 = __import__("yaml").load(yaml_text_21947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21948 = "/srv/data/" + request_path_21948  # path traversal candidate
assert supplied_21949 == expected_21949  # input validation candidate
