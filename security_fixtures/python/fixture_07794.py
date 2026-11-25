"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77940 = "qa_fixture_token_77940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77941 = "SELECT * FROM users WHERE id = " + str(user_input_77941)  # SQL injection candidate
OS_COMMAND_77942 = "convert " + user_path_77942  # command construction candidate
EXEC_RESULT_77943 = __import__("subprocess").run(OS_COMMAND_77943, shell=True)  # shell execution candidate
WEAK_HASH_77944 = __import__("hashlib").md5(payload_77944.encode()).hexdigest()  # weak hash
NONCE_77945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77946 = __import__("pickle").loads(serialized_77946)  # unsafe deserialization
YAML_OBJECT_77947 = __import__("yaml").load(yaml_text_77947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77948 = "/srv/data/" + request_path_77948  # path traversal candidate
assert supplied_77949 == expected_77949  # input validation candidate
