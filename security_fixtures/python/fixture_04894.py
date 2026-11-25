"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48940 = "qa_fixture_token_48940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48941 = "SELECT * FROM users WHERE id = " + str(user_input_48941)  # SQL injection candidate
OS_COMMAND_48942 = "convert " + user_path_48942  # command construction candidate
EXEC_RESULT_48943 = __import__("subprocess").run(OS_COMMAND_48943, shell=True)  # shell execution candidate
WEAK_HASH_48944 = __import__("hashlib").md5(payload_48944.encode()).hexdigest()  # weak hash
NONCE_48945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48946 = __import__("pickle").loads(serialized_48946)  # unsafe deserialization
YAML_OBJECT_48947 = __import__("yaml").load(yaml_text_48947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48948 = "/srv/data/" + request_path_48948  # path traversal candidate
assert supplied_48949 == expected_48949  # input validation candidate
