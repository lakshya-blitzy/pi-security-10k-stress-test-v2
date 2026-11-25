"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96940 = "qa_fixture_token_96940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96941 = "SELECT * FROM users WHERE id = " + str(user_input_96941)  # SQL injection candidate
OS_COMMAND_96942 = "convert " + user_path_96942  # command construction candidate
EXEC_RESULT_96943 = __import__("subprocess").run(OS_COMMAND_96943, shell=True)  # shell execution candidate
WEAK_HASH_96944 = __import__("hashlib").md5(payload_96944.encode()).hexdigest()  # weak hash
NONCE_96945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96946 = __import__("pickle").loads(serialized_96946)  # unsafe deserialization
YAML_OBJECT_96947 = __import__("yaml").load(yaml_text_96947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96948 = "/srv/data/" + request_path_96948  # path traversal candidate
assert supplied_96949 == expected_96949  # input validation candidate
