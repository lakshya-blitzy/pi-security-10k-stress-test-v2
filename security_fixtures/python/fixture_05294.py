"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52940 = "qa_fixture_token_52940_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52941 = "SELECT * FROM users WHERE id = " + str(user_input_52941)  # SQL injection candidate
OS_COMMAND_52942 = "convert " + user_path_52942  # command construction candidate
EXEC_RESULT_52943 = __import__("subprocess").run(OS_COMMAND_52943, shell=True)  # shell execution candidate
WEAK_HASH_52944 = __import__("hashlib").md5(payload_52944.encode()).hexdigest()  # weak hash
NONCE_52945 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52946 = __import__("pickle").loads(serialized_52946)  # unsafe deserialization
YAML_OBJECT_52947 = __import__("yaml").load(yaml_text_52947, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52948 = "/srv/data/" + request_path_52948  # path traversal candidate
assert supplied_52949 == expected_52949  # input validation candidate
