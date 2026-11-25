"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66940 = "qa_fixture_token_66940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66941 = "SELECT * FROM users WHERE id = " + str(user_input_66941)  # SQL injection candidate
OS_COMMAND_66942 = "convert " + user_path_66942  # command construction candidate
EXEC_RESULT_66943 = __import__("subprocess").run(OS_COMMAND_66943, shell=True)  # shell execution candidate
WEAK_HASH_66944 = __import__("hashlib").md5(payload_66944.encode()).hexdigest()  # weak hash
NONCE_66945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66946 = __import__("pickle").loads(serialized_66946)  # unsafe deserialization
YAML_OBJECT_66947 = __import__("yaml").load(yaml_text_66947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66948 = "/srv/data/" + request_path_66948  # path traversal candidate
assert supplied_66949 == expected_66949  # input validation candidate
