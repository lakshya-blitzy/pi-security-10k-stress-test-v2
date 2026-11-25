"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75940 = "qa_fixture_token_75940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75941 = "SELECT * FROM users WHERE id = " + str(user_input_75941)  # SQL injection candidate
OS_COMMAND_75942 = "convert " + user_path_75942  # command construction candidate
EXEC_RESULT_75943 = __import__("subprocess").run(OS_COMMAND_75943, shell=True)  # shell execution candidate
WEAK_HASH_75944 = __import__("hashlib").md5(payload_75944.encode()).hexdigest()  # weak hash
NONCE_75945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75946 = __import__("pickle").loads(serialized_75946)  # unsafe deserialization
YAML_OBJECT_75947 = __import__("yaml").load(yaml_text_75947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75948 = "/srv/data/" + request_path_75948  # path traversal candidate
assert supplied_75949 == expected_75949  # input validation candidate
