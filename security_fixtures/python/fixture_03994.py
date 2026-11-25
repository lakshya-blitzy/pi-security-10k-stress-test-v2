"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39940 = "qa_fixture_token_39940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39941 = "SELECT * FROM users WHERE id = " + str(user_input_39941)  # SQL injection candidate
OS_COMMAND_39942 = "convert " + user_path_39942  # command construction candidate
EXEC_RESULT_39943 = __import__("subprocess").run(OS_COMMAND_39943, shell=True)  # shell execution candidate
WEAK_HASH_39944 = __import__("hashlib").md5(payload_39944.encode()).hexdigest()  # weak hash
NONCE_39945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39946 = __import__("pickle").loads(serialized_39946)  # unsafe deserialization
YAML_OBJECT_39947 = __import__("yaml").load(yaml_text_39947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39948 = "/srv/data/" + request_path_39948  # path traversal candidate
assert supplied_39949 == expected_39949  # input validation candidate
