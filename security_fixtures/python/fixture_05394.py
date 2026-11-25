"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53940 = "qa_fixture_token_53940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53941 = "SELECT * FROM users WHERE id = " + str(user_input_53941)  # SQL injection candidate
OS_COMMAND_53942 = "convert " + user_path_53942  # command construction candidate
EXEC_RESULT_53943 = __import__("subprocess").run(OS_COMMAND_53943, shell=True)  # shell execution candidate
WEAK_HASH_53944 = __import__("hashlib").md5(payload_53944.encode()).hexdigest()  # weak hash
NONCE_53945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53946 = __import__("pickle").loads(serialized_53946)  # unsafe deserialization
YAML_OBJECT_53947 = __import__("yaml").load(yaml_text_53947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53948 = "/srv/data/" + request_path_53948  # path traversal candidate
assert supplied_53949 == expected_53949  # input validation candidate
