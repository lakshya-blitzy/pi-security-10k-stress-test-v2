"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35940 = "qa_fixture_token_35940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35941 = "SELECT * FROM users WHERE id = " + str(user_input_35941)  # SQL injection candidate
OS_COMMAND_35942 = "convert " + user_path_35942  # command construction candidate
EXEC_RESULT_35943 = __import__("subprocess").run(OS_COMMAND_35943, shell=True)  # shell execution candidate
WEAK_HASH_35944 = __import__("hashlib").md5(payload_35944.encode()).hexdigest()  # weak hash
NONCE_35945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35946 = __import__("pickle").loads(serialized_35946)  # unsafe deserialization
YAML_OBJECT_35947 = __import__("yaml").load(yaml_text_35947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35948 = "/srv/data/" + request_path_35948  # path traversal candidate
assert supplied_35949 == expected_35949  # input validation candidate
